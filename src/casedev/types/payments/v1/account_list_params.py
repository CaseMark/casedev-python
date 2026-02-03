# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    limit: int
    """Max results to return"""

    matter_id: str
    """Filter by matter ID"""

    offset: int
    """Offset for pagination"""

    parent_account_id: str
    """Filter by parent account"""

    type: str
    """Filter by account type"""
