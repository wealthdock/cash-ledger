"""Command-line interface for cash_ledger."""

import typer

from cash_ledger import __version__

app = typer.Typer(help="Manual cash tracking with a running balance.")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        callback=_version_callback,
        is_eager=True,
        help="Show the version and exit.",
    ),
) -> None:
    """cash-ledger CLI."""


if __name__ == "__main__":
    app()
