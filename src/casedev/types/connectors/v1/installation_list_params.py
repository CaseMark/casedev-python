# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InstallationListParams"]


class InstallationListParams(TypedDict, total=False):
    application: str

    external_tenant_id: str
