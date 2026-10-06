# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SkillCatalogParams"]


class SkillCatalogParams(TypedDict, total=False):
    limit: int
    """Maximum results to return"""

    offset: int
    """Number of results to skip"""

    q: str
    """Optional text search"""

    source: Literal["custom", "curated"]
    """
    Optional source filter, applied after organization overrides and before
    pagination. Omit to browse both sources.
    """

    tag: str
    """Optional tag filter"""
