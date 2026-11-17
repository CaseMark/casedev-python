# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ConnectionCreateFolderParams"]


class ConnectionCreateFolderParams(TypedDict, total=False):
    name: Required[str]
    """Folder name.

    Trimmed; 1-255 characters; no '/', '\', or control characters; not '.' or '..'.
    Providers may refuse further characters.
    """

    container: str
    """Container id of the parent, from its browse_ref"""

    parent: str
    """Folder id of the parent, from its browse_ref. Omit for a container root."""

    site: str
    """Site id of the parent, from its browse_ref"""

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
