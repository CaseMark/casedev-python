# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LedgerGetParams"]


class LedgerGetParams(TypedDict, total=False):
    account_id: str
    """Filter by account"""

    limit: int

    offset: int

    transaction_id: str
    """Filter by transaction"""
