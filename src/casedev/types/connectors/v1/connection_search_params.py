# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ConnectionSearchParams"]


class ConnectionSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search text"""

    container: str
    """Container to search in, or the container holding parent"""

    cursor: str

    kind: Literal["file", "folder"]
    """What to search for: files, or folders by name"""

    page_size: int

    parent: str
    """Folder to search in"""

    site: str
    """Site to search in"""

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
