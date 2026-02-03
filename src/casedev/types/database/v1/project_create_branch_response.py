# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProjectCreateBranchResponse"]


class ProjectCreateBranchResponse(BaseModel):
    id: str
    """Branch ID"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Branch creation timestamp"""

    is_default: bool = FieldInfo(alias="isDefault")
    """Whether this is the default branch (always false for new branches)"""

    name: str
    """Branch name"""

    parent_branch_id: Optional[str] = FieldInfo(alias="parentBranchId", default=None)
    """Parent branch ID"""

    status: str
    """Branch status"""
