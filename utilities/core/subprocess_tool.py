# Shrek was proudly coded by Shrek™ [https://github.com/SHREK-TM].

import os
import subprocess
import sys

from utilities.core.shrek_ui import show_banner

TOOLS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tools")


def run_tool_script(relative_path: str, title: str = "Shrek Multi Tools"):
    """Execute a script under utilities/tools/ with the correct working directory."""
    script_path = os.path.join(TOOLS_DIR, relative_path.replace("/", os.sep))
    if not os.path.isfile(script_path):
        print(f"[Error] Script not found: {script_path}")
        return 1

    work_dir = os.path.dirname(script_path)
    if not os.path.isdir(work_dir):
        work_dir = TOOLS_DIR

    show_banner(title)
    result = subprocess.run([sys.executable, script_path], cwd=work_dir)
    return result.returncode
