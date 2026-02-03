# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ProjectCreateBranchParams"]


class ProjectCreateBranchParams(TypedDict, total=False):
    name: Required[str]
    """Branch name (letters, numbers, hyphens, underscores only)"""

    parent_branch_id: Annotated[str, PropertyInfo(alias="parentBranchId")]
    """Parent branch ID to clone from (defaults to main branch)"""
