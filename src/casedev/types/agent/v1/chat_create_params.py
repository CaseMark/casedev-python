# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ChatCreateParams"]


class ChatCreateParams(TypedDict, total=False):
    idle_timeout_ms: Annotated[Optional[int], PropertyInfo(alias="idleTimeoutMs")]
    """Idle timeout before session is eligible for snapshot/termination.

    Defaults to 15 minutes.
    """

    model: Optional[str]
    """Optional model override for the chat runtime session"""

    title: str
    """Optional human-readable session title"""

    vault_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="vaultIds")]
    """Restrict the chat session to specific vault IDs"""
