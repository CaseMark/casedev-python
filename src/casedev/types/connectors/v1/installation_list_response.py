# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["InstallationListResponse", "Pagination"]


class Pagination(BaseModel):
    has_more: Optional[bool] = None

    limit: Optional[int] = None

    next_cursor: Optional[str] = None


class InstallationListResponse(BaseModel):
    installations: Optional[List[object]] = None

    pagination: Optional[Pagination] = None
