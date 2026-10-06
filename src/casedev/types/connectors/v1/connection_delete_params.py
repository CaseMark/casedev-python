# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ConnectionDeleteParams"]


class ConnectionDeleteParams(TypedDict, total=False):
    purge: bool

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
