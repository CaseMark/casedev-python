# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1VerifyResponse", "Citation", "CitationCandidate", "CitationCase", "CitationSpan", "Summary"]


class CitationCandidate(BaseModel):
    court: Optional[str] = None

    date_decided: Optional[str] = FieldInfo(alias="dateDecided", default=None)

    name: Optional[str] = None

    url: Optional[str] = None


class CitationCase(BaseModel):
    """Case metadata (when verified)"""

    id: Optional[int] = None

    court: Optional[str] = None

    date_decided: Optional[str] = FieldInfo(alias="dateDecided", default=None)

    docket_number: Optional[str] = FieldInfo(alias="docketNumber", default=None)

    name: Optional[str] = None

    parallel_citations: Optional[List[str]] = FieldInfo(alias="parallelCitations", default=None)

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)

    url: Optional[str] = None


class CitationSpan(BaseModel):
    end: Optional[int] = None

    start: Optional[int] = None


class Citation(BaseModel):
    candidates: Optional[List[CitationCandidate]] = None
    """Multiple candidates (when multiple_matches or heuristic verification)"""

    case: Optional[CitationCase] = None
    """Case metadata (when verified)"""

    confidence: Optional[float] = None
    """Confidence score (1.0 for CourtListener, heuristic score for fallback)."""

    normalized: Optional[str] = None
    """Normalized citation string"""

    original: Optional[str] = None
    """Original citation as found in text"""

    span: Optional[CitationSpan] = None

    status: Optional[Literal["verified", "not_found", "multiple_matches"]] = None

    verification_source: Optional[Literal["courtlistener", "heuristic"]] = FieldInfo(
        alias="verificationSource", default=None
    )
    """Source of verification result (heuristic for fallback matches)."""


class Summary(BaseModel):
    multiple_matches: Optional[int] = FieldInfo(alias="multipleMatches", default=None)
    """Citations with multiple possible matches"""

    not_found: Optional[int] = FieldInfo(alias="notFound", default=None)
    """Citations not found in database"""

    total: Optional[int] = None
    """Total citations found"""

    verified: Optional[int] = None
    """Citations verified against real cases"""


class V1VerifyResponse(BaseModel):
    citations: Optional[List[Citation]] = None

    summary: Optional[Summary] = None
