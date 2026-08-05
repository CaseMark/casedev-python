# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["V1SyncLinkParams", "Remote", "Policy", "PolicyFilters"]


class V1SyncLinkParams(TypedDict, total=False):
    connection_id: Required[str]

    direction: Required[Literal["import", "export"]]

    remote: Required[Remote]

    vault_id: Required[str]

    matter_id: Optional[str]

    policy: Policy


class Remote(TypedDict, total=False):
    folder_id: Required[str]

    container_id: str

    path: str

    site_id: str


class PolicyFilters(TypedDict, total=False):
    exclude_mime: SequenceNotStr[str]

    max_size_bytes: int


class Policy(TypedDict, total=False):
    collisions: Literal["version", "overwrite", "skip"]

    deletes: Literal["mirror", "preserve"]

    filters: PolicyFilters
