# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ProjectCreateParams", "EnvironmentVariable"]


class ProjectCreateParams(TypedDict, total=False):
    git_repo: Required[Annotated[str, PropertyInfo(alias="gitRepo")]]
    """GitHub repository URL or owner/repo identifier"""

    name: Required[str]
    """Human-readable project name"""

    build_command: Annotated[str, PropertyInfo(alias="buildCommand")]
    """Custom build command to override the framework default"""

    environment_variables: Annotated[Iterable[EnvironmentVariable], PropertyInfo(alias="environmentVariables")]
    """Environment variables to create before the first deployment"""

    framework: str
    """Framework preset for the hosting project, such as nextjs or remix"""

    git_branch: Annotated[str, PropertyInfo(alias="gitBranch")]
    """Git branch to deploy. Defaults to main."""

    install_command: Annotated[str, PropertyInfo(alias="installCommand")]
    """Custom install command to override the framework default"""

    output_directory: Annotated[str, PropertyInfo(alias="outputDirectory")]
    """Build output directory relative to the project root"""

    root_directory: Annotated[str, PropertyInfo(alias="rootDirectory")]
    """Repository subdirectory that contains the app to deploy"""


class EnvironmentVariable(TypedDict, total=False):
    key: Required[str]
    """Environment variable name"""

    target: Required[List[Literal["production", "preview", "development"]]]
    """Deployment targets that should receive this variable"""

    value: Required[str]
    """Environment variable value"""

    type: Literal["plain", "encrypted", "secret"]
    """Storage mode for the environment variable value"""
