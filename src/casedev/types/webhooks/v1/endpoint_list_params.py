# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["EndpointListParams"]


class EndpointListParams(TypedDict, total=False):
    limit: int

    status: Literal["active", "disabled", "auto_disabled"]
    """Filter by endpoint status"""
