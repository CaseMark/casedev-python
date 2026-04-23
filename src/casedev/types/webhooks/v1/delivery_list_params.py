# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DeliveryListParams"]


class DeliveryListParams(TypedDict, total=False):
    endpoint_id: str

    limit: int

    status: Literal["pending", "delivered", "failed"]
