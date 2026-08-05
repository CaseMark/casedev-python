# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConnectionCreateParams"]


class ConnectionCreateParams(TypedDict, total=False):
    provider: Required[Literal["clio", "gdrive", "microsoft"]]

    return_url: Required[str]
    """HTTPS URL the user is sent back to after consent."""

    scope_tier: Literal["clio.us", "drive", "microsoft.read"]
    """Provider-specific OAuth permission tier. Omit to use the provider's default."""
