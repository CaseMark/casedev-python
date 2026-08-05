# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ConnectionCreateResponse"]


class ConnectionCreateResponse(BaseModel):
    connect_url: Optional[str] = None

    connection_id: Optional[str] = None

    expires_at: Optional[str] = None
