# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ObjectGetChunksResponse", "Chunk"]


class Chunk(BaseModel):
    index: int
    """Chunk index within the document"""

    page_end: Optional[int] = None
    """Last page covered by the chunk, if page mapping is available"""

    page_start: Optional[int] = None
    """First page covered by the chunk, if page mapping is available"""

    text: str
    """Full text for the chunk"""

    word_end_index: Optional[int] = None
    """Last OCR word index covered by the chunk, if available"""

    word_start_index: Optional[int] = None
    """First OCR word index covered by the chunk, if available"""


class ObjectGetChunksResponse(BaseModel):
    chunks: List[Chunk]
    """Full chunk objects for the requested range"""

    object_id: str
    """The object ID"""

    total_chunks: int
    """Total number of chunks stored for the object"""

    vault_id: str
    """The vault ID"""
