# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectGetSummarizeJobResponse"]


class ObjectGetSummarizeJobResponse(BaseModel):
    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """When the job completed"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the job was created"""

    error: Optional[str] = None
    """Error message (if failed)"""

    job_id: Optional[str] = FieldInfo(alias="jobId", default=None)
    """Case.dev job ID"""

    result_filename: Optional[str] = FieldInfo(alias="resultFilename", default=None)
    """Filename of the result document (if completed)"""

    result_object_id: Optional[str] = FieldInfo(alias="resultObjectId", default=None)
    """ID of the result document (if completed)"""

    source_object_id: Optional[str] = FieldInfo(alias="sourceObjectId", default=None)
    """ID of the source document"""

    status: Optional[Literal["pending", "processing", "completed", "failed"]] = None
    """Current job status"""

    workflow_type: Optional[str] = FieldInfo(alias="workflowType", default=None)
    """Type of workflow being executed"""
