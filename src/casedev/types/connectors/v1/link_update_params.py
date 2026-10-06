# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LinkUpdateParams"]


class LinkUpdateParams(TypedDict, total=False):
    mode: Literal["once", "synced"]

    policy: object
    """Replaces the entire stored policy; omitted fields return to defaults.

    Repeat deletes, collisions and filters that should be retained. Folder/file
    exclusions require deletes: preserve (the default).
    """

    state: Literal["paused", "ready"]

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
