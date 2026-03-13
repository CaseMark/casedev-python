# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["FileListResponse", "File"]


class File(BaseModel):
    name: Optional[str] = None

    path: Optional[str] = None
    """Relative path from /workspace"""

    size_bytes: Optional[int] = FieldInfo(alias="sizeBytes", default=None)


class FileListResponse(BaseModel):
    chat_id: Optional[str] = FieldInfo(alias="chatId", default=None)

    files: Optional[List[File]] = None
