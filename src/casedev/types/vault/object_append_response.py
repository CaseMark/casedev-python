# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectAppendResponse"]


class ObjectAppendResponse(BaseModel):
    id: Optional[str] = None

    bates: Optional[object] = None

    checksum: Optional[str] = None

    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    download_url: Optional[str] = FieldInfo(alias="downloadUrl", default=None)

    expires_in: Optional[int] = FieldInfo(alias="expiresIn", default=None)

    filename: Optional[str] = None

    ingestion_status: Optional[str] = FieldInfo(alias="ingestionStatus", default=None)

    metadata: Optional[object] = None

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)

    page_count: Optional[int] = FieldInfo(alias="pageCount", default=None)

    size_bytes: Optional[int] = FieldInfo(alias="sizeBytes", default=None)

    vault_id: Optional[str] = FieldInfo(alias="vaultId", default=None)
