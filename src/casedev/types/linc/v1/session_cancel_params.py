# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SessionCancelParams"]


class SessionCancelParams(TypedDict, total=False):
    clear_queue: Annotated[bool, PropertyInfo(alias="clearQueue")]
    """
    Also clear queued steering/follow-up messages so the abort leaves the agent
    fully idle. Cleared texts are returned in the `response.data.clearedQueue` field
    of the response body. Without it, messages still queued when the abort settles
    are auto-continued as a new run. Runtimes older than the Linc release that
    supports this flag ignore it: the abort still happens but the queue is left
    untouched.
    """
