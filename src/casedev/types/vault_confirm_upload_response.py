# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VaultConfirmUploadResponse", "Ingest"]


class Ingest(BaseModel):
    """Present when autoIngest was requested on a successful confirmation"""

    error: Optional[str] = None

    triggered: Optional[bool] = None

    workflow_id: Optional[str] = FieldInfo(alias="workflowId", default=None)


class VaultConfirmUploadResponse(BaseModel):
    already_confirmed: Optional[bool] = FieldInfo(alias="alreadyConfirmed", default=None)

    ingest: Optional[Ingest] = None
    """Present when autoIngest was requested on a successful confirmation"""

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)

    status: Optional[Literal["completed", "failed"]] = None

    vault_id: Optional[str] = FieldInfo(alias="vaultId", default=None)
