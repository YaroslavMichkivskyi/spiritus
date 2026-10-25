#!/usr/bin/env python3
"""bootstrap: first-time (and repeat-safe) setup of Spiritus on this machine.

1. checks the requirements (doctor);
2. installs the `spiritus` command: a tiny shim in a user bin folder that runs
   arsenal/spiritus-cli/spiritus_cli.py with this Python;
3. puts that folder on PATH (asks first);
4. restores my modules from modules.local.json, if any;
5. says what to do next.

Run from the repo root: `python bootstrap.py [--yes]` (`python3` on macOS / Linux).
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import doctor  # noqa: E402

ROOT = doctor.ROOT
MODULES = ROOT / "arsenal" / "spiritus-module-manager" / "modules.py"
MODULES_LOCAL = MODULES.parent / "modules.local.json"
RC_MARK = "# spiritus: user bin folder on PATH"


def ask(question, assume_yes):
    if assume_yes:
        return True
    skipped = "-> skipped (no terminal; pass --yes)"
    if not sys.stdin.isatty():
        print(f"{question} {skipped}")
        return False
    try:
        answer = input(f"{question} [Y/n] ")
    except EOFError:  # Windows reports NUL as a terminal
        print(skipped)
        return False
    return answer.strip().lower() in ("", "y", "yes", "д", "да")


# --- PATH -------------------------------------------------------------------

def add_to_path_win(directory):
    import ctypes
    import winreg
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0,
                        winreg.KEY_READ | winreg.KEY_WRITE) as key:
        try:
            value, kind = winreg.QueryValueEx(key, "Path")
        except OSError:
            value, kind = "", winreg.REG_EXPAND_SZ
        parts = [p for p in value.split(";") if p]
        parts.append(str(directory))
        winreg.SetValueEx(key, "Path", 0, kind, ";".join(parts))
    # tell Explorer & co. that the environment changed (new terminals see it)
    HWND_BROADCAST, WM_SETTINGCHANGE, SMTO_ABORTIFHUNG = 0xFFFF, 0x1A, 0x2
    ctypes.windll.user32.SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0,
                                             "Environment", SMTO_ABORTIFHUNG, 3000, None)
    return "user PATH (Windows registry)"


def rc_file():
    shell = os.path.basename(os.environ.get("SHELL", ""))
    home = Path.home()
    if shell == "zsh":
        return home / ".zshrc"
    if shell == "bash":
        return home / (".bash_profile" if sys.platform == "darwin" else ".bashrc")
    return home / ".profile"


def add_to_path_posix(directory):
    rc = rc_file()
    text = rc.read_text(encoding="utf-8") if rc.exists() else ""
    if RC_MARK not in text:
        line = f'export PATH="{directory}:$PATH"'
        with open(rc, "a", encoding="utf-8", newline="\n") as f:
            f.write(f"\n{RC_MARK}\n{line}\n")
    return str(rc)


# --- steps ----------------------------------------------------------------

def install_shim(assume_yes):
    shim = doctor.shim_path()
    if shim.exists():
        target = doctor.parse_shim(shim.read_text(encoding="utf-8", errors="replace"))
        if target is None:
            print(f"{shim} exists and is not a Spiritus shim - leaving it alone")
            return False
        if os.path.normcase(str(target[1])) != os.path.normcase(str(doctor.CLI)):
            if not ask(f"`spiritus` now points to {target[1].parents[2]} - switch it to {ROOT}?",
                       assume_yes):
                return False
    shim.parent.mkdir(parents=True, exist_ok=True)
    with open(shim, "w", encoding="utf-8", newline="") as f:
        f.write(doctor.shim_text(sys.executable, doctor.CLI))
    if sys.platform != "win32":
        shim.chmod(0o755)
    print(f"installed `spiritus` -> {shim}")
    return True


def ensure_path(assume_yes):
    directory = doctor.shim_dir()
    if doctor.dir_on_path(directory):
        return
    if not ask(f"add {directory} to PATH so `spiritus` works in any terminal?", assume_yes):
        print(f"  -> skipped; run it as {doctor.shim_path()} or add the folder yourself")
        return
    where = add_to_path_win(directory) if sys.platform == "win32" else add_to_path_posix(directory)
    print(f"added to {where} - open a new terminal for it to apply")


def restore_modules():
    # both commands also write spiritus.code-workspace
    command = "workspace"
    if MODULES_LOCAL.exists():
        print("restoring modules from modules.local.json", flush=True)
        command = "sync"
    sys.stdout.flush()
    subprocess.run([sys.executable, str(MODULES), command], cwd=ROOT)


def main():
    p = argparse.ArgumentParser(description="Set up Spiritus on this machine.")
    p.add_argument("--yes", "-y", action="store_true", help="answer yes to every question")
    args = p.parse_args()

    print("Spiritus bootstrap\n\n1. requirements")
    base = [doctor.check_python, doctor.check_git, doctor.check_clone]
    if not doctor.report(base):
        print("\nfix the FAIL lines above, then run bootstrap again")
        sys.exit(1)
    rest_ok = doctor.report([doctor.check_git_identity, doctor.check_node, doctor.check_runtime])

    print("\n2. `spiritus` command")
    if install_shim(args.yes):
        ensure_path(args.yes)
    restore_modules()

    print("\n3. result")
    doctor.report([doctor.check_cli])
    print("\nnext:" if rest_ok else "\nnext (after fixing the FAIL lines):")
    print("  - open a new terminal in this folder")
    print("  - start your agent there (`claude` or `codex`) and say: \"set me up\"")
    print("  - check the machine any time: `spiritus run doctor`")


if __name__ == "__main__":
    main()
