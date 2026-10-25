#!/usr/bin/env python3
"""spiritus doctor: check that this machine has what Spiritus needs.

Prints one line per check (ok / warn / FAIL) with how to fix it; exits 1 if
anything required is missing. Changes nothing. Used by bootstrap.py too.
"""

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLI = ROOT / "arsenal" / "spiritus-cli" / "spiritus_cli.py"
README = "README.md -> Requirements"
MIN_PYTHON = (3, 9)
MIN_NODE = 18


def run(*cmd):
    """stdout of a command, or None if it can't be started / fails."""
    exe = shutil.which(cmd[0])
    if not exe:
        return None
    try:
        res = subprocess.run([exe, *cmd[1:]], capture_output=True, text=True,
                             encoding="utf-8", errors="replace", timeout=20)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return res.stdout.strip() if res.returncode == 0 else None


def version_of(text):
    m = re.search(r"(\d+)\.(\d+)(?:\.(\d+))?", text or "")
    return tuple(int(x or 0) for x in m.groups()) if m else None


# --- shim location (shared with bootstrap.py) ------------------------------

def shim_dir():
    # the same folder the Claude Code and uv installers use on every OS,
    # so it is often on PATH already
    return Path.home() / ".local" / "bin"


def shim_path():
    return shim_dir() / ("spiritus.cmd" if sys.platform == "win32" else "spiritus")


SHIM_RE = re.compile(r'"([^"]+)" "([^"]+)"')


def shim_text(python, cli):
    if sys.platform == "win32":
        return ("@echo off\r\nrem spiritus shim, written by bootstrap.py\r\n"
                f'"{python}" "{cli}" %*\r\n')
    return ("#!/bin/sh\n# spiritus shim, written by bootstrap.py\n"
            f'exec "{python}" "{cli}" "$@"\n')


def parse_shim(text):
    """(python, cli) the shim runs, or None."""
    m = SHIM_RE.search(text)
    return (Path(m.group(1)), Path(m.group(2))) if m else None


def dir_on_path(directory):
    target = os.path.normcase(os.path.normpath(str(directory)))
    for part in os.environ.get("PATH", "").split(os.pathsep):
        if part and os.path.normcase(os.path.normpath(os.path.expandvars(part))) == target:
            return True
    if sys.platform == "win32":
        # set by bootstrap for new terminals, not yet in this process
        return target in [os.path.normcase(os.path.normpath(p)) for p in user_path_win()]
    return False


def user_path_win():
    import winreg
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as key:
            value, _ = winreg.QueryValueEx(key, "Path")
    except OSError:
        return []
    return [os.path.expandvars(p) for p in value.split(";") if p]


# --- checks ---------------------------------------------------------------
# each returns (level, what, fix) with level in "ok" / "warn" / "fail"

def check_python():
    v = sys.version_info[:3]
    shown = ".".join(map(str, v))
    if v < MIN_PYTHON:
        return "fail", f"Python {shown}", f"need Python >= {'.'.join(map(str, MIN_PYTHON))} ({README})"
    return "ok", f"Python {shown}", ""


def check_git():
    v = version_of(run("git", "--version"))
    if not v:
        return "fail", "git not found", f"install git ({README})"
    return "ok", f"git {'.'.join(map(str, v))}", ""


def check_clone():
    if not (ROOT / ".git").exists():
        return "fail", "repo is not a git clone", "get Spiritus with `git clone`, not as a zip"
    return "ok", "git clone", ""


def check_git_identity():
    name, email = run("git", "config", "user.name"), run("git", "config", "user.email")
    if not (name and email):
        return ("warn", "git user.name / user.email not set",
                'git config --global user.name "Your Name" && '
                'git config --global user.email you@example.com')
    return "ok", f"git identity: {name} <{email}>", ""


def check_node():
    v = version_of(run("node", "--version"))
    if not v:
        return "warn", "Node.js not found", f"needed only for Node-based MCP servers ({README})"
    if v[0] < MIN_NODE:
        return "warn", f"Node.js {v[0]}", f"MCP servers expect Node >= {MIN_NODE}"
    return "ok", f"Node.js {'.'.join(map(str, v))}", ""


def check_runtime():
    found = [name for name, cmd in (("Claude Code", "claude"), ("Codex", "codex"))
             if shutil.which(cmd)]
    if not found:
        return "fail", "no agent runtime (claude / codex)", f"install Claude Code or Codex CLI ({README})"
    return "ok", "runtime: " + ", ".join(found), ""


def check_cli():
    shim = shim_path()
    if not shim.exists():
        return "fail", "`spiritus` command not installed", "run `python bootstrap.py`"
    target = parse_shim(shim.read_text(encoding="utf-8", errors="replace"))
    if not target:
        return "fail", f"{shim} is not a Spiritus shim", "remove it, then run `python bootstrap.py`"
    python, cli = target
    if os.path.normcase(str(cli)) != os.path.normcase(str(CLI)):
        return "fail", f"`spiritus` points to another copy ({cli.parents[2]})", "run `python bootstrap.py` here"
    if not python.exists():
        return "fail", "`spiritus` uses a Python that no longer exists", "run `python bootstrap.py`"
    if not dir_on_path(shim.parent):
        return "fail", f"{shim.parent} is not on PATH", "run `python bootstrap.py` (it offers to add it)"
    if not shutil.which("spiritus"):
        return "warn", "`spiritus` installed", "open a new terminal to pick up PATH"
    return "ok", "`spiritus` command", ""


CHECKS = [check_python, check_git, check_clone, check_git_identity, check_node,
          check_runtime, check_cli]


def report(checks=CHECKS):
    """print the checks; True if nothing required is missing."""
    ok = True
    for check in checks:
        level, what, fix = check()
        mark = {"ok": "  ok  ", "warn": " warn ", "fail": " FAIL "}[level]
        print(f"[{mark}] {what}" + (f"\n         -> {fix}" if fix else ""))
        ok = ok and level != "fail"
    return ok


def main():
    print("Spiritus doctor\n")
    ok = report()
    print("\nall required checks passed" if ok else "\nfix the FAIL lines above")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
