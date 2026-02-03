# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ChargeCreateParams"]


class ChargeCreateParams(TypedDict, total=False):
    amount: Required[int]
    """Amount in cents"""

    destination_account_id: Required[str]
    """Account to receive funds"""

    party_id: Required[str]
    """Party to charge"""

    currency: str

    description: str

    metadata: object

    payment_methods: SequenceNotStr[str]
