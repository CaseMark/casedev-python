# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["V1SearchResponse", "Result", "ResultTags"]


class ResultTags(BaseModel):
    """Tag values for this memory"""

    tag_1: Optional[str] = None

    tag_10: Optional[str] = None

    tag_11: Optional[str] = None

    tag_12: Optional[str] = None

    tag_2: Optional[str] = None

    tag_3: Optional[str] = None

    tag_4: Optional[str] = None

    tag_5: Optional[str] = None

    tag_6: Optional[str] = None

    tag_7: Optional[str] = None

    tag_8: Optional[str] = None

    tag_9: Optional[str] = None


class Result(BaseModel):
    id: Optional[str] = None
    """Memory ID"""

    created_at: Optional[datetime] = None

    memory: Optional[str] = None
    """Memory content"""

    metadata: Optional[object] = None
    """Additional metadata"""

    score: Optional[float] = None
    """Similarity score (0-1)"""

    tags: Optional[ResultTags] = None
    """Tag values for this memory"""

    updated_at: Optional[datetime] = None


class V1SearchResponse(BaseModel):
    results: Optional[List[Result]] = None
