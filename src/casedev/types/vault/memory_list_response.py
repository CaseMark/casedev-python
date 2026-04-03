# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["MemoryListResponse", "Entry", "Meta"]


class Entry(BaseModel):
    id: Optional[str] = None

    content: Optional[str] = None

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    source: Optional[str] = None

    tags: Optional[List[str]] = None

    type: Optional[str] = None

    updated_at: Optional[datetime] = None


class Meta(BaseModel):
    chars: Optional[int] = None

    count: Optional[int] = None

    max_chars: Optional[int] = None

    updated_at: Optional[datetime] = None


class MemoryListResponse(BaseModel):
    entries: Optional[List[Entry]] = None

    meta: Optional[Meta] = None
