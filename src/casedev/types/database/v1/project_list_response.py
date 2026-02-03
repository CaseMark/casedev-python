# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProjectListResponse", "Project", "ProjectLinkedDeployment"]


class ProjectLinkedDeployment(BaseModel):
    id: Optional[str] = None
    """Deployment ID"""

    name: Optional[str] = None
    """Deployment name"""

    type: Optional[Literal["thurgood", "compute"]] = None
    """Type of deployment"""

    url: Optional[str] = None
    """Deployment URL (for Thurgood apps)"""


class Project(BaseModel):
    id: Optional[str] = None
    """Project ID"""

    compute_time_seconds: Optional[float] = FieldInfo(alias="computeTimeSeconds", default=None)
    """Total compute time consumed in seconds"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Project creation timestamp"""

    description: Optional[str] = None
    """Project description"""

    linked_deployments: Optional[List[ProjectLinkedDeployment]] = FieldInfo(alias="linkedDeployments", default=None)
    """Linked application deployments using this database"""

    name: Optional[str] = None
    """Project name"""

    pg_version: Optional[int] = FieldInfo(alias="pgVersion", default=None)
    """PostgreSQL major version"""

    region: Optional[str] = None
    """AWS region where database is deployed"""

    status: Optional[Literal["active", "suspended", "deleted"]] = None
    """Current project status"""

    storage_size_bytes: Optional[float] = FieldInfo(alias="storageSizeBytes", default=None)
    """Current storage usage in bytes"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Project last update timestamp"""


class ProjectListResponse(BaseModel):
    projects: List[Project]
