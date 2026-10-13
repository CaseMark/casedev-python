# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConnectionUpdateAllParams"]


class ConnectionUpdateAllParams(TypedDict, total=False):
    confirm_organization_wide: Required[Literal[True]]
    """Confirms that this change applies to every user connection in scope."""

    enabled: Required[bool]

    provider: Required[str]
