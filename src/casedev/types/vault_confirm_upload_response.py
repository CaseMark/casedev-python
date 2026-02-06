# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VaultConfirmUploadResponse"]


class VaultConfirmUploadResponse(BaseModel):
    already_confirmed: Optional[bool] = FieldInfo(alias="alreadyConfirmed", default=None)

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)

    status: Optional[Literal["completed", "failed"]] = None

    vault_id: Optional[str] = FieldInfo(alias="vaultId", default=None)
