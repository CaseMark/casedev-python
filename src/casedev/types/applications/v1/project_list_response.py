# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProjectListResponse", "Project", "ProjectDomain"]


class ProjectDomain(BaseModel):
    id: Optional[str] = None
    """Domain record identifier"""

    domain: Optional[str] = None
    """Hostname assigned to the project"""

    is_primary: Optional[bool] = FieldInfo(alias="isPrimary", default=None)
    """Whether this is the primary project domain"""

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)
    """Whether the domain has been verified by the hosting provider"""


class Project(BaseModel):
    id: Optional[str] = None
    """Project identifier"""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """When the project record was created"""

    domains: Optional[List[ProjectDomain]] = None
    """Custom or generated domains assigned to the project"""

    framework: Optional[str] = None
    """Detected or configured application framework"""

    git_branch: Optional[str] = FieldInfo(alias="gitBranch", default=None)
    """Default Git branch used for deployments"""

    git_repo: Optional[str] = FieldInfo(alias="gitRepo", default=None)
    """Connected Git repository in owner/repo format"""

    name: Optional[str] = None
    """Project display name"""

    status: Optional[str] = None
    """Current project deployment status"""

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
    """When the project record was last updated"""

    vercel_project_id: Optional[str] = FieldInfo(alias="vercelProjectId", default=None)
    """Hosting provider project ID, when linked"""


class ProjectListResponse(BaseModel):
    projects: Optional[List[Project]] = None
    """Projects and deployed apps visible to the organization"""
