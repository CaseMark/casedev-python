# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ProjectDeleteParams"]


class ProjectDeleteParams(TypedDict, total=False):
    delete_from_hosting: Annotated[bool, PropertyInfo(alias="deleteFromHosting")]
    """Also delete the project from hosting (default: true)"""
