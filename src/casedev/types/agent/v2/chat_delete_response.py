# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ChatDeleteResponse"]


class ChatDeleteResponse(BaseModel):
    id: Optional[str] = None

    cost: Optional[float] = None

    provider: Optional[str] = None

    runtime_id: Optional[str] = FieldInfo(alias="runtimeId", default=None)

    runtime_ms: Optional[int] = FieldInfo(alias="runtimeMs", default=None)

    status: Optional[str] = None
