# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1DocketParams"]


class V1DocketParams(TypedDict, total=False):
    type: Required[Literal["search", "lookup"]]
    """Search dockets or look up a docket by ID"""

    court: str
    """Optional CourtListener court slug (e.g. "nysd", "ca9", "cafc")"""

    date_filed_after: Annotated[Union[str, date], PropertyInfo(alias="dateFiledAfter", format="iso8601")]
    """Optional lower bound for filing date (YYYY-MM-DD)"""

    date_filed_before: Annotated[Union[str, date], PropertyInfo(alias="dateFiledBefore", format="iso8601")]
    """Optional upper bound for filing date (YYYY-MM-DD)"""

    docket_id: Annotated[str, PropertyInfo(alias="docketId")]
    """CourtListener docket ID (required for lookup)"""

    include_entries: Annotated[bool, PropertyInfo(alias="includeEntries")]
    """Include docket entries/filings in lookup responses"""

    limit: int
    """
    Page size for search results or entry list (default 25 for search, 50 for
    lookup)
    """

    live: bool
    """Reserved for future PACER live fetch support.

    Setting true currently returns 400.
    """

    offset: int
    """Offset for search results or entry list"""

    query: str
    """Case name or party name search query (required for search)"""
