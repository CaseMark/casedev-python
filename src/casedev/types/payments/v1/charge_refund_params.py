# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ChargeRefundParams"]


class ChargeRefundParams(TypedDict, total=False):
    amount: int
    """Amount to refund in cents. If not provided, full refund."""

    reason: str
    """Reason for refund"""
