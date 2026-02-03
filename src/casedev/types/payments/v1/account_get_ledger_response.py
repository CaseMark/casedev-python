# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["AccountGetLedgerResponse"]


class AccountGetLedgerResponse(BaseModel):
    entries: Optional[List[object]] = None

    pagination: Optional[object] = None
