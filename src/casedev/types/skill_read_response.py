# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["SkillReadResponse", "Bundle", "BundleUnionMember0", "BundleUnionMember0File", "BundleUnionMember1"]


class BundleUnionMember0File(BaseModel):
    path: str

    slug: str

    content_type: Optional[str] = None

    name: Optional[str] = None


class BundleUnionMember0(BaseModel):
    files: List[BundleUnionMember0File]

    role: Literal["root"]


class BundleUnionMember1(BaseModel):
    path: str

    role: Literal["file"]

    root_slug: str

    content_type: Optional[str] = None


Bundle: TypeAlias = Union[BundleUnionMember0, BundleUnionMember1, None]


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
