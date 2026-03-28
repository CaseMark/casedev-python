# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WorkItemListParams"]


class WorkItemListParams(TypedDict, total=False):
    assignee_id: str

    status: str
