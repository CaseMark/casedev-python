# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ChargeListParams"]


class ChargeListParams(TypedDict, total=False):
    destination_account_id: str

    limit: int

    offset: int

    party_id: str

    status: str
