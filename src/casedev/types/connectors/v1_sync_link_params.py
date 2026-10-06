# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["V1SyncLinkParams", "Remote", "ExportDestination", "Policy", "PolicyFilters"]


class V1SyncLinkParams(TypedDict, total=False):
    connection_id: Required[str]

    direction: Required[Literal["import", "export", "both"]]

    remote: Required[Remote]

    vault_id: Required[str]

    export_destination: ExportDestination
    """Optional destination for direction both.

    Defaults to CaseMark Output under remote.
    """

    matter_id: Optional[str]

    policy: Policy

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]


class Remote(TypedDict, total=False):
    folder_id: Required[str]

    container_id: str

    path: str

    resource_type: str

    site_id: str


class ExportDestination(TypedDict, total=False):
    """Optional destination for direction both.

    Defaults to CaseMark Output under remote.
    """

    folder_id: Required[str]

    container_id: str

    path: str

    site_id: str


class PolicyFilters(TypedDict, total=False):
    exclude_file_ids: SequenceNotStr[str]
    """Skip these stable document ids before download, including future versions."""

    exclude_folder_ids: SequenceNotStr[str]
    """Skip these folders and all descendants during document imports."""

    exclude_mime: SequenceNotStr[str]

    max_size_bytes: int


class Policy(TypedDict, total=False):
    collisions: Literal["version", "overwrite", "skip"]

    deletes: Literal["mirror", "preserve"]

    filters: PolicyFilters
