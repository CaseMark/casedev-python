# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LinkUpdateParams"]


class LinkUpdateParams(TypedDict, total=False):
    expected_policy: object
    """Optional saved Clio import policy.

    Rejects concurrent changes to its folder/file exclusions.
    """

    expected_remote: object
    """
    Required saved remote when expanding a Clio import root; detects concurrent
    source changes.
    """

    mode: Literal["once", "synced"]

    policy: object
    """Replaces the entire stored policy; omitted fields return to defaults.

    Repeat deletes, collisions and filters that should be retained. Folder/file
    exclusions require deletes: preserve (the default).
    """

    remote: object
    """
    For unpaired Clio document imports only: expand folder_id to its verified Clio
    matter root. Connection, matter, vault and ledger remain unchanged.
    """

    state: Literal["paused", "ready"]

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
