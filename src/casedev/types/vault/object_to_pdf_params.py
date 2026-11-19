# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ObjectToPdfParams"]


class ObjectToPdfParams(TypedDict, total=False):
    id: Required[str]

    force: bool
    """Make the PDF version again even when one is ready"""
