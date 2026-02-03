# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["V1RetrieveResponse"]


class V1RetrieveResponse(BaseModel):
    id: Optional[str] = None
    """Memory ID"""

    created_at: Optional[datetime] = None

    memory: Optional[str] = None
    """Memory content"""

    metadata: Optional[object] = None
    """Memory metadata"""

    updated_at: Optional[datetime] = None
