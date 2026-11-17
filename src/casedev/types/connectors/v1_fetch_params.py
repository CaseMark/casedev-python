# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1FetchParams"]


class V1FetchParams(TypedDict, total=False):
    open_ref: Required[str]
    """From a browse item, exactly as received"""

    upload_url: str
    """Presigned HTTPS S3 PUT URL.

    Content-Type must not be a signed header. Exactly one destination.
    """

    vault_id: str
    """Destination Vault. Exactly one destination."""

    x_case_connector_subject: Annotated[str, PropertyInfo(alias="x-case-connector-subject")]
