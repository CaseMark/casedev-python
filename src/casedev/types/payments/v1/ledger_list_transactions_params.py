# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LedgerListTransactionsParams"]


class LedgerListTransactionsParams(TypedDict, total=False):
    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    limit: int

    offset: int

    reference_id: str
    """Filter by reference ID"""

    reference_type: str
    """Filter by reference type (transfer, charge, payout, etc.)"""

    start_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
