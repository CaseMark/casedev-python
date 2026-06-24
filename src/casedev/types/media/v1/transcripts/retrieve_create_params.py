# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RetrieveCreateParams", "Transcript"]


class RetrieveCreateParams(TypedDict, total=False):
    object_id: Required[str]
    """Object ID for either the source audio/video file or transcript artifact."""

    vault_id: Required[str]
    """Vault ID containing the source media or transcript object."""

    transcript: Transcript
    """Alternative nested transcript object reference."""


class Transcript(TypedDict, total=False):
    """Alternative nested transcript object reference."""

    object_id: str

    vault_id: str
