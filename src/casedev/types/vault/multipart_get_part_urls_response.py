# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MultipartGetPartURLsResponse", "URL"]


class URL(BaseModel):
    part_number: Optional[int] = FieldInfo(alias="partNumber", default=None)

    url: Optional[str] = None


class MultipartGetPartURLsResponse(BaseModel):
    urls: Optional[List[URL]] = None
