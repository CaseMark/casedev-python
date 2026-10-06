# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WorkItemListParams"]


class WorkItemListParams(TypedDict, total=False):
    assignee_id: str

    cursor: str
    """Opaque continuation cursor from `pagination.next_cursor` of the previous page.

    Must be replayed with the same filters that produced it.
    """

    limit: int
    """Work items per page (1-200).

    Omit to receive every work item. Supplying a cursor without a limit uses 50.
    """

    status: str
