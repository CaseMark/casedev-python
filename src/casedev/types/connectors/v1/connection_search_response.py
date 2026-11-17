# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ConnectionSearchResponse", "Item"]


class Item(BaseModel):
    id: Optional[str] = None

    browse_ref: Optional[object] = None
    """Reference for GET /connectors/v1/connections/{id}/browse that opens this folder.

    Null for files.
    """

    container_id: Optional[str] = None

    kind: Optional[Literal["file", "folder"]] = None

    mime_type: Optional[str] = None

    modified_at: Optional[str] = None

    name: Optional[str] = None

    open_ref: Optional[str] = None
    """Signed reference to this file for POST /connectors/v1/fetch.

    Null for providers without single-file fetch. Pass it back exactly as received.
    """

    parent_ids: Optional[List[str]] = None

    path: Optional[str] = None

    size_bytes: Optional[int] = None

    unsupported_reason: Optional[str] = None
    """Set when the file cannot be imported (for example a Box note)"""


class ConnectionSearchResponse(BaseModel):
    cursor: Optional[str] = None

    folder_scope_recursive: Optional[bool] = None
    """False when a folder scope covers its direct children only"""

    full_text: Optional[bool] = None
    """Whether the provider matches file contents, not only names.

    Always false for kind=folder.
    """

    items: Optional[List[Item]] = None

    scope: Optional[Literal["account", "folder"]] = None

    scope_ref: Optional[object] = None
