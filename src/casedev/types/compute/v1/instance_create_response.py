# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["InstanceCreateResponse"]


class InstanceCreateResponse(BaseModel):
    id: Optional[str] = None

    auto_shutdown_minutes: Optional[int] = FieldInfo(alias="autoShutdownMinutes", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    gpu: Optional[str] = None

    instance_type: Optional[str] = FieldInfo(alias="instanceType", default=None)

    message: Optional[str] = None

    name: Optional[str] = None

    price_per_hour: Optional[str] = FieldInfo(alias="pricePerHour", default=None)

    region: Optional[str] = None

    specs: Optional[object] = None

    status: Optional[str] = None

    vaults: Optional[List[object]] = None
