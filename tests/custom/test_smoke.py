"""
Live API smoke tests for the CaseDev Python SDK.

These tests hit a real API server (staging or production) to verify
the SDK works end-to-end. They are intentionally read-only — no
resources are created, mutated, or deleted.

This file is custom code that persists across Stainless SDK regeneration
since Stainless never touches files it didn't generate.

Configuration (via environment variables):
  CASEDEV_API_KEY       - Required. A valid API key for the target environment.
  CASEDEV_BASE_URL      - Optional. Defaults to https://api.case.dev.

Usage:
  pytest tests/custom/ -m smoke
  pytest tests/custom/ -m smoke --timeout=30
"""

from __future__ import annotations

import os

import pytest

from casedev import Casedev

# ---------------------------------------------------------------------------
# Skip the entire module if no API key is configured.
# This lets the test suite run cleanly in environments that only have
# Prism (mock) credentials.
# ---------------------------------------------------------------------------
pytestmark = pytest.mark.smoke

LIVE_API_KEY = os.environ.get("CASEDEV_API_KEY")

skip_no_api_key = pytest.mark.skipif(
    not LIVE_API_KEY,
    reason="CASEDEV_API_KEY not set — live smoke tests require a real API key",
)


@pytest.fixture(scope="module")
def live_client() -> Casedev:
    """Create a SDK client pointed at the live (or staging) API."""
    return Casedev(
        # CASEDEV_BASE_URL is picked up automatically by the client if set.
        # If unset, the client defaults to https://api.case.dev (production).
    )


# ---------------------------------------------------------------------------
# Smoke tests — read-only, no side effects
# ---------------------------------------------------------------------------


@skip_no_api_key
class TestLlmSmoke:
    """Validate the /llm/config endpoint returns a well-formed model list."""

    def test_get_config_returns_models(self, live_client: Casedev) -> None:
        config = live_client.llm.get_config()
        assert config.models is not None, "Expected models list, got None"
        assert len(config.models) > 0, "Expected at least one model in config"

    def test_get_config_model_has_required_fields(self, live_client: Casedev) -> None:
        config = live_client.llm.get_config()
        model = config.models[0]
        assert model.id, "Model missing 'id'"
        assert model.name, "Model missing 'name'"
        assert model.api_model_type, "Model missing 'modelType'"

    def test_get_config_raw_response(self, live_client: Casedev) -> None:
        """Verify the raw HTTP response is well-formed."""
        response = live_client.llm.with_raw_response.get_config()
        assert response.status_code == 200
        assert "application/json" in response.headers.get("content-type", "")


@skip_no_api_key
class TestVaultSmoke:
    """Validate the /vault list endpoint returns a well-formed response."""

    def test_vault_list_returns_response(self, live_client: Casedev) -> None:
        result = live_client.vault.list()
        # total can be 0 for a fresh org, but the field should exist
        assert result.total is not None, "Expected 'total' field in vault list response"
        assert result.vaults is not None, "Expected 'vaults' list in response"

    def test_vault_list_raw_response(self, live_client: Casedev) -> None:
        """Verify the raw HTTP response is well-formed."""
        response = live_client.vault.with_raw_response.list()
        assert response.status_code == 200
        assert "application/json" in response.headers.get("content-type", "")
