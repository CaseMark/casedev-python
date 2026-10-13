# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LinkDeleteParams"]


class LinkDeleteParams(TypedDict, total=False):
    vault_docs: Literal["keep", "delete"]

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
