# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ConnectionListContentsParams"]


class ConnectionListContentsParams(TypedDict, total=False):
    container: str
    """Container to list, or the container holding parent"""

    cursor: str

    page_size: int

    parent: str
    """Folder to list"""

    site: str
    """Site of the folder"""

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
