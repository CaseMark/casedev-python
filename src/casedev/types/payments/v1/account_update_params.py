# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountUpdateParams"]


class AccountUpdateParams(TypedDict, total=False):
    is_active: bool

    metadata: object

    name: str
