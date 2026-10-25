#!/usr/bin/env python3
"""spiritus-module-manager: daemons and domains kept in their own git repos.

A module is a git repo cloned into `daemons/<name>/` or `domains/<name>/`.
Standard modules are listed in `catalog.json` (tracked); what *I* installed,
plus my private modules, is in `modules.local.json` (gitignored). Installed
modules are hidden from the platform repo via `.git/info/exclude`, and their
row in the realm's `registry.md` is generated from the module's frontmatter.

Run `python arsenal/spiritus-module-manager/modules.py --help`.
"""

import argparse
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CATALOG = HERE / "catalog.json"
LOCAL = HERE / "modules.local.json"
EXCLUDE_TAG = "# spiritus-module-manager: installed modules"

# kind -> realm folder, registry header, frontmatter fields for the row cells
KINDS = {
    "daemon": {"dir": "daemons", "header": ["Daemon", "Summon when", "Works for"],
               "fields": ["when", "works-for"]},
    "domain": {"dir": "domains", "header": ["Domain", "About", "Enter when"],
               "fields": ["about", "when"]},
}
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


class Fail(Exception):
    pass


# --- helpers -------------------------------------------------------------

def git(*args, cwd=ROOT, check=True):
    res = subprocess.run(["git", *args], cwd=cwd, capture_output=True,
                         text=True, encoding="utf-8", errors="replace")
    if check and res.returncode != 0:
        raise Fail(f"git {' '.join(args)} failed:\n{res.stderr.strip()}")
    return res.stdout.strip()


def load(path):
    if not path.exists():
        return {"modules": {}}
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    data.setdefault("modules", {})
    return data


def save(path, data):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def write_lines(path, lines):
    # open(): Path.write_text has no newline= before Python 3.10
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def module_path(kind, name):
    return ROOT / KINDS[kind]["dir"] / name


def rel(path):
    return path.relative_to(ROOT).as_posix()


def check_entry(name, entry):
    if not NAME_RE.match(name):
        raise Fail(f"bad module name '{name}': lowercase kebab-case only")
    if entry.get("kind") not in KINDS:
        raise Fail(f"module '{name}': kind must be one of {', '.join(KINDS)}")
    if not entry.get("url"):
        raise Fail(f"module '{name}': no url")


def rmtree(path):
    # git marks pack files read-only; Windows refuses to delete them as-is
    def force(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)
    if sys.version_info >= (3, 12):
        shutil.rmtree(path, onexc=force)
    else:
        shutil.rmtree(path, onerror=force)


# --- frontmatter and registry ------------------------------------------------

def frontmatter(path):
    """`key: value` lines between leading `---` fences of the module's AGENTS.md."""
    charter = path / "AGENTS.md"
    if not charter.exists():
        return {}
    lines = charter.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        key, sep, value = line.partition(":")
        if sep:
            meta[key.strip().lower()] = value.strip()
    return meta


def registry_file(kind):
    return ROOT / KINDS[kind]["dir"] / "registry.md"


def row_prefix(name):
    return f"| `{name}/` |"


def set_registry_row(kind, name, path):
    spec = KINDS[kind]
    meta = frontmatter(path)
    missing = [f for f in spec["fields"] if not meta.get(f)]
    if missing:
        print(f"  ! {rel(path)}/AGENTS.md has no frontmatter {', '.join(missing)} - "
              f"fill that row of {rel(registry_file(kind))} by hand")
    cells = [f"`{name}/`"] + [meta.get(f) or "-" for f in spec["fields"]]
    row = "| " + " | ".join(c.replace("|", "\\|") for c in cells) + " |"

    reg = registry_file(kind)
    if reg.exists():
        lines = reg.read_text(encoding="utf-8").splitlines()
    else:
        lines = [f"# {spec['dir']} — my registry", "",
                 "| " + " | ".join(spec["header"]) + " |",
                 "|" + "---|" * len(spec["header"])]
    for i, line in enumerate(lines):
        if line.startswith(row_prefix(name)):
            lines[i] = row
            break
    else:
        last = max((i for i, l in enumerate(lines) if l.startswith("|")), default=None)
        if last is None:
            lines += ["", "| " + " | ".join(spec["header"]) + " |",
                      "|" + "---|" * len(spec["header"])]
            last = len(lines) - 1
        lines.insert(last + 1, row)
    write_lines(reg, lines)


def drop_registry_row(kind, name):
    reg = registry_file(kind)
    if not reg.exists():
        return
    lines = reg.read_text(encoding="utf-8").splitlines()
    kept = [l for l in lines if not l.startswith(row_prefix(name))]
    if kept != lines:
        write_lines(reg, kept)


# --- git exclude (keeps module repos out of the platform repo) ---------------

def exclude_file():
    return ROOT / git("rev-parse", "--git-path", "info/exclude")


def set_excluded(path, on):
    excl = exclude_file()
    entry = f"/{rel(path)}/"
    lines = excl.read_text(encoding="utf-8").splitlines() if excl.exists() else []
    lines = [l for l in lines if l.strip() != entry]
    if on:
        # exclude files have no inline comments: tag once, entries below it
        if EXCLUDE_TAG not in lines:
            lines.append(EXCLUDE_TAG)
        lines.append(entry)
    excl.parent.mkdir(parents=True, exist_ok=True)
    write_lines(excl, lines)


# --- repo state ---------------------------------------------------------

def repo_state(path, fetch=False):
    if fetch:
        git("fetch", "--quiet", cwd=path, check=False)
    branch = git("rev-parse", "--abbrev-ref", "HEAD", cwd=path, check=False) or "?"
    dirty = len([l for l in git("status", "--porcelain", cwd=path).splitlines() if l])
    ahead = behind = None
    counts = git("rev-list", "--left-right", "--count", "@{upstream}...HEAD",
                 cwd=path, check=False)
    if counts:
        behind, ahead = (int(x) for x in counts.split())
    return {"branch": branch, "dirty": dirty, "ahead": ahead, "behind": behind}


def describe(state):
    parts = [state["branch"]]
    parts.append(f"{state['dirty']} changed" if state["dirty"] else "clean")
    if state["ahead"] is None:
        parts.append("no upstream")
    else:
        if state["ahead"]:
            parts.append(f"{state['ahead']} to push")
        if state["behind"]:
            parts.append(f"{state['behind']} to pull")
    return ", ".join(parts)


# --- commands -------------------------------------------------------------

def clone(name, entry):
    check_entry(name, entry)
    path = module_path(entry["kind"], name)
    if path.exists():
        raise Fail(f"{rel(path)} already exists - remove it first or pick another name")
    print(f"cloning {entry['url']} -> {rel(path)}")
    git("clone", "--quiet", entry["url"], str(path))
    if entry.get("ref"):
        git("checkout", "--quiet", entry["ref"], cwd=path)
    set_excluded(path, True)
    set_registry_row(entry["kind"], name, path)


def cmd_list(args):
    catalog = load(CATALOG)["modules"]
    local = load(LOCAL)["modules"]
    names = sorted(set(catalog) | set(local))
    if not names:
        print("no modules in the catalog or in modules.local.json")
        return
    for name in names:
        entry = local.get(name) or catalog[name]
        source = "catalog" if name in catalog else "private"
        installed = module_path(entry["kind"], name).exists()
        about = catalog.get(name, {}).get("about", "")
        mark = "installed" if installed else "-"
        print(f"{name:28} {entry['kind']:7} {source:8} {mark:10} {about}")


def cmd_install(args):
    catalog = load(CATALOG)["modules"]
    if args.name not in catalog:
        raise Fail(f"'{args.name}' is not in catalog.json - private module? use `add`")
    entry = {k: catalog[args.name][k] for k in ("kind", "url")}
    entry["source"] = "catalog"
    if args.ref:
        entry["ref"] = args.ref
    clone(args.name, entry)
    local = load(LOCAL)
    local["modules"][args.name] = entry
    save(LOCAL, local)
    print("done")


def cmd_add(args):
    name = args.name or re.sub(r"\.git$", "", args.url.rstrip("/").split("/")[-1].split(":")[-1])
    entry = {"kind": args.kind, "url": args.url, "source": "private"}
    if args.ref:
        entry["ref"] = args.ref
    clone(name, entry)
    local = load(LOCAL)
    local["modules"][name] = entry
    save(LOCAL, local)
    print("done")


def cmd_sync(args):
    local = load(LOCAL)["modules"]
    todo = [n for n, e in local.items() if not module_path(e["kind"], n).exists()]
    if not todo:
        print("all modules from modules.local.json are installed")
    for name in todo:
        clone(name, local[name])
    print("done")


def cmd_update(args):
    local = load(LOCAL)["modules"]
    names = [args.name] if args.name else sorted(local)
    for name in names:
        if name not in local:
            raise Fail(f"'{name}' is not installed by the module manager")
        entry = local[name]
        path = module_path(entry["kind"], name)
        if not path.exists():
            print(f"{name}: not on disk - run `sync`")
            continue
        if entry.get("ref"):
            git("fetch", "--quiet", cwd=path)
            git("checkout", "--quiet", entry["ref"], cwd=path)
            print(f"{name}: at {entry['ref']}")
        else:
            res = subprocess.run(["git", "pull", "--ff-only", "--quiet"], cwd=path,
                                 capture_output=True, text=True)
            print(f"{name}: " + ("updated" if res.returncode == 0
                                 else "NOT updated - " + res.stderr.strip()))
        set_registry_row(entry["kind"], name, path)


def cmd_status(args):
    local = load(LOCAL)["modules"]
    tracked = set(git("ls-files").splitlines())
    for kind, spec in KINDS.items():
        realm = ROOT / spec["dir"]
        dirs = sorted(p for p in realm.iterdir() if p.is_dir()) if realm.exists() else []
        print(f"{spec['dir']}/")
        if not dirs:
            print("  (empty)")
        for path in dirs:
            name = path.name
            if (path / ".git").exists():
                kind_label = "module" if name in local else "repo (not managed)"
                print(f"  {name:26} {kind_label:20} {describe(repo_state(path, args.fetch))}")
            elif any(t.startswith(rel(path) + "/") for t in tracked):
                print(f"  {name:26} in platform repo")
            else:
                print(f"  {name:26} local folder")


def cmd_remove(args):
    local = load(LOCAL)
    entry = local["modules"].get(args.name)
    if not entry:
        raise Fail(f"'{args.name}' is not installed by the module manager")
    path = module_path(entry["kind"], args.name)
    if path.exists():
        state = repo_state(path)
        # commits reachable from any local branch / HEAD but from no remote
        unpushed = int(git("rev-list", "--count", "HEAD", "--branches", "--not",
                           "--remotes", cwd=path, check=False) or 0)
        if (state["dirty"] or unpushed) and not args.force:
            raise Fail(f"{rel(path)}: {state['dirty']} changed, {unpushed} unpushed "
                       f"commit(s) - work would be lost; commit and push, or pass --force")
        rmtree(path)
    set_excluded(path, False)
    drop_registry_row(entry["kind"], args.name)
    del local["modules"][args.name]
    save(LOCAL, local)
    print(f"removed {args.name}")


def main():
    p = argparse.ArgumentParser(prog="modules.py", description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list", help="catalog + my modules, installed or not")
    s = sub.add_parser("install", help="install a standard module from catalog.json")
    s.add_argument("name")
    s.add_argument("--ref", help="branch / tag / commit to pin")
    s = sub.add_parser("add", help="add my own (private) module by git URL")
    s.add_argument("url")
    s.add_argument("--kind", required=True, choices=sorted(KINDS))
    s.add_argument("--name", help="folder name (default: repo name)")
    s.add_argument("--ref", help="branch / tag / commit to pin")
    sub.add_parser("sync", help="clone every module from modules.local.json that is missing")
    s = sub.add_parser("update", help="pull one / all modules, refresh their registry rows")
    s.add_argument("name", nargs="?")
    s = sub.add_parser("status", help="every daemon / domain folder and its git state")
    s.add_argument("--fetch", action="store_true", help="fetch first (network)")
    s = sub.add_parser("remove", help="delete a module folder (refuses to lose work)")
    s.add_argument("name")
    s.add_argument("--force", action="store_true")
    args = p.parse_args()
    try:
        globals()["cmd_" + args.cmd](args)
    except Fail as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
