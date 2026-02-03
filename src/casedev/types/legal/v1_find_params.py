# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1FindParams"]


class V1FindParams(TypedDict, total=False):
    query: Required[str]
    """Search query (e.g., "fair use copyright", "Miranda rights")"""

    jurisdiction: str
    """
    Optional jurisdiction ID from resolveJurisdiction (e.g., "california",
    "us-federal")
    """

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results 1-25 (default: 10)"""
