# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["V1FindResponse", "Candidate"]


class Candidate(BaseModel):
    snippet: Optional[str] = None
    """Text excerpt from the document"""

    source: Optional[str] = None
    """Domain of the source"""

    title: Optional[str] = None
    """Title of the document"""

    url: Optional[str] = None
    """URL of the legal source"""


class V1FindResponse(BaseModel):
    candidates: Optional[List[Candidate]] = None

    found: Optional[int] = None
    """Number of candidates found"""

    hint: Optional[str] = None
    """Usage guidance"""

    jurisdiction: Optional[str] = None
    """Jurisdiction filter applied"""

    query: Optional[str] = None
    """Original search query"""
