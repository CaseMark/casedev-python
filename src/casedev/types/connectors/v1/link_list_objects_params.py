# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LinkListObjectsParams"]


class LinkListObjectsParams(TypedDict, total=False):
    cursor: str

    state: Literal["pending", "transferring", "ingesting", "synced", "skipped", "failed", "tombstoned"]

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
