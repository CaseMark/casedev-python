# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VaultConfirmUploadParams"]


class VaultConfirmUploadParams(TypedDict, total=False):
    id: Required[str]

    success: Required[bool]
    """Whether the upload succeeded"""

    auto_ingest: Annotated[bool, PropertyInfo(alias="autoIngest")]
    """
    When true and the object was uploaded with auto_index, trigger ingestion
    immediately after a successful confirmation (no separate ingest call needed).
    The ingest outcome is reported in the `ingest` response field; an ingest failure
    does not fail the confirmation.
    """

    error_code: Annotated[str, PropertyInfo(alias="errorCode")]
    """Client-side error code. Required when success=false."""

    error_message: Annotated[str, PropertyInfo(alias="errorMessage")]
    """Client-side error message. Required when success=false."""

    etag: str
    """S3 ETag for the uploaded object (optional if client cannot access ETag header).

    Only meaningful when success=true.
    """

    size_bytes: Annotated[int, PropertyInfo(alias="sizeBytes")]
    """Uploaded file size in bytes. Required when success=true."""
