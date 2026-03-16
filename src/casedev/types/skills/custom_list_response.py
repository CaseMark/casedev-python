# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CustomListResponse", "Skill"]


class Skill(BaseModel):
    created_at: Optional[datetime] = None

    metadata: Optional[object] = None

    name: Optional[str] = None

    slug: Optional[str] = None

    summary: Optional[str] = None

    tags: Optional[List[str]] = None

    updated_at: Optional[datetime] = None

    version: Optional[int] = None


class CustomListResponse(BaseModel):
    has_more: Optional[bool] = None

    next_cursor: Optional[str] = None

    skills: Optional[List[Skill]] = None
