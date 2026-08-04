"""Smoke tests for the CLI."""

from typer.testing import CliRunner

from cash_ledger import __version__
from cash_ledger.cli import app

runner = CliRunner()


def test_version_flag() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout
