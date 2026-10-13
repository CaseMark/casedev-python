# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VaultListResponse", "Pagination", "Totals", "Vault"]


class Pagination(BaseModel):
    has_more: Optional[bool] = None

    limit: Optional[int] = None

    next_cursor: Optional[str] = None


class Totals(BaseModel):
    """Present only with `include_totals=true`.

    Covers every vault matching the filters, across all pages.
    """

    total_bytes: Optional[int] = FieldInfo(alias="totalBytes", default=None)

    total_objects: Optional[int] = FieldInfo(alias="totalObjects", default=None)

    vaults: Optional[int] = None


class Vault(BaseModel):
    id: Optional[str] = None
    """Vault identifier"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Vault creation timestamp"""

    description: Optional[str] = None
    """Vault description"""

    name: Optional[str] = None
    """Vault name"""

    total_bytes: Optional[int] = FieldInfo(alias="totalBytes", default=None)
    """Total storage size in bytes"""

    total_objects: Optional[int] = FieldInfo(alias="totalObjects", default=None)
    """Number of stored documents"""


class VaultListResponse(BaseModel):
    pagination: Optional[Pagination] = None

    total: Optional[int] = None
    """Number of vaults in this response"""

    totals: Optional[Totals] = None
    """Present only with `include_totals=true`.

    Covers every vault matching the filters, across all pages.
    """

    vaults: Optional[List[Vault]] = None
