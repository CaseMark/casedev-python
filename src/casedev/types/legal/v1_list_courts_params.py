# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1ListCourtsParams"]


class V1ListCourtsParams(TypedDict, total=False):
    in_use_only: Annotated[bool, PropertyInfo(alias="inUseOnly")]
    """Only return courts currently in use by CourtListener"""

    jurisdiction: str
    """Optional CourtListener jurisdiction code filter (e.g. FD, F, S)"""

    limit: int
    """Maximum number of courts to return"""

    offset: int
    """Number of courts to skip before returning results"""

    query: str
    """Search by court name or slug (e.g. "Northern District", "nysd", "ca9")"""
