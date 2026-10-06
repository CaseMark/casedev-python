# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SessionDeleteParams"]


class SessionDeleteParams(TypedDict, total=False):
    reason: Literal[
        "user_deleted", "replaced_scope_changed", "replaced_missing_session", "replaced_runtime_unavailable"
    ]
    """Why the session is being ended; recorded in the linc.session.ended event
    payload.

    Unknown values fall back to user*deleted. The replaced*\\** values distinguish
    automatic session replacement (e.g. by C3) from a user-initiated deletion.
    """
