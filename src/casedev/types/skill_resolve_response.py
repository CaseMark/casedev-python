# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SkillResolveResponse", "Result"]


class Result(BaseModel):
    name: Optional[str] = None
    """Skill name"""

    score: Optional[float] = None
    """Relevance score"""

    slug: Optional[str] = None
    """Unique skill identifier"""

    source: Optional[Literal["curated", "custom"]] = None
    """Whether the skill is curated or org-custom"""

    summary: Optional[str] = None
    """Brief skill description"""

    tags: Optional[List[str]] = None
    """Skill tags"""


class SkillResolveResponse(BaseModel):
    methods_used: Optional[List[str]] = None
    """Search methods used (text, tag, semantic)"""

    results: Optional[List[Result]] = None
