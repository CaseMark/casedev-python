# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["V1ListResponse", "Result"]


class Result(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    memory: Optional[str] = None

    metadata: Optional[object] = None

    tags: Optional[object] = None

    updated_at: Optional[datetime] = None


class V1ListResponse(BaseModel):
    count: Optional[int] = None
    """Total count matching filters"""

    results: Optional[List[Result]] = None
