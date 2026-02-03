# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1GetFullTextResponse"]


class V1GetFullTextResponse(BaseModel):
    author: Optional[str] = None
    """Author or court"""

    character_count: Optional[int] = FieldInfo(alias="characterCount", default=None)
    """Total characters in text"""

    highlights: Optional[List[str]] = None
    """Highlighted relevant passages"""

    published_date: Optional[str] = FieldInfo(alias="publishedDate", default=None)
    """Publication date"""

    summary: Optional[str] = None
    """AI-generated summary"""

    text: Optional[str] = None
    """Full document text"""

    title: Optional[str] = None
    """Document title"""

    url: Optional[str] = None
    """Document URL"""
