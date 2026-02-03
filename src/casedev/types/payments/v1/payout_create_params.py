# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PayoutCreateParams"]


class PayoutCreateParams(TypedDict, total=False):
    amount: Required[int]
    """Amount in cents"""

    destination_type: Required[Literal["bank_account", "card"]]

    from_account_id: Required[str]
    """Source account"""

    currency: str

    memo: str

    metadata: object

    party_id: str
    """Recipient party (optional)"""
