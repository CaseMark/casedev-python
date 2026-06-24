# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SessionRetrieveMessagesParams"]


class SessionRetrieveMessagesParams(TypedDict, total=False):
    after_seq: Annotated[int, PropertyInfo(alias="afterSeq")]
    """Alias for cursor. Ignored when cursor is also provided."""

    cursor: int
    """Replay messages with a source event sequence number greater than this cursor."""

    limit: int
    """Maximum number of source events to scan for completed messages."""
