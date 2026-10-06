# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LinkListParams"]


class LinkListParams(TypedDict, total=False):
    connection_id: str

    cursor: str
    """Opaque cursor from the previous page."""

    direction: Literal["import", "export"]

    mode: Literal["once", "synced"]

    pair_id: str

    state: Literal["ready", "running", "active", "paused", "orphaned", "error"]

    vault_id: str

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
