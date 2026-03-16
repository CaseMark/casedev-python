# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CustomListParams"]


class CustomListParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination (skill ID from previous page)"""

    limit: int
    """Maximum number of results (1-100)"""

    tag: str
    """Filter by tag"""
