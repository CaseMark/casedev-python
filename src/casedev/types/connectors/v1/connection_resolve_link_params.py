# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ConnectionResolveLinkParams"]


class ConnectionResolveLinkParams(TypedDict, total=False):
    url: Required[str]
    """Folder link copied from the provider, including any query string"""

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
