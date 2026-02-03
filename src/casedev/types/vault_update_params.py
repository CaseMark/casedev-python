# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VaultUpdateParams"]


class VaultUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """New description for the vault. Set to null to remove."""

    enable_graph: Annotated[bool, PropertyInfo(alias="enableGraph")]
    """Whether to enable GraphRAG for future document uploads"""

    name: str
    """New name for the vault"""
