# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V1ListParams"]


class V1ListParams(TypedDict, total=False):
    cursor: str
    """Opaque continuation cursor from `pagination.next_cursor` of the previous page.

    Must be replayed with the same filters that produced it.
    """

    limit: int
    """Matters per page (1-200).

    Omit to receive every matter. Supplying a cursor without a limit uses 50.
    """

    matter_type: str

    practice_area: str

    query: str

    status: str
