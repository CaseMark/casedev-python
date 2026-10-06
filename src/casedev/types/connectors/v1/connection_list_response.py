# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ConnectionListResponse", "Capabilities", "Pagination", "Provider"]


class Capabilities(BaseModel):
    google_drive_folder_mirroring: Optional[bool] = None


class Pagination(BaseModel):
    has_more: Optional[bool] = None

    limit: Optional[int] = None

    next_cursor: Optional[str] = None


class Provider(BaseModel):
    id: Optional[str] = None

    resource_types: Optional[List[str]] = None

    scope_tier: Optional[str] = None

    supports_export: Optional[bool] = None


class ConnectionListResponse(BaseModel):
    capabilities: Optional[Capabilities] = None

    connections: Optional[List[object]] = None

    cursor: Optional[str] = None
    """Mirror of `pagination.next_cursor`. Prefer `pagination`."""

    pagination: Optional[Pagination] = None

    providers: Optional[List[Provider]] = None
    """Available import providers and their adapter-declared capabilities."""
