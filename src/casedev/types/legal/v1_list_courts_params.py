# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1ListCourtsParams"]


class V1ListCourtsParams(TypedDict, total=False):
    in_use_only: Annotated[bool, PropertyInfo(alias="inUseOnly")]
    """Only return courts with available docket data"""

    jurisdiction: str
    """Optional jurisdiction code filter (e.g.

    FD for Federal District, F for all Federal, S for State)
    """

    limit: int
    """Maximum number of courts to return"""

    offset: int
    """Number of courts to skip before returning results"""

    query: str
    """Search by court name or slug (e.g. "Northern District", "nysd", "ca9")"""
