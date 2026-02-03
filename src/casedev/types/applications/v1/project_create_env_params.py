# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ProjectCreateEnvParams"]


class ProjectCreateEnvParams(TypedDict, total=False):
    key: Required[str]
    """Environment variable name"""

    target: Required[List[Literal["production", "preview", "development"]]]
    """Deployment targets for this variable"""

    value: Required[str]
    """Environment variable value"""

    git_branch: Annotated[str, PropertyInfo(alias="gitBranch")]
    """Specific git branch (for preview deployments)"""

    type: Literal["plain", "encrypted", "secret"]
    """Variable type"""
