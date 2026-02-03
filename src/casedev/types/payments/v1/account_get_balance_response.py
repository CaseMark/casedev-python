# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AccountGetBalanceResponse"]


class AccountGetBalanceResponse(BaseModel):
    account_id: Optional[str] = FieldInfo(alias="accountId", default=None)

    available_balance: Optional[float] = FieldInfo(alias="availableBalance", default=None)
    """Balance minus holds"""

    balance: Optional[float] = None
    """Total balance in cents"""

    currency: Optional[str] = None

    held_amount: Optional[float] = FieldInfo(alias="heldAmount", default=None)
    """Amount held by active holds"""

    pending_charges: Optional[float] = FieldInfo(alias="pendingCharges", default=None)
    """Pending incoming payments"""
