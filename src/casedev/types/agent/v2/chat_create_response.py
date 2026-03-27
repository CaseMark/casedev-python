# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ChatCreateResponse"]


class ChatCreateResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    idle_timeout_ms: Optional[int] = FieldInfo(alias="idleTimeoutMs", default=None)

    provider: Optional[Literal["daytona"]] = None

    runtime_state: Optional[str] = FieldInfo(alias="runtimeState", default=None)

    status: Optional[str] = None
