# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AssemblyCreateResponse", "Volume"]


class Volume(BaseModel):
    filename: Optional[str] = None

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)


class AssemblyCreateResponse(BaseModel):
    id: Optional[str] = None

    client_reference: Optional[str] = FieldInfo(alias="clientReference", default=None)

    status: Optional[Literal["queued", "processing", "completed", "failed"]] = None

    volumes: Optional[List[Volume]] = None
