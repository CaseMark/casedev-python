# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectGetOcrWordsResponse", "Page", "PageWord"]


class PageWord(BaseModel):
    bbox: Optional[List[float]] = None
    """Bounding box [x0, y0, x1, y1] normalized to 0-1 range"""

    confidence: Optional[float] = None
    """OCR confidence score (0-1)"""

    text: Optional[str] = None
    """The word text"""

    word_index: Optional[int] = FieldInfo(alias="wordIndex", default=None)
    """Global word index across the entire document (0-based)"""


class Page(BaseModel):
    page: Optional[int] = None
    """Page number (1-indexed)"""

    words: Optional[List[PageWord]] = None


class ObjectGetOcrWordsResponse(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the OCR data was extracted"""

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)
    """The object ID"""

    page_count: Optional[int] = FieldInfo(alias="pageCount", default=None)
    """Total number of pages in the document"""

    pages: Optional[List[Page]] = None
    """Per-page word data with bounding boxes"""

    total_words: Optional[int] = FieldInfo(alias="totalWords", default=None)
    """Total number of words extracted from the document"""
