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

    acknowledge_pacer_fees: Annotated[bool, PropertyInfo(alias="acknowledgePacerFees")]
    """Required when live: true.

    Acknowledges that PACER fees (up to $3.00 per docket) plus a $0.05 service fee
    will be charged to your account.
    """

    court: str
    """Optional court slug for filtering (e.g.

    "nysd", "ca9", "cafc"). Use legal.listCourts() to find slugs.
    """

    date_filed_after: Annotated[Union[str, date], PropertyInfo(alias="dateFiledAfter", format="iso8601")]
    """Optional lower bound for filing date (YYYY-MM-DD)"""

    date_filed_before: Annotated[Union[str, date], PropertyInfo(alias="dateFiledBefore", format="iso8601")]
    """Optional upper bound for filing date (YYYY-MM-DD)"""

    docket_id: Annotated[str, PropertyInfo(alias="docketId")]
    """Docket ID (required for lookup)"""

    include_entries: Annotated[bool, PropertyInfo(alias="includeEntries")]
    """Include docket entries/filings in lookup responses.

    Coming soon — currently returns 501. The parameter is accepted for forward
    compatibility.
    """

    limit: int
    """
    Page size for search results or entry list (default 25 for search, 50 for
    lookup)
    """

    live: bool
    """Trigger a live PACER fetch for dockets not yet in the RECAP archive.

    Requires acknowledgePacerFees: true. PACER charges up to $3.00 per docket sheet
    plus a $0.05 service fee. Only valid with type: "lookup".
    """

    offset: int
    """Offset for search results or entry list"""

    query: str
    """Case name or party name search query (required for search)"""
