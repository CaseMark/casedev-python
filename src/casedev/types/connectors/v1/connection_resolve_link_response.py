# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ConnectionResolveLinkResponse"]


class ConnectionResolveLinkResponse(BaseModel):
    id: Optional[str] = None

    browse_ref: Optional[object] = None
    """Pass these fields to browse to open the folder"""

    container_id: Optional[str] = None

    description: Optional[str] = None

    import_ref: Optional[object] = None

    kind: Optional[Literal["folder"]] = None

    mime_type: Optional[str] = None

    modified_at: Optional[str] = None

    name: Optional[str] = None

    open_ref: Optional[str] = None
    """Always null for folders"""

    parent_ids: Optional[List[str]] = None

    path: Optional[str] = None
    """Display path in the account, when the provider reports it"""

    size_bytes: Optional[int] = None
