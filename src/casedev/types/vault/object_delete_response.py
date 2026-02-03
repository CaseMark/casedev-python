# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectDeleteResponse", "DeletedObject"]


class DeletedObject(BaseModel):
    id: Optional[str] = None
    """Deleted object ID"""

    filename: Optional[str] = None
    """Original filename"""

    size_bytes: Optional[int] = FieldInfo(alias="sizeBytes", default=None)
    """Size of deleted file in bytes"""

    vectors_deleted: Optional[int] = FieldInfo(alias="vectorsDeleted", default=None)
    """Number of vectors deleted"""


class ObjectDeleteResponse(BaseModel):
    deleted_object: Optional[DeletedObject] = FieldInfo(alias="deletedObject", default=None)

    success: Optional[bool] = None
