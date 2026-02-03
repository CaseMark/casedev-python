# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProjectCreateResponse", "DefaultBranch"]


class DefaultBranch(BaseModel):
    """Default 'main' branch details"""

    id: Optional[str] = None
    """Branch ID"""

    name: Optional[str] = None
    """Branch name"""


class ProjectCreateResponse(BaseModel):
    id: str
    """Project ID"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Project creation timestamp"""

    default_branch: DefaultBranch = FieldInfo(alias="defaultBranch")
    """Default 'main' branch details"""

    name: str
    """Project name"""

    pg_version: int = FieldInfo(alias="pgVersion")
    """PostgreSQL major version"""

    region: str
    """AWS region"""

    status: Literal["active", "suspended", "deleted"]
    """Project status"""

    description: Optional[str] = None
    """Project description"""
