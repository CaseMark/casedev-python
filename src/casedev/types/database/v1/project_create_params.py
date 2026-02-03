# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProjectCreateParams"]


class ProjectCreateParams(TypedDict, total=False):
    name: Required[str]
    """Project name (letters, numbers, hyphens, underscores only)"""

    description: str
    """Optional project description"""

    region: Literal[
        "aws-us-east-1",
        "aws-us-east-2",
        "aws-us-west-2",
        "aws-eu-central-1",
        "aws-eu-west-1",
        "aws-eu-west-2",
        "aws-ap-southeast-1",
        "aws-ap-southeast-2",
    ]
    """AWS region for database deployment"""
