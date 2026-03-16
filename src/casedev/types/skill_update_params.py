# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SkillUpdateParams"]


class SkillUpdateParams(TypedDict, total=False):
    content: str

    metadata: object

    name: str

    body_slug: Annotated[str, PropertyInfo(alias="slug")]
    """New slug (renames the skill)"""

    summary: Optional[str]

    tags: SequenceNotStr[str]
