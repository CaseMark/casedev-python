# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor (agent ID from previous page).

    Returns agents created before this agent.
    """

    limit: int
    """Maximum number of agents to return (default 50, max 250)"""
