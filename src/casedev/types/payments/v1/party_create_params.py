# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PartyCreateParams"]


class PartyCreateParams(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["individual", "organization"]]

    address_line1: str

    city: str

    country: str

    email: str

    metadata: object

    phone: str

    postal_code: str

    role: Literal["client", "vendor", "counsel", "expert", "lien_holder", "funder", "opposing_party", "other"]

    state: str
