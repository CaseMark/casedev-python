# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AccountCreateResponse"]


class AccountCreateResponse(BaseModel):
    id: Optional[str] = None

    cached_available_balance: Optional[float] = FieldInfo(alias="cachedAvailableBalance", default=None)

    cached_balance: Optional[float] = FieldInfo(alias="cachedBalance", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    currency: Optional[str] = None

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    name: Optional[str] = None

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)

    type: Optional[str] = None
