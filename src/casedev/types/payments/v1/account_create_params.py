# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountCreateParams"]


class AccountCreateParams(TypedDict, total=False):
    name: Required[str]
    """Account name"""

    type: Required[Literal["trust", "operating", "escrow", "reserve", "client", "sub"]]
    """Account type"""

    currency: str
    """Currency code"""

    matter_id: str
    """Associated matter ID"""

    metadata: object
    """Additional metadata"""

    parent_account_id: str
    """Parent account ID for sub-accounts"""
