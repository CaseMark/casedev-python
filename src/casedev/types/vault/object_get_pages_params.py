# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ObjectGetPagesParams"]


class ObjectGetPagesParams(TypedDict, total=False):
    id: Required[str]

    end: int
    """Last page to return (inclusive, 1-indexed).

    If omitted, returns through the last page with text.
    """

    start: int
    """First page to return (inclusive, 1-indexed).

    If omitted, starts at the first page with text.
    """
