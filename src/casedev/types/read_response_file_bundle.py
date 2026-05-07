# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ReadResponseFileBundle"]


class ReadResponseFileBundle(BaseModel):
    path: str

    role: Literal["file"]

    root_slug: str

    content_type: Optional[str] = None
