# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MatterPartyCreateParams"]


class MatterPartyCreateParams(TypedDict, total=False):
    party_id: Required[str]

    role: Required[
        Literal[
            "client",
            "prospect",
            "opposing_party",
            "opposing_counsel",
            "co_counsel",
            "judge",
            "expert",
            "witness",
            "vendor",
            "insurer",
            "other",
        ]
    ]

    custom_fields: Optional[Dict[str, object]]

    is_primary: bool

    metadata: Dict[str, object]

    notes: Optional[str]

    set_as_client: bool
