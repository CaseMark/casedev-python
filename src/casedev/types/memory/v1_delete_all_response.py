# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["V1DeleteAllResponse"]


class V1DeleteAllResponse(BaseModel):
    deleted: Optional[int] = None
    """Number of memories deleted"""
