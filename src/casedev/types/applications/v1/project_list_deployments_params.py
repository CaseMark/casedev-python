# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ProjectListDeploymentsParams"]


class ProjectListDeploymentsParams(TypedDict, total=False):
    limit: float
    """Maximum number of deployments to return"""

    state: str
    """Deployment state to filter by"""

    target: Literal["production", "staging"]
    """Deployment target to filter by"""
