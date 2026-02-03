# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1DeleteParams"]


class V1DeleteParams(TypedDict, total=False):
    delete_deployments: Annotated[bool, PropertyInfo(alias="deleteDeployments")]
    """Whether to also delete all deployments (default: true)"""
