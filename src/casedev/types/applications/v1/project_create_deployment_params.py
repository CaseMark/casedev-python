# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ProjectCreateDeploymentParams", "EnvironmentVariable"]


class ProjectCreateDeploymentParams(TypedDict, total=False):
    environment_variables: Annotated[Iterable[EnvironmentVariable], PropertyInfo(alias="environmentVariables")]
    """Additional environment variables to set or update before deployment"""


class EnvironmentVariable(TypedDict, total=False):
    key: Required[str]
    """Environment variable name"""

    target: Required[List[Literal["production", "preview", "development"]]]
    """Deployment targets for this variable"""

    value: Required[str]
    """Environment variable value"""

    type: Literal["plain", "encrypted", "secret"]
    """Variable type"""
