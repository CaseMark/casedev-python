# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RunWatchParams"]


class RunWatchParams(TypedDict, total=False):
    callback_url: Required[Annotated[str, PropertyInfo(alias="callbackUrl")]]
    """HTTPS URL to receive completion callback"""
