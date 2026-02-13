# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1PatentSearchParams"]


class V1PatentSearchParams(TypedDict, total=False):
    query: Required[str]
    """Free-text search across all patent fields, or field-specific query (e.g.

    "applicationMetaData.patentNumber:11234567"). Supports AND, OR, NOT operators.
    """

    application_status: Annotated[str, PropertyInfo(alias="applicationStatus")]
    """Filter by application status (e.g. "Patented Case", "Abandoned", "Pending")"""

    application_type: Annotated[
        Literal["Utility", "Design", "Plant", "Provisional", "Reissue"], PropertyInfo(alias="applicationType")
    ]
    """Filter by application type"""

    assignee: str
    """Filter by assignee/owner name (e.g. "Google LLC")"""

    filing_date_from: Annotated[Union[str, date], PropertyInfo(alias="filingDateFrom", format="iso8601")]
    """Start of filing date range (YYYY-MM-DD)"""

    filing_date_to: Annotated[Union[str, date], PropertyInfo(alias="filingDateTo", format="iso8601")]
    """End of filing date range (YYYY-MM-DD)"""

    grant_date_from: Annotated[Union[str, date], PropertyInfo(alias="grantDateFrom", format="iso8601")]
    """Start of grant date range (YYYY-MM-DD)"""

    grant_date_to: Annotated[Union[str, date], PropertyInfo(alias="grantDateTo", format="iso8601")]
    """End of grant date range (YYYY-MM-DD)"""

    inventor: str
    """Filter by inventor name"""

    limit: int
    """Number of results to return (default 25, max 100)"""

    offset: int
    """Starting position for pagination"""

    sort_by: Annotated[Literal["filingDate", "grantDate"], PropertyInfo(alias="sortBy")]
    """Field to sort results by"""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Sort order (default desc, newest first)"""
