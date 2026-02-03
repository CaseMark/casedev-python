# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VaultDeleteParams"]


class VaultDeleteParams(TypedDict, total=False):
    async_: Annotated[bool, PropertyInfo(alias="async")]
    """
    If true and vault has many objects, queue deletion in background and return
    immediately
    """
