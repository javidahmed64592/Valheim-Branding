# Valheim Branding - AI Agent Instructions

## Project Overview

Visual branding rules and icon generator for the Aestelwen Valheim mods. `valheim_branding/build_icons.py` composes one 256x256 Thunderstore icon per glyph in `assets/glyphs/`, using the tokens in `tokens/` and the mark in `assets/mark/`. Rules are written up in `BRAND.md`. The project uses Python 3.13+, `uv`, `ruff`, `ty`, and `pytest`, with build configuration using hatchling.

## Package Management with uv

- **Always use `uv` commands**, not `pip` - this project is managed exclusively with `uv`
- Install dependencies: `uv sync` (core) or `uv sync --extra dev` (with dev tools)
- Run commands: `uv run <command>` (e.g., `uv run pytest`, `uv run ty check .`)
- Update dependencies: `uv lock --upgrade`
- Version pinned in `.python-version` (currently 3.13)

## Code Quality Standards

### Ruff Configuration (pyproject.toml)

- Line length: 120 characters
- Target: Python 3.13
- Extensive rule selection including: type annotations (ANN), docstrings (D), performance (PERF), pandas (PD), numpy (NPY)
- **Docstring convention**: Google style via `[tool.ruff.lint.pydocstyle]`
- **Ignored rules**: D203, D213 (conflicting docstring rules), PLR0913 (too many arguments), S101 (assert allowed in tests)
- `__init__.py` files excluded from linting via `extend-exclude`

### Type Checking (ty)

- **All functions require type annotations** - never omit return types or parameter types

### Testing (pytest)

- Configuration in `pyproject.toml` under `[tool.pytest.ini_options]`
- Always run with coverage: `uv run pytest` (coverage enabled by default via `addopts`)
- **Coverage requirements**: Minimum 95% coverage enforced via `fail_under = 95`
- **Branch coverage enabled**: Tracks both line and branch coverage
- Coverage report format: `term-missing` shows uncovered lines
- Test files in `tests/` directory follow `test_*.py` naming

### Security Scanning

- **bandit** - scans Python code for security vulnerabilities
- **pip-audit** - audits dependencies for known security issues
- Both run automatically in CI pipeline
- Run locally: `uv run bandit -r valheim_branding/` and `uv run pip-audit`

## Development Workflow

### Before Committing

1. Format: `uv run ruff format .`
2. Lint: `uv run ruff check .`
3. Type check: `uv run ty check .`
4. Test: `uv run pytest`

## Code Style Patterns

### Module Documentation

Every Python file starts with a module-level docstring:

```python
"""Brief description of module purpose."""
```

### Function Signatures

Always include complete type annotations:

```python
def example_function() -> str:
    """Return a string."""
    return "This is an example function."
```

### Test Structure

Tests mirror the source structure and use descriptive names:

```python
def test_example_function() -> None:
    """Test the example_function."""
    result = example_function()
    assert result == "This is an example function."
```

## Project Structure

- `.github/` - GitHub workflows and actions
- `assets/` - the Longhouse A mark and one glyph SVG per mod
- `tokens/` - palette and layout tokens
- `docs/` - documentation files
- `valheim_branding/` - main package code
- `tests/` - pytest test files
- `.python-version` - Python version specification for `uv` and CI
- `pyproject.toml` - single source of truth for all configuration (build, dependencies, tooling)
- `uv.lock` - locked dependency versions

## Version Management

- Package version defined in `pyproject.toml` under `[project]` → `version`
- CI validates version consistency across `pyproject.toml` and `uv.lock`
