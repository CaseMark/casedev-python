# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectOrganizeResponse", "Move"]


class Move(BaseModel):
    id: Optional[str] = None

    path: Optional[str] = None

    previous_path: Optional[str] = FieldInfo(alias="previousPath", default=None)


class ObjectOrganizeResponse(BaseModel):
    folder_paths: Optional[List[str]] = FieldInfo(alias="folderPaths", default=None)

    moves: Optional[List[Move]] = None
