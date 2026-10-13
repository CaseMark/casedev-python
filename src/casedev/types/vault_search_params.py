# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["VaultSearchParams", "Filters", "FiltersPageRange"]


class VaultSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query or question to find relevant documents"""

    filters: Filters
    """Filters to narrow search results to specific documents"""

    method: Literal["hybrid", "fast", "vector"]
    """
    Search method: 'hybrid' for combined vector + keyword ranking (default), 'fast'
    for quick vector similarity search, 'vector' for a simple document listing
    fallback
    """

    top_k: Annotated[int, PropertyInfo(alias="topK")]
    """Maximum number of results to return.

    Hybrid search supports 1 to 50; other methods may support up to 100.
    """


class FiltersPageRange(TypedDict, total=False):
    """
    Restrict vector-backed retrieval to chunks wholly contained in this inclusive PDF page range. Supported by vector, hybrid, and fast methods.
    """

    start: Required[int]

    end: int


class Filters(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """Filters to narrow search results to specific documents"""

    object_id: Union[str, SequenceNotStr[str]]
    """Filter to specific document(s) by object ID.

    Accepts a single ID or array of IDs.
    """

    page_range: FiltersPageRange
    """
    Restrict vector-backed retrieval to chunks wholly contained in this inclusive
    PDF page range. Supported by vector, hybrid, and fast methods.
    """
