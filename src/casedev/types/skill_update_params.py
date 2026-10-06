# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SkillUpdateParams", "File"]


class SkillUpdateParams(TypedDict, total=False):
    content: str

    expected_version: Annotated[int, PropertyInfo(alias="expectedVersion")]
    """Reject with 409 if the skill changed since this version was read."""

    files: Optional[Iterable[File]]
    """Optional replacement companion file tree, limited to 12 MiB of decoded content.

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
    """
    UTF-8 text when encoding is utf8 (max 65,536 characters), or canonical base64
    when encoding is base64 (max 262,144 decoded bytes).
    """

    path: Required[str]

    content_type: Annotated[str, PropertyInfo(alias="contentType")]

    encoding: Literal["utf8", "base64"]
    """How content is encoded. Omit for UTF-8 text files."""

    metadata: object

    name: str

    summary: str

    tags: SequenceNotStr[str]
