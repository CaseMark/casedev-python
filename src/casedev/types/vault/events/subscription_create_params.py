# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["SubscriptionCreateParams"]


class SubscriptionCreateParams(TypedDict, total=False):
    callback_url: Required[Annotated[str, PropertyInfo(alias="callbackUrl")]]
    """Webhook endpoint URL that will receive vault event deliveries"""

    event_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="eventTypes")]
    """Vault event types to deliver. Omit to receive the default supported set."""

    object_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="objectIds")]
    """Vault object IDs to limit notifications to.

    Omit to receive events for all objects in the vault.
    """

    signing_secret: Annotated[str, PropertyInfo(alias="signingSecret")]
    """Optional secret used to sign outbound webhook deliveries"""
