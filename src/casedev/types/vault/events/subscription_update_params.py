# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["SubscriptionUpdateParams"]


class SubscriptionUpdateParams(TypedDict, total=False):
    id: Required[str]

    callback_url: Annotated[str, PropertyInfo(alias="callbackUrl")]
    """Updated webhook endpoint URL for deliveries"""

    clear_signing_secret: Annotated[bool, PropertyInfo(alias="clearSigningSecret")]
    """Whether to remove the existing signing secret"""

    event_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="eventTypes")]
    """Updated event types to deliver for this subscription"""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Whether the subscription should continue delivering events"""

    object_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="objectIds")]
    """Updated vault object IDs to limit notifications to.

    Pass an empty array to remove the filter.
    """

    signing_secret: Annotated[str, PropertyInfo(alias="signingSecret")]
    """Replacement secret used to sign webhook deliveries"""
