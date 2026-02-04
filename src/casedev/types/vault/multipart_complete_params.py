# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MultipartCompleteParams", "Part"]


class MultipartCompleteParams(TypedDict, total=False):
    object_id: Required[Annotated[str, PropertyInfo(alias="objectId")]]

    parts: Required[Iterable[Part]]

    size_bytes: Required[Annotated[int, PropertyInfo(alias="sizeBytes")]]

    upload_id: Required[Annotated[str, PropertyInfo(alias="uploadId")]]


class Part(TypedDict, total=False):
    etag: Required[str]

    part_number: Required[Annotated[int, PropertyInfo(alias="partNumber")]]
