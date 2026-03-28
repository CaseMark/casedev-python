# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PartyCreateParams"]


class PartyCreateParams(TypedDict, total=False):
    name: Required[str]

    addresses: Iterable[Dict[str, object]]

    custom_fields: Optional[Dict[str, object]]

    email: str

    metadata: Dict[str, object]

    notes: Optional[str]

    phone: str

    type: Literal["person", "organization"]
