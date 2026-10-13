# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["PartyListResponse", "Pagination"]


class Pagination(BaseModel):
    has_more: Optional[bool] = None

    limit: Optional[int] = None

    next_cursor: Optional[str] = None


class PartyListResponse(BaseModel):
    data: Optional[List[object]] = None

    pagination: Optional[Pagination] = None
