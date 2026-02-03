# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1SimilarParams"]


class V1SimilarParams(TypedDict, total=False):
    url: Required[str]
    """URL of a legal document to find similar sources for"""

    jurisdiction: str
    """Optional jurisdiction ID to filter results"""

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results 1-25 (default: 10)"""

    start_published_date: Annotated[Union[str, date], PropertyInfo(alias="startPublishedDate", format="iso8601")]
    """Optional ISO date to find only newer documents (e.g., "2020-01-01")"""
