import os
import subprocess
import sys

from docs_src.commands.help import tutorial001 as mod


def test_completion_complete_subcommand_bash():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL001.PY_COMPLETE": "complete_bash",
            "COMP_WORDS": "tutorial001.py del",
            "COMP_CWORD": "1",
        },
    )
    assert "delete\ndelete-all" in result.stdout


def test_completion_complete_subcommand_bash_invalid():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL001.PY_COMPLETE": "complete_bash",
            "COMP_WORDS": "tutorial001.py del",
            "COMP_CWORD": "42",
        },
    )
    assert "create\ndelete\ndelete-all\ninit" in result.stdout


def test_completion_complete_subcommand_zsh():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL001.PY_COMPLETE": "complete_zsh",
            "_TYPES_COMPLETE_ARGS": "tutorial001.py del",
        },
    )
    assert (
        """_arguments '*: :(("delete":"Delete a user with USERNAME."\n"""
        """\"delete-all":"Delete ALL users in the database."))'"""
    ) in result.stdout


def test_completion_complete_subcommand_zsh_files():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL001.PY_COMPLETE": "complete_zsh",
            "_TYPES_COMPLETE_ARGS": "tutorial001.py delete ",
        },
    )
    assert ("_files") in result.stdout


def test_completion_complete_subcommand_fish():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL001.PY_COMPLETE": "complete_fish",
            "_TYPES_COMPLETE_ARGS": "tutorial001.py del",
            "_TYPES_COMPLETE_FISH_ACTION": "get-args",
        },
    )
    assert (
        "delete\tDelete a user with USERNAME.\ndelete-all\tDelete ALL users in the database."
        in result.stdout
    )


def test_completion_complete_subcommand_fish_should_complete():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL001.PY_COMPLETE": "complete_fish",
            "_TYPES_COMPLETE_ARGS": "tutorial001.py del",
            "_TYPES_COMPLETE_FISH_ACTION": "is-args",
        },
    )
    assert result.returncode == 0


def test_completion_complete_subcommand_fish_should_complete_no():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL001.PY_COMPLETE": "complete_fish",
            "_TYPES_COMPLETE_ARGS": "tutorial001.py delete ",
            "_TYPES_COMPLETE_FISH_ACTION": "is-args",
        },
    )
    assert result.returncode != 0


def test_completion_complete_subcommand_powershell():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL001.PY_COMPLETE": "complete_powershell",
            "_TYPES_COMPLETE_ARGS": "tutorial001.py del",
        },
    )
    assert (
        "delete:::Delete a user with USERNAME.\ndelete-all:::Delete ALL users in the database."
    ) in result.stdout


def test_completion_complete_subcommand_pwsh():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL001.PY_COMPLETE": "complete_pwsh",
            "_TYPES_COMPLETE_ARGS": "tutorial001.py del",
        },
    )
    assert (
        "delete:::Delete a user with USERNAME.\ndelete-all:::Delete ALL users in the database."
    ) in result.stdout


def test_completion_complete_subcommand_noshell():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL001.PY_COMPLETE": "complete_noshell",
            "_TYPES_COMPLETE_ARGS": "tutorial001.py del",
        },
    )
    assert ("") in result.stdout