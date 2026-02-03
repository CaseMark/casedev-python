# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ProjectCreateParams", "EnvironmentVariable"]


class ProjectCreateParams(TypedDict, total=False):
    git_repo: Required[Annotated[str, PropertyInfo(alias="gitRepo")]]
    """GitHub repository URL or "owner/repo" """

    name: Required[str]
    """Project name"""

    build_command: Annotated[str, PropertyInfo(alias="buildCommand")]
    """Custom build command"""

    environment_variables: Annotated[Iterable[EnvironmentVariable], PropertyInfo(alias="environmentVariables")]
    """Environment variables to set on the project"""

    framework: str
    """Framework (e.g., "nextjs", "remix", "astro")"""

    git_branch: Annotated[str, PropertyInfo(alias="gitBranch")]
    """Git branch to deploy"""

    install_command: Annotated[str, PropertyInfo(alias="installCommand")]
    """Custom install command"""

    output_directory: Annotated[str, PropertyInfo(alias="outputDirectory")]
    """Build output directory"""

    root_directory: Annotated[str, PropertyInfo(alias="rootDirectory")]
    """Root directory of the project"""


class EnvironmentVariable(TypedDict, total=False):
    key: Required[str]
    """Environment variable name"""

    target: Required[List[Literal["production", "preview", "development"]]]
    """Deployment targets for this variable"""

    value: Required[str]
    """Environment variable value"""

    type: Literal["plain", "encrypted", "secret"]
    """Variable type"""
