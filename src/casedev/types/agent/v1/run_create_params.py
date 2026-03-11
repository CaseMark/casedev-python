# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["RunCreateParams"]


class RunCreateParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]
    """ID of the agent to run"""

    prompt: Required[str]
    """Task prompt for the agent"""

    callback_url: Annotated[Optional[str], PropertyInfo(alias="callbackUrl")]
    """HTTPS callback URL to receive a notification when the run completes.

    Registered atomically with the run — eliminates the race condition of calling
    /watch after /exec. Additional watchers can still be added via POST
    /run/:id/watch.
    """

    guidance: Optional[str]
    """Additional guidance for this run"""

    model: Optional[str]
    """Override the agent default model for this run"""

    object_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="objectIds")]
    """Scope this run to specific vault object IDs.

    The agent will only be able to access these objects during execution.
    """
