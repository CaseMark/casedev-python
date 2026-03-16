# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SkillUpdateResponse"]


class SkillUpdateResponse(BaseModel):
    content: Optional[str] = None

    metadata: Optional[object] = None

    name: Optional[str] = None

    slug: Optional[str] = None

    summary: Optional[str] = None

    tags: Optional[List[str]] = None

    updated_at: Optional[datetime] = None

    version: Optional[int] = None
