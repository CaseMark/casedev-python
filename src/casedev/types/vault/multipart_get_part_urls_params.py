# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MultipartGetPartURLsParams", "Part"]


class MultipartGetPartURLsParams(TypedDict, total=False):
    object_id: Required[Annotated[str, PropertyInfo(alias="objectId")]]

    parts: Required[Iterable[Part]]

    upload_id: Required[Annotated[str, PropertyInfo(alias="uploadId")]]


class Part(TypedDict, total=False):
    part_number: Required[Annotated[int, PropertyInfo(alias="partNumber")]]

    size_bytes: Required[Annotated[int, PropertyInfo(alias="sizeBytes")]]
    """Part size in bytes (min 5MB except final part, max 5GB)."""
