# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProjectGetConnectionParams"]


class ProjectGetConnectionParams(TypedDict, total=False):
    branch: str
    """Branch name (defaults to 'main')"""

    pooled: bool
    """Use pooled connection (PgBouncer)"""
