# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1UpdateParams"]


class V1UpdateParams(TypedDict, total=False):
    archived_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

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

    title: str
