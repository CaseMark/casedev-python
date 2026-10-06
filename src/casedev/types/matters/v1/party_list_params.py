# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PartyListParams"]


class PartyListParams(TypedDict, total=False):
    cursor: str
    """Opaque continuation cursor from `pagination.next_cursor` of the previous page.

    Must be replayed with the same filters that produced it.
    """

    email: str

    limit: int
    """Parties per page (1-200).

    Omit to receive every party. Supplying a cursor without a limit uses 50.
    """

    query: str

    type: Literal["person", "organization"]
