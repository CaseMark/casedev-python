# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1ExecuteParams"]


class V1ExecuteParams(TypedDict, total=False):
    callback_headers: Annotated[object, PropertyInfo(alias="callbackHeaders")]
    """Headers to include in callback request (e.g., Authorization)"""

    callback_url: Annotated[str, PropertyInfo(alias="callbackUrl")]
    """URL to POST results when workflow completes (enables callback mode)"""

    input: object
    """Input data to pass to the workflow"""

    api_timeout: Annotated[str, PropertyInfo(alias="timeout")]
    """Timeout for sync wait mode (e.g., '30s', '2m'). Max 5m. Default: 30s"""

    wait: bool
    """Wait for completion (default: false, max 5 min)"""
