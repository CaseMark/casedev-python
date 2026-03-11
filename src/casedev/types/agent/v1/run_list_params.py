# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    agent_id: Annotated[str, PropertyInfo(alias="agentId")]
    """Filter by agent ID"""

    cursor: str
    """Pagination cursor (run ID from previous page).

    Returns runs created before this run.
    """

    limit: int
    """Maximum number of runs to return (default 50, max 250)"""

    status: Literal["queued", "running", "completed", "failed", "cancelled"]
    """Filter by run status"""
