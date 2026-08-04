# cash-ledger

Manual cash tracking — quick-entry for cash spending and income, with a running balance. Standalone for cash-only users.

Part of the [wealthdock](https://github.com/wealthdock) organization — see the [org profile](https://github.com/wealthdock/.github) for how the repos fit together.

## Development Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --all-extras
```

Run linting and type checking:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src tests
```

Run the test suite:

```bash
uv run pytest
```

Run the CLI:

```bash
uv run cash-ledger --version
```

## License

MIT — see [LICENSE](LICENSE).
