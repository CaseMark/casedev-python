# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SessionIngestEventsParams", "Frame"]


class SessionIngestEventsParams(TypedDict, total=False):
    frames: Required[Iterable[Frame]]
    """Native Linc event frames to persist for replay."""


class Frame(TypedDict, total=False):
    event: Required[Dict[str, object]]
    """Native Linc event payload."""

    seq: Required[int]
    """Monotonic native event sequence number."""

    type: Required[str]
    """Native Linc event type."""
