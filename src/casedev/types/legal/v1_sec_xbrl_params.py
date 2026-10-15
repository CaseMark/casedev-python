# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["V1SecXbrlParams"]


class V1SecXbrlParams(TypedDict, total=False):
    type: Required[Literal["concept", "facts", "frames"]]
    """concept: one line item for one company over time.

    facts: all concepts for one company (catalog, or values for the concepts you
    list). frames: one concept across all companies for one period.
    """

    cik: str
    """Company CIK, padded or unpadded (concept and facts).

    Provide exactly one of cik or ticker.
    """

    ciks: SequenceNotStr[str]
    """frames only. Restrict results to these CIKs (peer set)."""

    concepts: SequenceNotStr[str]
    """facts only.

    "taxonomy:tag" strings or bare tags (default us-gaap). Omit to get the concept
    catalog, which has no values.
    """

    date_after: Annotated[Union[str, date], PropertyInfo(alias="dateAfter", format="iso8601")]
    """concept and facts.

    Only facts whose period end date is on or after this date (YYYY-MM-DD).
    """

    date_before: Annotated[Union[str, date], PropertyInfo(alias="dateBefore", format="iso8601")]
    """concept and facts.

    Only facts whose period end date is on or before this date (YYYY-MM-DD).
    """

    dedupe: bool
    """concept and facts.

    When true, keep only facts the SEC assigned a calendar frame (its canonical fact
    per period), dropping prior-period comparatives re-reported in later filings.
    When false, return every reported fact.
    """

    fiscal_periods: Annotated[List[Literal["FY", "Q1", "Q2", "Q3"]], PropertyInfo(alias="fiscalPeriods")]
    """concept and facts. Filter by fiscal period."""

    form_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="formTypes")]
    """concept and facts. Filter by SEC form type such as 10-K or 10-Q."""

    limit: int
    """Maximum rows to return"""

    offset: int
    """Result offset for pagination"""

    period: str
    """frames only, required.

    CY2024 = annual duration, CY2024Q1 = quarterly duration, CY2024Q1I =
    instantaneous (balance sheet items).
    """

    sort: Literal["value_desc", "value_asc"]
    """frames only. Sort order by value."""

    tag: str
    """XBRL element name such as NetIncomeLoss (required for concept and frames)"""

    taxonomy: Literal["us-gaap", "ifrs-full", "dei", "srt"]
    """XBRL taxonomy. For facts it only filters the catalog and has no default."""

    ticker: str
    """Company ticker (concept and facts). Provide exactly one of cik or ticker."""

    tickers: SequenceNotStr[str]
    """frames only. Restrict results to these tickers (peer set)."""

    unit: str
    """Unit such as USD, shares, or USD/shares.

    Optional filter for concept; defaults to USD for frames (the SEC URL form
    USD-per-shares is also accepted).
    """
