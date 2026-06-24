# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectSummarizeResponse"]


class ObjectSummarizeResponse(BaseModel):
    casemark_workflow_id: Optional[str] = FieldInfo(alias="casemarkWorkflowId", default=None)
    """CaseMark workflow ID"""

    job_id: Optional[str] = FieldInfo(alias="jobId", default=None)
    """Case.dev job ID for tracking"""

    status: Optional[Literal["pending", "processing", "completed", "failed"]] = None
    """Current job status"""

    status_url: Optional[str] = FieldInfo(alias="statusUrl", default=None)
    """URL to check job status"""

    workflow_type: Optional[str] = FieldInfo(alias="workflowType", default=None)
    """Type of workflow being executed"""
