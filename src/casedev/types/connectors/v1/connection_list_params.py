# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ConnectionListParams"]


class ConnectionListParams(TypedDict, total=False):
    cursor: str
    """Opaque continuation cursor from `pagination.next_cursor` of the previous page.

    Must be replayed with the same filters and scope that produced it.
    """

    limit: int
    """Connections per page (1-200). Defaults to 200."""

    provider: str

    status: Literal["pending", "healthy", "reauth_required", "revoked", "throttled"]

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
