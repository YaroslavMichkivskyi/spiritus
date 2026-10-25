#!/usr/bin/env python3
"""Set up Spiritus on this machine: `python bootstrap.py` (`python3` on macOS / Linux).

Safe to run again. The work is done by arsenal/spiritus-setup/bootstrap.py.
"""

import runpy
from pathlib import Path

runpy.run_path(str(Path(__file__).resolve().parent / "arsenal" / "spiritus-setup" / "bootstrap.py"),
               run_name="__main__")
