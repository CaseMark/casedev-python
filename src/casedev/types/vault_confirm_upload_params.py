# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["VaultConfirmUploadParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    id: Required[str]

    size_bytes: Required[Annotated[int, PropertyInfo(alias="sizeBytes")]]
    """Uploaded file size in bytes (required when success=true)"""

    success: Required[Literal[True]]

    error_code: Annotated[str, PropertyInfo(alias="errorCode")]
    """Client-side error code (required when success=false)"""

    error_message: Annotated[str, PropertyInfo(alias="errorMessage")]
    """Client-side error message (required when success=false)"""

    etag: str
    """S3 ETag for the uploaded object (optional if client cannot access ETag header)"""


class Variant1(TypedDict, total=False):
    id: Required[str]

    error_code: Required[Annotated[str, PropertyInfo(alias="errorCode")]]
    """Client-side error code (required when success=false)"""

    error_message: Required[Annotated[str, PropertyInfo(alias="errorMessage")]]
    """Client-side error message (required when success=false)"""

    success: Required[Literal[False]]

    etag: str
    """S3 ETag for the uploaded object (optional if client cannot access ETag header)"""

    size_bytes: Annotated[int, PropertyInfo(alias="sizeBytes")]
    """Uploaded file size in bytes (required when success=true)"""


VaultConfirmUploadParams: TypeAlias = Union[Variant0, Variant1]
