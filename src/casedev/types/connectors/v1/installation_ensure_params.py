# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InstallationEnsureParams"]


class InstallationEnsureParams(TypedDict, total=False):
    application: Required[str]
    """Consuming application key (e.g. "p3")."""

    external_tenant_id: Required[str]
    """The application's own tenant identifier (e.g. a P3 organization id)."""
