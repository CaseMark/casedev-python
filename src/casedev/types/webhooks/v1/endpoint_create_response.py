# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["EndpointCreateResponse", "Endpoint", "EndpointResourceScopes"]


class EndpointResourceScopes(BaseModel):
    matter_ids: Optional[List[str]] = FieldInfo(alias="matterIds", default=None)

    vault_ids: Optional[List[str]] = FieldInfo(alias="vaultIds", default=None)


class Endpoint(BaseModel):
    id: str

    consecutive_failure_count: int = FieldInfo(alias="consecutiveFailureCount")

    created_at: datetime = FieldInfo(alias="createdAt")

    description: Optional[str] = None

    disabled_reason: Optional[str] = FieldInfo(alias="disabledReason", default=None)

    event_type_filters: List[str] = FieldInfo(alias="eventTypeFilters")

    has_previous_signing_secret: bool = FieldInfo(alias="hasPreviousSigningSecret")

    last_failure_at: Optional[datetime] = FieldInfo(alias="lastFailureAt", default=None)

    last_success_at: Optional[datetime] = FieldInfo(alias="lastSuccessAt", default=None)

    previous_signing_secret_expires_at: Optional[datetime] = FieldInfo(
        alias="previousSigningSecretExpiresAt", default=None
    )

    resource_scopes: Optional[EndpointResourceScopes] = FieldInfo(alias="resourceScopes", default=None)

    status: Literal["active", "disabled", "auto_disabled"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    url: str


class EndpointCreateResponse(BaseModel):
    endpoint: Endpoint

    signing_secret: str = FieldInfo(alias="signingSecret")
    """One-time webhook signing secret."""
