# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ExecuteCreateResponse", "Logs"]


class Logs(BaseModel):
    linc: Optional[str] = None

    runner: Optional[str] = None


class ExecuteCreateResponse(BaseModel):
    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)

    error: Optional[str] = None

    logs: Optional[Logs] = None

    message: Optional[str] = None

    output: Optional[str] = None

    provider: Optional[Literal["daytona", "vercel"]] = None

    run_id: Optional[str] = FieldInfo(alias="runId", default=None)

    runtime_id: Optional[str] = FieldInfo(alias="runtimeId", default=None)

    runtime_state: Optional[Literal["running", "ended", "error"]] = FieldInfo(alias="runtimeState", default=None)

    status: Optional[Literal["running", "completed", "failed"]] = None

    usage: Optional[object] = None
