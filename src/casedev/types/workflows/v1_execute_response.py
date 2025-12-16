# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1ExecuteResponse"]


class V1ExecuteResponse(BaseModel):
    duration: Optional[int] = None

    execution_arn: Optional[str] = FieldInfo(alias="executionArn", default=None)

    execution_id: Optional[str] = FieldInfo(alias="executionId", default=None)

    mode: Optional[Literal["fire-and-forget", "callback", "sync"]] = None

    output: Optional[object] = None

    status: Optional[Literal["running", "completed", "failed"]] = None
