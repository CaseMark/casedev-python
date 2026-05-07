# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .read_response_file_bundle import ReadResponseFileBundle
from .read_response_root_bundle import ReadResponseRootBundle

__all__ = ["SkillReadResponse", "Bundle"]

Bundle: TypeAlias = Union[ReadResponseRootBundle, ReadResponseFileBundle, None]


class SkillReadResponse(BaseModel):
    author_name: Optional[str] = None
    """Skill author"""

    bundle: Optional[Bundle] = None
    """Skill bundle metadata for root skills and companion file rows"""

    content: Optional[str] = None
    """Full skill content in markdown"""

    license: Optional[str] = None
    """Skill license"""

    metadata: Optional[object] = None
    """Custom metadata (custom skills only)"""

    name: Optional[str] = None
    """Skill name"""

    slug: Optional[str] = None
    """Unique skill identifier"""

    source: Optional[Literal["curated", "custom"]] = None
    """Skill source (authenticated requests only)"""

    summary: Optional[str] = None
    """Brief skill description"""

    tags: Optional[List[str]] = None
    """Skill tags"""

    version: Optional[str] = None
    """Skill version"""
