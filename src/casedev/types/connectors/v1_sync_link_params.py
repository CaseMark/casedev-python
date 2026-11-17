# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["V1SyncLinkParams", "Remote", "ExportDestination", "Policy", "PolicyFilters", "Selection"]


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

    selection: Selection
    """
    Export only part of the vault (direction export only; 400
    selection_requires_export otherwise). Provide object_ids, folder, or both (their
    intersection). The selection is part of link identity: each distinct selection
    to the same destination is its own link, and repeating a selection re-runs that
    link. Exported objects still exclude files still processing and
    connector-imported or fetched copies. Destination paths: with folder, paths are
    relative to that folder, so its contents land directly in remote; with
    object_ids only, each object keeps its full vault path. Omit to export the whole
    vault.
    """

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
    allow_extensions: SequenceNotStr[str]
    """File extensions (e.g.

    ".exe") to import even though the engine skips Windows executables, libraries,
    installers and disc metadata by default.
    """

    exclude_file_ids: SequenceNotStr[str]
    """Skip these stable document ids before download, including future versions."""

    exclude_folder_ids: SequenceNotStr[str]
    """Skip these folders and all descendants during document imports."""

    exclude_mime: SequenceNotStr[str]

    max_size_bytes: int


class Policy(TypedDict, total=False):
    collisions: Literal["version", "overwrite", "skip"]
    """
    Export handling of a destination file with the same name that this export does
    not own. version keeps both: the export is written as name (CaseMark).ext, then
    name (CaseMark 2).ext, name (CaseMark 3).ext, using the first number the folder
    does not use (up to 100). overwrite replaces the existing file; skip leaves it.
    Any other value returns 400.
    """

    deletes: Literal["mirror", "preserve"]

    filters: PolicyFilters


class Selection(TypedDict, total=False):
    """
    Export only part of the vault (direction export only; 400 selection_requires_export otherwise). Provide object_ids, folder, or both (their intersection). The selection is part of link identity: each distinct selection to the same destination is its own link, and repeating a selection re-runs that link. Exported objects still exclude files still processing and connector-imported or fetched copies. Destination paths: with folder, paths are relative to that folder, so its contents land directly in remote; with object_ids only, each object keeps its full vault path. Omit to export the whole vault.
    """

    folder: str
    """Vault folder path such as /Reports/Final; includes every subfolder.

    The vault root is not a selection.
    """

    object_ids: SequenceNotStr[str]
    """Vault object ids from vault_id.

    Unknown ids return 400 selection_objects_not_found with data.error.count.
    """
