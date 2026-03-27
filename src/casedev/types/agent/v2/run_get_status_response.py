# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RunGetStatusResponse"]


class RunGetStatusResponse(BaseModel):
    id: Optional[str] = None

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    duration_ms: Optional[int] = FieldInfo(alias="durationMs", default=None)

    provider: Optional[str] = None

    runtime_id: Optional[str] = FieldInfo(alias="runtimeId", default=None)

    runtime_state: Optional[str] = FieldInfo(alias="runtimeState", default=None)

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    status: Optional[Literal["queued", "running", "completed", "failed", "cancelled"]] = None
