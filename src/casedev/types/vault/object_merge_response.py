# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectMergeResponse"]


class ObjectMergeResponse(BaseModel):
    client_reference: Optional[str] = FieldInfo(alias="clientReference", default=None)

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)

    status: Optional[Literal["processing"]] = None

    workflow_id: Optional[str] = FieldInfo(alias="workflowId", default=None)
