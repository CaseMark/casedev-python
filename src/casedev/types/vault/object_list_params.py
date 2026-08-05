# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ObjectListParams"]


class ObjectListParams(TypedDict, total=False):
    include_unconfirmed: Annotated[bool, PropertyInfo(alias="includeUnconfirmed")]
    """
    Include placeholders for uploads that were never completed (awaiting_upload) or
    were cancelled (aborted). Excluded by default.
    """
