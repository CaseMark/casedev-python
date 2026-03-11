# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MultipartAbortParams"]


class MultipartAbortParams(TypedDict, total=False):
    object_id: Required[Annotated[str, PropertyInfo(alias="objectId")]]
    """Vault object ID associated with the multipart upload"""

    upload_id: Required[Annotated[str, PropertyInfo(alias="uploadId")]]
    """Multipart upload ID returned when the upload was initialized"""
