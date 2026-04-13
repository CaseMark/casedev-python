# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ChatStreamParams"]


class ChatStreamParams(TypedDict, total=False):
    token: str
    """Short-lived stream token from POST /agent/v2/chat/:id/stream-token.

    If provided, Bearer auth is not required.
    """

    last_event_id: Annotated[int, PropertyInfo(alias="lastEventId")]
    """Replay events after this sequence number"""
