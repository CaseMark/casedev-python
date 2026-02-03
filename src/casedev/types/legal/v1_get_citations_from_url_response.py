# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1GetCitationsFromURLResponse", "Citations", "CitationsCase", "CitationsRegulation", "CitationsStatute"]


class CitationsCase(BaseModel):
    citation: Optional[str] = None
    """The citation string"""

    count: Optional[int] = None
    """Number of occurrences"""

    type: Optional[str] = None
    """Citation type (usReporter, federalReporter, etc.)"""


class CitationsRegulation(BaseModel):
    citation: Optional[str] = None
    """The citation string"""

    count: Optional[int] = None
    """Number of occurrences"""

    type: Optional[str] = None
    """Citation type (cfr)"""


class CitationsStatute(BaseModel):
    citation: Optional[str] = None
    """The citation string"""

    count: Optional[int] = None
    """Number of occurrences"""

    type: Optional[str] = None
    """Citation type (usc)"""


class Citations(BaseModel):
    cases: Optional[List[CitationsCase]] = None

    regulations: Optional[List[CitationsRegulation]] = None

    statutes: Optional[List[CitationsStatute]] = None


class V1GetCitationsFromURLResponse(BaseModel):
    citations: Optional[Citations] = None

    external_links: Optional[List[str]] = FieldInfo(alias="externalLinks", default=None)
    """External links found in the document"""

    hint: Optional[str] = None
    """Usage guidance"""

    title: Optional[str] = None
    """Document title"""

    total_citations: Optional[int] = FieldInfo(alias="totalCitations", default=None)
    """Total citations found"""

    url: Optional[str] = None
    """Source document URL"""
