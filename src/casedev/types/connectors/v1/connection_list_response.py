# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ConnectionListResponse", "Capabilities"]


class Capabilities(BaseModel):
    google_drive_folder_mirroring: Optional[bool] = None


class ConnectionListResponse(BaseModel):
    capabilities: Optional[Capabilities] = None

    connections: Optional[List[object]] = None

    cursor: Optional[str] = None
