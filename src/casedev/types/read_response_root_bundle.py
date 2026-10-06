# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ReadResponseRootBundle", "File"]


class File(BaseModel):
    path: str

    slug: str

    content_type: Optional[str] = None

    encoding: Optional[Literal["utf8", "base64"]] = None
    """Encoding used by content when this companion slug is read."""

    name: Optional[str] = None


class ReadResponseRootBundle(BaseModel):
    files: List[File]

    role: Literal["root"]
