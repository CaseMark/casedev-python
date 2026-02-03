# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["InstanceCreateParams"]


class InstanceCreateParams(TypedDict, total=False):
    instance_type: Required[Annotated[str, PropertyInfo(alias="instanceType")]]
    """GPU type (e.g., 'gpu_1x_h100_sxm5')"""

    name: Required[str]
    """Instance name"""

    region: Required[str]
    """Region (e.g., 'us-west-1')"""

    auto_shutdown_minutes: Annotated[Optional[int], PropertyInfo(alias="autoShutdownMinutes")]
    """Auto-shutdown timer (null = never)"""

    vault_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="vaultIds")]
    """Vault IDs to mount"""
