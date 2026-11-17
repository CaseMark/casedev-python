# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ConnectionCreateParams"]


class ConnectionCreateParams(TypedDict, total=False):
    provider: Required[Literal["box", "clio", "dropbox", "gdrive", "microsoft", "sharefile", "smokeball"]]

    return_url: Required[str]
    """HTTPS URL the user is sent back to after consent."""

    scope_tier: Literal[
        "box.readwrite",
        "box.readwrite.webhooks",
        "clio.us",
        "dropbox.readwrite",
        "drive",
        "microsoft.account.read",
        "microsoft.read",
        "microsoft.personal.read",
        "microsoft.write",
        "microsoft.personal.write",
        "sharefile",
        "smokeball.us",
        "smokeball.us.staging",
        "smokeball.us.staging.write",
        "smokeball.us.write",
    ]
    """Provider-specific OAuth permission tier.

    Omit to use the provider's default. Use microsoft.account.read to let Microsoft
    choose a personal or work/school account. Existing explicit microsoft.read and
    microsoft.personal.read tiers remain supported. Microsoft write tiers require
    the separate write switch and explicit authorization for bounded exports and
    paired sync.
    """

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
