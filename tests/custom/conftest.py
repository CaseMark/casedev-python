"""
Pytest configuration for custom (non-Stainless-generated) tests.

Registers the 'smoke' marker so that filterwarnings = ["error"] in
pyproject.toml doesn't turn PytestUnknownMarkWarning into a hard failure.
"""

import pytest


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "smoke: live API smoke tests (read-only, requires CASEDEV_API_KEY)")
