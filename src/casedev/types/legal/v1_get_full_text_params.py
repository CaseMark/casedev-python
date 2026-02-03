# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1GetFullTextParams"]


class V1GetFullTextParams(TypedDict, total=False):
    url: Required[str]
    """URL of the verified legal document"""

    highlight_query: Annotated[str, PropertyInfo(alias="highlightQuery")]
    """Optional query to extract relevant highlights (e.g., "What is the holding?")"""

    max_characters: Annotated[int, PropertyInfo(alias="maxCharacters")]
    """Maximum characters to return (default: 10000, max: 50000)"""

    summary_query: Annotated[str, PropertyInfo(alias="summaryQuery")]
    """Optional query for generating a summary (e.g., "Summarize the key ruling")"""
