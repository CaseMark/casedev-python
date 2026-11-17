# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ConnectionListResponse",
    "Capabilities",
    "Connection",
    "Pagination",
    "Provider",
    "ProviderAuthorizationOption",
    "ProviderSearch",
]


class Capabilities(BaseModel):
    google_drive_folder_mirroring: Optional[bool] = None


class Connection(BaseModel):
    organization_id: Optional[str] = None
    """
    Authenticated organization owning this connection; server-side approval binding
    uses this identifier.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Pagination(BaseModel):
    has_more: Optional[bool] = None

    limit: Optional[int] = None

    next_cursor: Optional[str] = None


class ProviderAuthorizationOption(BaseModel):
    label: Optional[str] = None

    scope_tier: Optional[str] = None

    write_scope_tier: Optional[str] = None
    """Explicit write-authorization upgrade for this account choice.

    Null means unavailable by policy; omitted when no upgrade is required.
    """


class ProviderSearch(BaseModel):
    """Present when GET /connections/{id}/search works for this provider."""

    folder_scope_recursive: Optional[bool] = None

    full_text: Optional[bool] = None

    kinds: Optional[List[Literal["file", "folder"]]] = None
    """Values the search kind parameter accepts."""

    max_page_size: Optional[int] = None

    scopes: Optional[List[Literal["account", "folder"]]] = None


class Provider(BaseModel):
    id: Optional[str] = None

    authorization_options: Optional[List[ProviderAuthorizationOption]] = None
    """
    Adapter-declared consent choices, filtered by deployment and organization
    policy.
    """

    browse_scope_tiers: Optional[List[str]] = None
    """Exact enabled tiers accepted by the adapter browse policy."""

    resource_types: Optional[List[str]] = None

    scope_tier: Optional[str] = None

    search: Optional[ProviderSearch] = None
    """Present when GET /connections/{id}/search works for this provider."""

    supports_create_folder: Optional[bool] = None
    """True when POST /connections/{id}/folders can create folders for this provider."""

    supports_export: Optional[bool] = None


class ConnectionListResponse(BaseModel):
    capabilities: Optional[Capabilities] = None

    connections: Optional[List[Connection]] = None

    cursor: Optional[str] = None
    """Mirror of `pagination.next_cursor`. Prefer `pagination`."""

    pagination: Optional[Pagination] = None

    providers: Optional[List[Provider]] = None
    """Available import providers and their adapter-declared capabilities."""
