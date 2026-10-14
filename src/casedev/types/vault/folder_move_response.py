# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FolderMoveResponse"]


class FolderMoveResponse(BaseModel):
    folder_paths: Optional[List[str]] = FieldInfo(alias="folderPaths", default=None)

    moved_files: Optional[int] = FieldInfo(alias="movedFiles", default=None)

    new_path: Optional[str] = FieldInfo(alias="newPath", default=None)

    path: Optional[str] = None

    revision: Optional[str] = None
