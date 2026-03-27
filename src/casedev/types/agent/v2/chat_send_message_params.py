# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatSendMessageParams", "Part"]


class ChatSendMessageParams(TypedDict, total=False):
    parts: Iterable[Part]
    """Message content parts.

    Currently only "text" type is supported. Additional types (e.g. file, image) may
    be added in future versions.
    """


class Part(TypedDict, total=False):
    text: Required[str]
    """The message text content"""

    type: Required[Literal["text"]]
    """Part type. Currently only "text" is supported."""
