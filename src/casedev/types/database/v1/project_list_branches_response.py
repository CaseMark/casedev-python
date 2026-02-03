# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProjectListBranchesResponse", "Branch"]


class Branch(BaseModel):
    id: Optional[str] = None
    """Branch ID"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Branch creation timestamp"""

    is_default: Optional[bool] = FieldInfo(alias="isDefault", default=None)
    """Whether this is the default branch"""

    name: Optional[str] = None
    """Branch name"""

    parent_branch_id: Optional[str] = FieldInfo(alias="parentBranchId", default=None)
    """Parent branch ID (null for default branch)"""

    status: Optional[str] = None
    """Branch status"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Branch last update timestamp"""


class ProjectListBranchesResponse(BaseModel):
    branches: List[Branch]
