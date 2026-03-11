# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DeploymentCreateParams"]


class DeploymentCreateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]
    """Project ID to deploy"""

    ref: str
    """Git branch, tag, or commit to deploy. Defaults to the project branch."""

    target: Literal["production", "preview"]
    """Deployment target environment"""
