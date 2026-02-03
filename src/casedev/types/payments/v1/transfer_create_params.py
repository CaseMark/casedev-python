# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransferCreateParams"]


class TransferCreateParams(TypedDict, total=False):
    amount: Required[int]
    """Amount in cents"""

    from_account_id: Required[str]

    to_account_id: Required[str]

    memo: str

    metadata: object
