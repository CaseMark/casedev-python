# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RunListResponse", "Run"]


class Run(BaseModel):
    id: Optional[str] = None

    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    model: Optional[str] = None

    prompt: Optional[str] = None
    """Truncated to first 200 characters"""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    status: Optional[Literal["queued", "running", "completed", "failed", "cancelled"]] = None


class RunListResponse(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Pass as cursor to fetch the next page"""

    runs: Optional[List[Run]] = None
