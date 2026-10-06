# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["SessionReplaceScopeParams", "VaultScope"]


class SessionReplaceScopeParams(TypedDict, total=False):
    vault_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="vaultIds")]
    """Legacy whole-vault scope. Mutually exclusive with vaultScopes."""

    vault_scopes: Annotated[Iterable[VaultScope], PropertyInfo(alias="vaultScopes")]
    """Authoritative object allowlist for the next and later turns."""


class VaultScope(TypedDict, total=False):
    object_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="objectIds")]]

    vault_id: Required[Annotated[str, PropertyInfo(alias="vaultId")]]
