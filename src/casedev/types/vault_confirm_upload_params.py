# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["VaultConfirmUploadParams", "VaultConfirmUploadSuccess", "VaultConfirmUploadFailure"]


class VaultConfirmUploadSuccess(TypedDict, total=False):
    id: Required[str]

    size_bytes: Required[Annotated[int, PropertyInfo(alias="sizeBytes")]]
    """Uploaded file size in bytes"""

    success: Required[Literal[True]]
    """Whether the upload succeeded"""

    etag: str
    """S3 ETag for the uploaded object (optional if client cannot access ETag header)"""


class VaultConfirmUploadFailure(TypedDict, total=False):
    id: Required[str]

    error_code: Required[Annotated[str, PropertyInfo(alias="errorCode")]]
    """Client-side error code"""

    error_message: Required[Annotated[str, PropertyInfo(alias="errorMessage")]]
    """Client-side error message"""

    success: Required[Literal[False]]
    """Whether the upload succeeded"""


VaultConfirmUploadParams: TypeAlias = Union[VaultConfirmUploadSuccess, VaultConfirmUploadFailure]
