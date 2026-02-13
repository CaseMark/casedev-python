# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["SubscriptionUpdateParams"]


class SubscriptionUpdateParams(TypedDict, total=False):
    id: Required[str]

    callback_url: Annotated[str, PropertyInfo(alias="callbackUrl")]

    clear_signing_secret: Annotated[bool, PropertyInfo(alias="clearSigningSecret")]

    event_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="eventTypes")]

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]

    object_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="objectIds")]

    signing_secret: Annotated[str, PropertyInfo(alias="signingSecret")]
