# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RunCreateParams"]


class RunCreateParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]
    """ID of the agent to run"""

    prompt: Required[str]
    """Task prompt for the agent"""

    guidance: Optional[str]
    """Additional guidance for this run"""

    model: Optional[str]
    """Override the agent default model for this run"""
