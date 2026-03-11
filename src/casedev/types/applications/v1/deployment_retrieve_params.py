# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DeploymentRetrieveParams"]


class DeploymentRetrieveParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]
    """Project ID used to verify access to the deployment"""

    include_logs: Annotated[bool, PropertyInfo(alias="includeLogs")]
    """Whether to include build logs in the response"""
