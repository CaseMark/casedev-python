# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ObjectListParams"]


class ObjectListParams(TypedDict, total=False):
    cursor: str
    """Opaque continuation cursor from `pagination.next_cursor` of the previous page.

    Must be replayed with the same API key scope and the same `query`, `file_origin`
    and `includeUnconfirmed` values that produced it.
    """

    file_origin: str
    """JSON-encoded provenance object used as a partial match.

    For example, {"provider":"clio"} returns objects whose file_origin contains that
    value.
    """

    include_totals: bool
    """
    When `true`, adds `totals` covering every object matching the filters, not just
    this page. Request it once per filter change rather than on every page.
    """

    include_unconfirmed: Annotated[bool, PropertyInfo(alias="includeUnconfirmed")]
    """
    Include placeholders for uploads that were never completed (awaiting_upload) or
    were cancelled (aborted). Excluded by default.
    """

    limit: int
    """Objects per page (1-200).

    Omit to receive every object. Supplying a cursor without a limit uses 50.
    """

    query: str
    """Case-insensitive substring match on the filename."""
