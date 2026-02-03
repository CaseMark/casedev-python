# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PartyUpdateParams"]


class PartyUpdateParams(TypedDict, total=False):
    address_line1: str

    address_line2: str

    city: str

    country: str

    email: str

    is_active: bool

    metadata: object

    name: str

    notes: str

    phone: str

    postal_code: str

    role: Literal["client", "vendor", "counsel", "expert", "lien_holder", "funder", "opposing_party", "other"]

    state: str
