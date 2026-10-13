# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SkillCatalogResponse", "Skill"]


class Skill(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None

    slug: Optional[str] = None

    source: Optional[Literal["custom", "curated"]] = None

    tags: Optional[List[str]] = None


class SkillCatalogResponse(BaseModel):
    count: Optional[int] = None

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    limit: Optional[int] = None

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)

    offset: Optional[int] = None

    query: Optional[str] = None

    skills: Optional[List[Skill]] = None

    total: Optional[int] = None
