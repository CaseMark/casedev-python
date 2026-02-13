# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SubscriptionTestParams"]


class SubscriptionTestParams(TypedDict, total=False):
    id: Required[str]

    event_type: Annotated[str, PropertyInfo(alias="eventType")]
    """Optional event type override for this test"""

    object_id: Annotated[str, PropertyInfo(alias="objectId")]
    """Optional object ID for object-scoped payload testing"""

    payload: Dict[str, object]
    """Optional additional fields merged into payload.data"""
