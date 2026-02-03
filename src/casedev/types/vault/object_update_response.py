# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectUpdateResponse"]


class ObjectUpdateResponse(BaseModel):
    id: Optional[str] = None
    """Object ID"""

    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)
    """MIME type"""

    filename: Optional[str] = None
    """Updated filename"""

    ingestion_status: Optional[str] = FieldInfo(alias="ingestionStatus", default=None)
    """Processing status"""

    metadata: Optional[object] = None
    """Full metadata object"""

    path: Optional[str] = None
    """Folder path for hierarchy preservation"""

    size_bytes: Optional[int] = FieldInfo(alias="sizeBytes", default=None)
    """File size in bytes"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Last update timestamp"""

    vault_id: Optional[str] = FieldInfo(alias="vaultId", default=None)
    """Vault ID"""
