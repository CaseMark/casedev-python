# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1ListResponse", "Project"]


class Project(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    framework: Optional[str] = None

    name: Optional[str] = None

    slug: Optional[str] = None

    source_type: Optional[Literal["github", "thurgood"]] = FieldInfo(alias="sourceType", default=None)


class V1ListResponse(BaseModel):
    projects: Optional[List[Project]] = None
