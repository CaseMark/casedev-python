# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["MemoryCreateResponse", "Entry"]


class Entry(BaseModel):
    id: Optional[str] = None

    content: Optional[str] = None

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    source: Optional[str] = None

    tags: Optional[List[str]] = None

    type: Optional[str] = None

    updated_at: Optional[datetime] = None


class MemoryCreateResponse(BaseModel):
    entry: Optional[Entry] = None
