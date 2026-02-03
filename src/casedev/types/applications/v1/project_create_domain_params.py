# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ProjectCreateDomainParams"]


class ProjectCreateDomainParams(TypedDict, total=False):
    domain: Required[str]
    """Domain name to add"""

    git_branch: Annotated[str, PropertyInfo(alias="gitBranch")]
    """Git branch to associate with this domain"""
