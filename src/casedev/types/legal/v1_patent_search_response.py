# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1PatentSearchResponse", "Result"]


class Result(BaseModel):
    application_number: Optional[str] = FieldInfo(alias="applicationNumber", default=None)
    """Patent application serial number"""

    application_type: Optional[str] = FieldInfo(alias="applicationType", default=None)
    """Application type (Utility, Design, Plant, etc.)"""

    assignees: Optional[List[str]] = None
    """List of assignee/owner names"""

    entity_status: Optional[str] = FieldInfo(alias="entityStatus", default=None)
    """Entity status (e.g. "Small Entity", "Micro Entity")"""

    filing_date: Optional[date] = FieldInfo(alias="filingDate", default=None)
    """Date the application was filed"""

    grant_date: Optional[date] = FieldInfo(alias="grantDate", default=None)
    """Date the patent was granted"""

    inventors: Optional[List[str]] = None
    """List of inventor names"""

    patent_number: Optional[str] = FieldInfo(alias="patentNumber", default=None)
    """Granted patent number (if granted)"""

    status: Optional[str] = None
    """Current application status (e.g. "Patented Case", "Pending")"""

    title: Optional[str] = None
    """Invention title"""


class V1PatentSearchResponse(BaseModel):
    limit: Optional[int] = None
    """Number of results returned"""

    offset: Optional[int] = None
    """Current pagination offset"""

    query: Optional[str] = None
    """Original search query"""

    results: Optional[List[Result]] = None
    """Array of matching patent applications"""

    total_results: Optional[int] = FieldInfo(alias="totalResults", default=None)
    """Total number of matching patent applications"""
