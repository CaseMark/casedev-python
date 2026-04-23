# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["EndpointUpdateParams", "ResourceScopes"]


class EndpointUpdateParams(TypedDict, total=False):
    description: Optional[str]

    event_type_filters: Annotated[SequenceNotStr[str], PropertyInfo(alias="eventTypeFilters")]

    resource_scopes: Annotated[Optional[ResourceScopes], PropertyInfo(alias="resourceScopes")]

    status: Literal["active", "disabled"]

    url: str


class ResourceScopes(TypedDict, total=False):
    matter_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="matterIds")]

    vault_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="vaultIds")]
