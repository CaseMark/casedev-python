# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SkillExportResponse", "File"]


class File(BaseModel):
    content: Optional[str] = None

    content_type: Optional[str] = None

    encoding: Optional[Literal["utf8", "base64"]] = None
    """Encoding of content. Binary files use canonical base64."""

    path: Optional[str] = None

    sha256: Optional[str] = None

    size_bytes: Optional[int] = None


class SkillExportResponse(BaseModel):
    files: Optional[List[File]] = None

    root: Optional[str] = None

    slug: Optional[str] = None

    source: Optional[Literal["custom", "curated"]] = None

    target: Optional[str] = None
