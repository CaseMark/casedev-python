# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1CreateParams"]


class V1CreateParams(TypedDict, total=False):
    name: Required[str]
    """Project name"""

    source_type: Required[Annotated[Literal["github", "thurgood"], PropertyInfo(alias="sourceType")]]

    build_command: Annotated[str, PropertyInfo(alias="buildCommand")]

    default_memory: Annotated[str, PropertyInfo(alias="defaultMemory")]

    default_vcpu: Annotated[str, PropertyInfo(alias="defaultVcpu")]

    description: str
    """Project description"""

    framework: str

    github_branch: Annotated[str, PropertyInfo(alias="githubBranch")]

    github_repo: Annotated[str, PropertyInfo(alias="githubRepo")]
    """GitHub repo (owner/repo)"""

    install_command: Annotated[str, PropertyInfo(alias="installCommand")]

    root_directory: Annotated[str, PropertyInfo(alias="rootDirectory")]

    s3_source_bucket: Annotated[str, PropertyInfo(alias="s3SourceBucket")]

    s3_source_prefix: Annotated[str, PropertyInfo(alias="s3SourcePrefix")]

    start_command: Annotated[str, PropertyInfo(alias="startCommand")]

    thurgood_session_id: Annotated[str, PropertyInfo(alias="thurgoodSessionId")]
