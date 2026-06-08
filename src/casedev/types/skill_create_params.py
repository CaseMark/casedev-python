# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SkillCreateParams", "File"]


class SkillCreateParams(TypedDict, total=False):
    content: Required[str]
    """Full skill content in markdown"""

    name: Required[str]
    """Skill name"""

    files: Iterable[File]
    """
    Optional bundled companion files installed alongside the skill as <slug>/<path>
    in sandbox skill directories.
    """

    metadata: object
    """Arbitrary metadata (author, license, etc.)"""

    slug: str
    """URL-safe slug. Auto-generated from name if omitted."""

    summary: str
    """Brief description (1-2 sentences)"""

    tags: SequenceNotStr[str]
    """Tags for categorization and search boosting"""


class File(TypedDict, total=False):
    content: Required[str]

    path: Required[str]
    """Relative path inside the skill directory.

    SKILL.md is reserved for the root skill content.
    """

    content_type: Annotated[str, PropertyInfo(alias="contentType")]

    metadata: object

    name: str

    summary: str

    tags: SequenceNotStr[str]
