# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DeploymentListParams"]


class DeploymentListParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]
    """Project ID"""

    limit: float
    """Maximum number of deployments to return"""

    state: str
    """Filter by deployment state"""

    target: Literal["production", "staging"]
    """Filter by deployment target"""
