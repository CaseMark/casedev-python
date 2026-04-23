# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EndpointRotateSecretParams"]


class EndpointRotateSecretParams(TypedDict, total=False):
    previous_secret_expires_in_sec: Annotated[int, PropertyInfo(alias="previousSecretExpiresInSec")]
    """How long (seconds) the old secret continues to be accepted.

    0 invalidates immediately. Default: 86400 (24h).
    """
