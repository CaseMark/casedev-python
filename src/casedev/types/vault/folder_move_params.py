# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FolderMoveParams"]


class FolderMoveParams(TypedDict, total=False):
    new_path: Required[Annotated[str, PropertyInfo(alias="newPath")]]

    path: Required[str]

    expected_revision: Annotated[str, PropertyInfo(alias="expectedRevision")]
    """Revision from a previous move, for safe Undo."""
