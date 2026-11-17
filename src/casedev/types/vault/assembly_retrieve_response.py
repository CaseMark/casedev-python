# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AssemblyRetrieveResponse", "Error", "Timings", "Volume"]


class Error(BaseModel):
    code: Optional[str] = None

    message: Optional[str] = None

    retryable: Optional[bool] = None

    source_index: Optional[int] = FieldInfo(alias="sourceIndex", default=None)

    stage: Optional[str] = None

    volume_index: Optional[int] = FieldInfo(alias="volumeIndex", default=None)


class Timings(BaseModel):
    accepted_at: Optional[datetime] = FieldInfo(alias="acceptedAt", default=None)

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    worker_elapsed_ms: Optional[int] = FieldInfo(alias="workerElapsedMs", default=None)

    worker_started_at: Optional[datetime] = FieldInfo(alias="workerStartedAt", default=None)


class Volume(BaseModel):
    bates_end: Optional[str] = FieldInfo(alias="batesEnd", default=None)

    bates_start: Optional[str] = FieldInfo(alias="batesStart", default=None)

    filename: Optional[str] = None

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)

    page_count: Optional[int] = FieldInfo(alias="pageCount", default=None)

    sha256: Optional[str] = None

    size_bytes: Optional[int] = FieldInfo(alias="sizeBytes", default=None)


class AssemblyRetrieveResponse(BaseModel):
    id: Optional[str] = None

    client_reference: Optional[str] = FieldInfo(alias="clientReference", default=None)

    error: Optional[Error] = None

    status: Optional[Literal["queued", "processing", "completed", "failed", "cancelled"]] = None

    timings: Optional[Timings] = None

    vault_id: Optional[str] = FieldInfo(alias="vaultId", default=None)

    volumes: Optional[List[Volume]] = None
