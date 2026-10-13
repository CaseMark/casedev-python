# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MultipartCompleteResponse", "Ingest"]


class Ingest(BaseModel):
    """Present when autoIngest was requested"""

    error: Optional[str] = None

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)

    triggered: Optional[bool] = None

    workflow_id: Optional[str] = FieldInfo(alias="workflowId", default=None)


class MultipartCompleteResponse(BaseModel):
    ingest: Optional[Ingest] = None
    """Present when autoIngest was requested"""

    success: Optional[bool] = None
