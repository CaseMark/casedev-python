# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["InstanceListResponse", "Instance"]


class Instance(BaseModel):
    id: Optional[str] = None

    auto_shutdown_minutes: Optional[int] = FieldInfo(alias="autoShutdownMinutes", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    gpu: Optional[str] = None

    instance_type: Optional[str] = FieldInfo(alias="instanceType", default=None)

    ip: Optional[str] = None

    name: Optional[str] = None

    price_per_hour: Optional[str] = FieldInfo(alias="pricePerHour", default=None)

    region: Optional[str] = None

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    status: Optional[Literal["booting", "running", "stopping", "stopped", "terminated", "failed"]] = None

    total_cost: Optional[str] = FieldInfo(alias="totalCost", default=None)

    total_runtime_seconds: Optional[int] = FieldInfo(alias="totalRuntimeSeconds", default=None)


class InstanceListResponse(BaseModel):
    count: Optional[int] = None

    instances: Optional[List[Instance]] = None
