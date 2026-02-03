# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1DeleteResponse", "ResourcesDeleted"]


class ResourcesDeleted(BaseModel):
    bundles: Optional[float] = None

    code_build: Optional[float] = FieldInfo(alias="codeBuild", default=None)

    routing_entries: Optional[float] = FieldInfo(alias="routingEntries", default=None)

    s3_sources: Optional[float] = FieldInfo(alias="s3Sources", default=None)


class V1DeleteResponse(BaseModel):
    id: Optional[str] = None

    deployments_deleted: Optional[float] = FieldInfo(alias="deploymentsDeleted", default=None)

    message: Optional[str] = None

    resources_deleted: Optional[ResourcesDeleted] = FieldInfo(alias="resourcesDeleted", default=None)

    status: Optional[str] = None
