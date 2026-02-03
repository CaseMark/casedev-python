# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["HoldApproveParams"]


class HoldApproveParams(TypedDict, total=False):
    approver_id: str
    """ID of the approver (party or user)"""
