# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AssemblyRetrieveResponse", "Cogs", "Error", "Timings", "Volume"]


class Cogs(BaseModel):
    """What the assembly cost Case.dev, once it is completed or failed.

    Internal COGS, not a price.
    """

    compute_micros: Optional[int] = FieldInfo(alias="computeMicros", default=None)

    cpu: Optional[float] = None

    memory_mib: Optional[int] = FieldInfo(alias="memoryMib", default=None)

    output_bytes: Optional[int] = FieldInfo(alias="outputBytes", default=None)

    rate_version: Optional[str] = FieldInfo(alias="rateVersion", default=None)

    source_bytes: Optional[int] = FieldInfo(alias="sourceBytes", default=None)

    transfer_micros: Optional[int] = FieldInfo(alias="transferMicros", default=None)

    worker_seconds: Optional[float] = FieldInfo(alias="workerSeconds", default=None)


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

    cogs: Optional[Cogs] = None
    """What the assembly cost Case.dev, once it is completed or failed.

    Internal COGS, not a price.
    """

    error: Optional[Error] = None

    status: Optional[Literal["queued", "processing", "completed", "failed", "cancelled"]] = None

    timings: Optional[Timings] = None

    vault_id: Optional[str] = FieldInfo(alias="vaultId", default=None)

    volumes: Optional[List[Volume]] = None
