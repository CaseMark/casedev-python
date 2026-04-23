# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EndpointTestParams"]


class EndpointTestParams(TypedDict, total=False):
    event_type: Annotated[str, PropertyInfo(alias="eventType")]
    """Event type to simulate. Defaults to "webhook.test"."""

    payload: object
    """Custom `data` payload. Defaults to a small placeholder."""
