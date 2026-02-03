# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ProjectListDeploymentsParams"]


class ProjectListDeploymentsParams(TypedDict, total=False):
    limit: float
    """Maximum number of deployments to return"""

    state: str
    """Filter by deployment state"""

    target: Literal["production", "staging"]
    """Filter by deployment target"""
