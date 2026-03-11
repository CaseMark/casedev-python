# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["GroupUpdateParams"]


class GroupUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Updated vault group description. Pass null to remove the current description."""

    name: str
    """New human-readable name for the vault group"""
