# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1GetCitationsResponse", "Citation", "CitationComponents", "CitationSpan"]


class CitationComponents(BaseModel):
    """Structured Bluebook components. Null if citation format is not recognized."""

    case_name: Optional[str] = FieldInfo(alias="caseName", default=None)
    """Case name, e.g., "Bush v. Gore" """

    court: Optional[str] = None
    """Court identifier"""

    page: Optional[int] = None
    """Starting page number"""

    pin_cite: Optional[int] = FieldInfo(alias="pinCite", default=None)
    """Pin cite (specific page)"""

    reporter: Optional[str] = None
    """Reporter abbreviation, e.g., "U.S." """

    volume: Optional[int] = None
    """Volume number"""

    year: Optional[int] = None
    """Decision year"""


class CitationSpan(BaseModel):
    end: Optional[int] = None

    start: Optional[int] = None


class Citation(BaseModel):
    components: Optional[CitationComponents] = None
    """Structured Bluebook components. Null if citation format is not recognized."""

    found: Optional[bool] = None
    """Whether citation was found in CourtListener database"""

    normalized: Optional[str] = None
    """Normalized citation string"""

    original: Optional[str] = None
    """Original citation as found in text"""

    span: Optional[CitationSpan] = None


class V1GetCitationsResponse(BaseModel):
    citations: Optional[List[Citation]] = None
