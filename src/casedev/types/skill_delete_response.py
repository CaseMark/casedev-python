# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SkillDeleteResponse"]


class SkillDeleteResponse(BaseModel):
    deleted: Optional[bool] = None

    slug: Optional[str] = None
