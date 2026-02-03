# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1SimilarResponse", "SimilarSource"]


class SimilarSource(BaseModel):
    published_date: Optional[str] = FieldInfo(alias="publishedDate", default=None)
    """Publication date"""

    snippet: Optional[str] = None
    """Text excerpt from the document"""

    source: Optional[str] = None
    """Domain of the source"""

    title: Optional[str] = None
    """Title of the document"""

    url: Optional[str] = None
    """URL of the similar source"""


class V1SimilarResponse(BaseModel):
    found: Optional[int] = None
    """Number of similar sources found"""

    hint: Optional[str] = None
    """Usage guidance"""

    jurisdiction: Optional[str] = None
    """Jurisdiction filter applied"""

    similar_sources: Optional[List[SimilarSource]] = FieldInfo(alias="similarSources", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)
    """Original source URL"""
