# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1TrademarkSearchParams"]


class V1TrademarkSearchParams(TypedDict, total=False):
    registration_number: Annotated[str, PropertyInfo(alias="registrationNumber")]
    """USPTO registration number (e.g.

    "6123456"). Provide either serialNumber or registrationNumber.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """USPTO serial number (e.g.

    "97123456"). Provide either serialNumber or registrationNumber.
    """
