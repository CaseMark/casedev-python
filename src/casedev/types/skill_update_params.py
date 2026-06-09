# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SkillUpdateParams", "File"]


class SkillUpdateParams(TypedDict, total=False):
    content: str

    files: Optional[Iterable[File]]
    """Optional replacement companion file tree.

    Omit to leave existing bundled files unchanged; send [] to remove bundled files.
    """

    metadata: object

    name: str

    body_slug: Annotated[str, PropertyInfo(alias="slug")]
    """New slug (renames the skill)"""

    summary: Optional[str]

    tags: SequenceNotStr[str]


class File(TypedDict, total=False):
    content: Required[str]

    path: Required[str]

    content_type: Annotated[str, PropertyInfo(alias="contentType")]

    metadata: object

    name: str

    summary: str

    tags: SequenceNotStr[str]
