# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ConnectionBrowseResponse", "Item"]


class Item(BaseModel):
    id: Optional[str] = None

    browse_ref: Optional[object] = None

    container_id: Optional[str] = None

    kind: Optional[Literal["my_drive", "shared_drive", "matter", "site", "document_library", "folder", "file"]] = None

    mime_type: Optional[str] = None

    modified_at: Optional[str] = None

    name: Optional[str] = None

    parent_ids: Optional[List[str]] = None

    path: Optional[str] = None

    size_bytes: Optional[int] = None


class ConnectionBrowseResponse(BaseModel):
    cursor: Optional[str] = None

    items: Optional[List[Item]] = None
