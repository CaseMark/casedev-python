# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MultipartInitResponse"]


class MultipartInitResponse(BaseModel):
    next_step: Optional[str] = None

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)

    part_count: Optional[int] = FieldInfo(alias="partCount", default=None)

    part_size_bytes: Optional[int] = FieldInfo(alias="partSizeBytes", default=None)

    s3_key: Optional[str] = FieldInfo(alias="s3Key", default=None)

    upload_id: Optional[str] = FieldInfo(alias="uploadId", default=None)
