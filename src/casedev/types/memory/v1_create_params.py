# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["V1CreateParams", "Message"]


class V1CreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """Conversation messages to extract memories from"""

    category: str
    """Custom category (e.g., "fact", "preference", "deadline")"""

    extraction_prompt: str
    """Optional custom prompt for fact extraction"""

    infer: bool
    """Whether to extract facts from messages (default: true)"""

    metadata: Dict[str, object]
    """Additional metadata (not indexed)"""

    tag_1: str
    """Generic indexed filter field 1 (you decide what it means)"""

    tag_10: str
    """Generic indexed filter field 10"""

    tag_11: str
    """Generic indexed filter field 11"""

    tag_12: str
    """Generic indexed filter field 12"""

    tag_2: str
    """Generic indexed filter field 2"""

    tag_3: str
    """Generic indexed filter field 3"""

    tag_4: str
    """Generic indexed filter field 4"""

    tag_5: str
    """Generic indexed filter field 5"""

    tag_6: str
    """Generic indexed filter field 6"""

    tag_7: str
    """Generic indexed filter field 7"""

    tag_8: str
    """Generic indexed filter field 8"""

    tag_9: str
    """Generic indexed filter field 9"""


class Message(TypedDict, total=False):
    content: Required[str]
    """Message content"""

    role: Required[Literal["user", "assistant", "system"]]
    """Message role"""
