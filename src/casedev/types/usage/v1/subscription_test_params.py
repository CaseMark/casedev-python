# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SubscriptionTestParams"]


class SubscriptionTestParams(TypedDict, total=False):
    event_type: Annotated[str, PropertyInfo(alias="eventType")]

    payload: Dict[str, object]
