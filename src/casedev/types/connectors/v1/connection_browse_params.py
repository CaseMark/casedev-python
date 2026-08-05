# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConnectionBrowseParams"]


class ConnectionBrowseParams(TypedDict, total=False):
    container: str
    """Container id to list, or the container containing parent"""

    cursor: str

    page_size: int

    parent: str
    """Folder id to list"""

    query: str
    """Optional provider-supported search text"""

    site: str
    """Site id to list"""
