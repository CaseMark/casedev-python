# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ExecuteCreateResponse"]


class ExecuteCreateResponse(BaseModel):
    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)
    """Ephemeral agent ID (auto-created).

    This agent is soft-deleted when the run completes and should not be stored for
    reuse.
    """

    message: Optional[str] = None

    run_id: Optional[str] = FieldInfo(alias="runId", default=None)
    """Run ID — poll /agent/v1/run/:id/status"""

    status: Optional[Literal["running"]] = None
