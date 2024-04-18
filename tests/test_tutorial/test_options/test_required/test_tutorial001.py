import subprocess
import sys

import cligenius
import cligenius.core
from cligenius.testing import CliRunner

from docs_src.options.required import tutorial001 as mod

runner = CliRunner()

app = cligenius.Cligenius()
app.command()(mod.main)


def test_1():
    result = runner.invoke(app, ["Camila"])
    assert result.exit_code != 0
    assert "Missing option '--lastname'." in result.output


def test_option_lastname():
    result = runner.invoke(app, ["Camila", "--lastname", "Gutiérrez"])
    assert result.exit_code == 0
    assert "Hello Camila Gutiérrez" in result.output


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "--lastname" in result.output
    assert "TEXT" in result.output
    assert "[required]" in result.output


def test_help_no_rich():
    rich = cligenius.core.rich
    cligenius.core.rich = None
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "--lastname" in result.output
    assert "TEXT" in result.output
    assert "[required]" in result.output
    cligenius.core.rich = rich


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
