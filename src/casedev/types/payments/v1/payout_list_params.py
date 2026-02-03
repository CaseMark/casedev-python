# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PayoutListParams"]


class PayoutListParams(TypedDict, total=False):
    from_account_id: str

    limit: int

    offset: int

    party_id: str

    status: Literal["pending", "processing", "completed", "failed", "cancelled"]
