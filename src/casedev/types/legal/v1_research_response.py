# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1ResearchResponse", "Candidate"]


class Candidate(BaseModel):
    highlights: Optional[List[str]] = None
    """Highlighted relevant passages"""

    published_date: Optional[str] = FieldInfo(alias="publishedDate", default=None)
    """Publication date"""

    snippet: Optional[str] = None
    """Text excerpt from the document"""

    source: Optional[str] = None
    """Domain of the source"""

    title: Optional[str] = None
    """Title of the document"""

    url: Optional[str] = None
    """URL of the legal source"""


class V1ResearchResponse(BaseModel):
    additional_queries: Optional[List[str]] = FieldInfo(alias="additionalQueries", default=None)
    """Additional queries used"""

    candidates: Optional[List[Candidate]] = None

    found: Optional[int] = None
    """Number of candidates found"""

    hint: Optional[str] = None
    """Usage guidance"""

    jurisdiction: Optional[str] = None
    """Jurisdiction filter applied"""

    query: Optional[str] = None
    """Primary search query"""

    search_type: Optional[str] = FieldInfo(alias="searchType", default=None)
    """Search type used (deep)"""
