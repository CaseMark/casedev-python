# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InstallationListParams"]


class InstallationListParams(TypedDict, total=False):
    application: str

    cursor: str
    """Opaque continuation cursor from `pagination.next_cursor` of the previous page.

    Must be replayed with the same filters and scope that produced it.
    """

    external_tenant_id: str

    limit: int
    """Installations per page (1-200). Defaults to 200."""
