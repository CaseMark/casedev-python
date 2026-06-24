# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["SessionRetrieveEventsParams"]


class SessionRetrieveEventsParams(TypedDict, total=False):
    after_seq: Annotated[int, PropertyInfo(alias="afterSeq")]
    """Alias for cursor. Ignored when cursor is also provided."""

    cursor: int
    """Replay events with a sequence number greater than this cursor."""

    exclude_event_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeEventTypes")]
    """Comma-separated Linc event types to omit from replay."""

    limit: int
    """Maximum number of events to return."""
