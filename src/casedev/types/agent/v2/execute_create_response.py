# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ExecuteCreateResponse"]


class ExecuteCreateResponse(BaseModel):
    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)

    message: Optional[str] = None

    provider: Optional[Literal["daytona"]] = None

    run_id: Optional[str] = FieldInfo(alias="runId", default=None)

    runtime_state: Optional[Literal["running"]] = FieldInfo(alias="runtimeState", default=None)

    status: Optional[Literal["running"]] = None
