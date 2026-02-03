# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["V1ResearchParams"]


class V1ResearchParams(TypedDict, total=False):
    query: Required[str]
    """Primary search query"""

    additional_queries: Annotated[SequenceNotStr[str], PropertyInfo(alias="additionalQueries")]
    """
    Additional query variations to search (e.g., different phrasings of the legal
    issue)
    """

    jurisdiction: str
    """Optional jurisdiction ID from resolveJurisdiction"""

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results 1-25 (default: 10)"""
