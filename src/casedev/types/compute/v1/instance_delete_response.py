# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["InstanceDeleteResponse"]


class InstanceDeleteResponse(BaseModel):
    id: Optional[str] = None

    message: Optional[str] = None

    name: Optional[str] = None

    status: Optional[str] = None

    total_cost: Optional[str] = FieldInfo(alias="totalCost", default=None)

    total_runtime_seconds: Optional[int] = FieldInfo(alias="totalRuntimeSeconds", default=None)
