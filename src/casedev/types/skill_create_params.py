# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SkillCreateParams"]


class SkillCreateParams(TypedDict, total=False):
    content: Required[str]
    """Full skill content in markdown"""

    name: Required[str]
    """Skill name"""

    metadata: object
    """Arbitrary metadata (author, license, etc.)"""

    slug: str
    """URL-safe slug. Auto-generated from name if omitted."""

    summary: str
    """Brief description (1-2 sentences)"""

    tags: SequenceNotStr[str]
    """Tags for categorization and search boosting"""
