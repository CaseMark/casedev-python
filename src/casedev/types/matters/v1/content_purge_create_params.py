# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ContentPurgeCreateParams"]


class ContentPurgeCreateParams(TypedDict, total=False):
    request_id: Required[str]
    """Stable caller idempotency ID; cannot be reused with different targets."""

    object_ids: SequenceNotStr[str]

    session_ids: SequenceNotStr[str]

    transcription_ids: SequenceNotStr[str]

    work_item_ids: SequenceNotStr[str]
