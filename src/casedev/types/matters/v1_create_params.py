# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1CreateParams", "Vault"]


class V1CreateParams(TypedDict, total=False):
    title: Required[str]

    billing: Dict[str, object]

    client_name: str

    client_party_id: Optional[str]

    custom_fields: Dict[str, object]

    description: str

    display_id: str

    important_dates: Dict[str, object]

    jurisdiction: Dict[str, object]

    matter_type: str

    metadata: Dict[str, object]

    practice_area: str

    responsible_attorney_id: str

    status: Literal["intake", "open", "pending", "closed", "archived"]

    subtype: str

    vault: Vault


class Vault(TypedDict, total=False):
    description: str

    enable_graph: Annotated[bool, PropertyInfo(alias="enableGraph")]

    enable_indexing: Annotated[bool, PropertyInfo(alias="enableIndexing")]

    metadata: Dict[str, object]
