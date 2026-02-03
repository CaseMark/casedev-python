# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VaultDeleteResponse", "DeletedVault"]


class DeletedVault(BaseModel):
    id: Optional[str] = None

    bytes_freed: Optional[int] = FieldInfo(alias="bytesFreed", default=None)

    name: Optional[str] = None

    objects_deleted: Optional[int] = FieldInfo(alias="objectsDeleted", default=None)

    vectors_deleted: Optional[int] = FieldInfo(alias="vectorsDeleted", default=None)


class VaultDeleteResponse(BaseModel):
    deleted_vault: Optional[DeletedVault] = FieldInfo(alias="deletedVault", default=None)

    status: Optional[str] = None
    """Either 'deleted' or 'deletion_queued'"""

    success: Optional[bool] = None
