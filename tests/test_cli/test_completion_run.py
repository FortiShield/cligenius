import os
import subprocess
import sys


def test_script_completion_run():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", "-m", "types"],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "___MAIN__.PY_COMPLETE": "complete_bash",
            "_PYTHON _M TYPES_COMPLETE": "complete_bash",
            "COMP_WORDS": "types tests/assets/cli/sample.py",
            "COMP_CWORD": "2",
        },
    )
    assert "run" in result.stdout