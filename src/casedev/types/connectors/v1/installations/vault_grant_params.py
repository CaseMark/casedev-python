# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VaultGrantParams"]


class VaultGrantParams(TypedDict, total=False):
    id: Required[str]

    can_manage: bool

    can_read: bool

    can_write: bool

    relationship: Literal["owned", "shared"]

    source: Literal["provisioning", "lazy_reconcile", "explicit_share"]
