# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProjectListResponse", "Project", "ProjectDomain"]


class ProjectDomain(BaseModel):
    id: Optional[str] = None

    domain: Optional[str] = None

    is_primary: Optional[bool] = FieldInfo(alias="isPrimary", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)


class Project(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    domains: Optional[List[ProjectDomain]] = None

    framework: Optional[str] = None

    git_branch: Optional[str] = FieldInfo(alias="gitBranch", default=None)

    git_repo: Optional[str] = FieldInfo(alias="gitRepo", default=None)

    name: Optional[str] = None

    status: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    vercel_project_id: Optional[str] = FieldInfo(alias="vercelProjectId", default=None)


class ProjectListResponse(BaseModel):
    projects: Optional[List[Project]] = None
