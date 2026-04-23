# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["EndpointCreateParams", "ResourceScopes"]


class EndpointCreateParams(TypedDict, total=False):
    event_type_filters: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="eventTypeFilters")]]
    """Glob patterns of event types to deliver (e.g.

    "vault._", "ocr.job.completed", "_")
    """

    url: Required[str]
    """HTTPS callback URL that will receive event deliveries"""

    description: str
    """Human-readable label for this endpoint"""

    resource_scopes: Annotated[ResourceScopes, PropertyInfo(alias="resourceScopes")]
    """Optional per-resource allowlists.

    If vaultIds is set, only events for those vaults are delivered. Same for
    matterIds.
    """


class ResourceScopes(TypedDict, total=False):
    """Optional per-resource allowlists.

    If vaultIds is set, only events for those vaults are delivered. Same for matterIds.
    """

    matter_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="matterIds")]

    vault_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="vaultIds")]
