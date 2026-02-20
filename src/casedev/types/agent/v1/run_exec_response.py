# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RunExecResponse"]


class RunExecResponse(BaseModel):
    id: Optional[str] = None

    message: Optional[str] = None

    status: Optional[Literal["running"]] = None

    workflow_id: Optional[str] = FieldInfo(alias="workflowId", default=None)
    """Durable workflow run ID"""
