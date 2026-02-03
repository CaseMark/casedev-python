# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProjectRetrieveResponse", "Branch", "Database", "LinkedDeployment"]


class Branch(BaseModel):
    id: Optional[str] = None
    """Branch ID"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Branch creation timestamp"""

    is_default: Optional[bool] = FieldInfo(alias="isDefault", default=None)
    """Whether this is the default branch"""

    name: Optional[str] = None
    """Branch name"""

    status: Optional[str] = None
    """Branch status"""


class Database(BaseModel):
    id: Optional[str] = None
    """Database ID"""

    name: Optional[str] = None
    """Database name"""

    owner_name: Optional[str] = FieldInfo(alias="ownerName", default=None)
    """Database owner role name"""


class LinkedDeployment(BaseModel):
    id: Optional[str] = None
    """Deployment ID"""

    env_var_name: Optional[str] = FieldInfo(alias="envVarName", default=None)
    """Environment variable name for connection string"""

    name: Optional[str] = None
    """Deployment name"""

    type: Optional[Literal["thurgood", "compute"]] = None
    """Deployment type"""

    url: Optional[str] = None
    """Deployment URL"""


class ProjectRetrieveResponse(BaseModel):
    id: str
    """Project ID"""

    branches: List[Branch]
    """All branches in this project"""

    compute_time_seconds: float = FieldInfo(alias="computeTimeSeconds")
    """Total compute time consumed in seconds"""

    connection_host: str = FieldInfo(alias="connectionHost")
    """Database connection hostname (masked for security)"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Project creation timestamp"""

    databases: List[Database]
    """Databases in the default branch"""

    linked_deployments: List[LinkedDeployment] = FieldInfo(alias="linkedDeployments")
    """Linked deployments using this database"""

    name: str
    """Project name"""

    pg_version: int = FieldInfo(alias="pgVersion")
    """PostgreSQL major version"""

    region: str
    """AWS region"""

    status: Literal["active", "suspended", "deleted"]
    """Project status"""

    storage_size_bytes: float = FieldInfo(alias="storageSizeBytes")
    """Current storage usage in bytes"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Project last update timestamp"""

    description: Optional[str] = None
    """Project description"""
