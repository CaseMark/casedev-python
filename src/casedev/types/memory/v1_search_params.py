# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V1SearchParams"]


class V1SearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query for semantic matching"""

    category: str
    """Filter by category"""

    tag_1: str
    """Filter by tag_1"""

    tag_10: str
    """Filter by tag_10"""

    tag_11: str
    """Filter by tag_11"""

    tag_12: str
    """Filter by tag_12"""

    tag_2: str
    """Filter by tag_2"""

    tag_3: str
    """Filter by tag_3"""

    tag_4: str
    """Filter by tag_4"""

    tag_5: str
    """Filter by tag_5"""

    tag_6: str
    """Filter by tag_6"""

    tag_7: str
    """Filter by tag_7"""

    tag_8: str
    """Filter by tag_8"""

    tag_9: str
    """Filter by tag_9"""

    top_k: int
    """Maximum number of results to return"""
