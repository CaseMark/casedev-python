# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SessionSendRpcParams"]


class SessionSendRpcParams(TypedDict, total=False):
    type: Required[str]
    """Native Pi/Linc RPC command type.

    Prompt commands also require a string id for idempotency.
    """

    body_id: Annotated[str, PropertyInfo(alias="id")]
    """Command idempotency key. Required when type is prompt."""
