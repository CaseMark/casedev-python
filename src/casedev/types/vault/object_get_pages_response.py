# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ObjectGetPagesResponse", "Metadata", "Page"]


class Metadata(BaseModel):
    filename: str

    object_id: str

    page_count: int
    """Total number of pages with extracted text in the document"""

    returned_pages: int
    """Number of pages returned after applying the range filter"""

    source: Literal["ocr", "txt"]
    """Where the page text came from.

    `ocr` for PDFs (per-page OCR sidecar). `txt` for plain-text files split on
    form-feed (\f) characters.
    """

    vault_id: str

    end: Optional[int] = None
    """Echoes the end query param if provided"""

    start: Optional[int] = None
    """Echoes the start query param if provided"""


class Page(BaseModel):
    page: int
    """Page number (1-indexed)"""

    text: str
    """OCR text for this page"""


class ObjectGetPagesResponse(BaseModel):
    metadata: Metadata

    pages: List[Page]
    """Per-page OCR text in ascending page order"""
