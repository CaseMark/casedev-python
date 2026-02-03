# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ObjectGetOcrWordsParams"]


class ObjectGetOcrWordsParams(TypedDict, total=False):
    id: Required[str]

    page: int
    """Filter to a specific page number (1-indexed). If omitted, returns all pages."""

    word_end: Annotated[int, PropertyInfo(alias="wordEnd")]
    """Filter to words ending at this index (inclusive).

    Useful for retrieving words for a specific chunk.
    """

    word_start: Annotated[int, PropertyInfo(alias="wordStart")]
    """Filter to words starting at this index (inclusive).

    Useful for retrieving words for a specific chunk.
    """
