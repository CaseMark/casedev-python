# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ConnectionListContentsResponse", "Item"]


class Item(BaseModel):
    id: Optional[str] = None

    container_id: Optional[str] = None

    kind: Optional[Literal["file"]] = None

    mime_type: Optional[str] = None

    modified_at: Optional[str] = None

    name: Optional[str] = None

    open_ref: Optional[str] = None
    """Signed reference to this file for POST /connectors/v1/fetch.

    Null for providers without single-file fetch. Pass it back exactly as received.
    """

    parent_ids: Optional[List[str]] = None

    path: Optional[str] = None
    """Path relative to the listed folder, ending in the file's name"""

    size_bytes: Optional[int] = None

    unsupported_reason: Optional[str] = None
    """Set when an import would skip the file (for example a Box note)"""


class ConnectionListContentsResponse(BaseModel):
    cursor: Optional[str] = None

    items: Optional[List[Item]] = None

    scope_ref: Optional[object] = None
    """The listed folder, as a browse_ref"""

    truncated: Optional[bool] = None
    """
    True when the listing stopped before every file was listed, at the 10,000-file
    limit or because the folder tree was too wide to page through
    """
