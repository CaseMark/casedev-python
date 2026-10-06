# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ConnectionCreateParams"]


class ConnectionCreateParams(TypedDict, total=False):
    provider: Required[Literal["box", "clio", "dropbox", "gdrive", "microsoft", "smokeball"]]

    return_url: Required[str]
    """HTTPS URL the user is sent back to after consent."""

    scope_tier: Literal[
        "box.readwrite",
        "box.readwrite.webhooks",
        "clio.us",
        "dropbox.readwrite",
        "drive",
        "microsoft.read",
        "microsoft.personal.read",
        "microsoft.write",
        "microsoft.personal.write",
        "smokeball.us",
        "smokeball.us.staging",
    ]
    """Provider-specific OAuth permission tier.

    Omit to use the provider's default. Microsoft defaults to organizational
    OneDrive/SharePoint; use microsoft.personal.read for a personal Microsoft
    account's own OneDrive. Microsoft write tiers are a separately gated private
    pilot; exports and paired sync are not yet available.
    """

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
