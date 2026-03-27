# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RunCreateResponse"]


class RunCreateResponse(BaseModel):
    id: Optional[str] = None

    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    object_ids: Optional[List[str]] = FieldInfo(alias="objectIds", default=None)

    status: Optional[Literal["queued"]] = None
