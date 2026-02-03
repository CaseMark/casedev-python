# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProjectListEnvParams"]


class ProjectListEnvParams(TypedDict, total=False):
    decrypt: bool
    """Whether to decrypt and return values (requires appropriate permissions)"""
