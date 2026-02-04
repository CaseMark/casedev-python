# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MultipartInitParams"]


class MultipartInitParams(TypedDict, total=False):
    content_type: Required[Annotated[str, PropertyInfo(alias="contentType")]]
    """MIME type of the file"""

    filename: Required[str]
    """Name of the file to upload"""

    size_bytes: Required[Annotated[int, PropertyInfo(alias="sizeBytes")]]
    """File size in bytes (required, max 8GB)."""

    auto_index: bool
    """Whether to automatically process and index the file for search"""

    metadata: object
    """Additional metadata to associate with the file"""

    part_size_bytes: Annotated[int, PropertyInfo(alias="partSizeBytes")]
    """Multipart part size in bytes (min 5MB). Defaults to 64MB."""

    path: str
    """Optional folder path for hierarchy preservation"""
