# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["V1CreateParams"]


class V1CreateParams(TypedDict, total=False):
    name: Required[str]
    """Operator name"""

    model: str
    """Model to use"""

    size: Literal["small", "medium", "large"]
    """Instance size"""
