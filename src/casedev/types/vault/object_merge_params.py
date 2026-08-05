# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ObjectMergeParams", "Bates"]


class ObjectMergeParams(TypedDict, total=False):
    filename: Required[str]
    """Output PDF filename"""

    source_object_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="sourceObjectIds")]]
    """Source object IDs in output order"""

    source_rendition: Required[Annotated[Literal["original", "searchable_pdf"], PropertyInfo(alias="sourceRendition")]]

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    bates: Bates

    client_reference: Annotated[str, PropertyInfo(alias="clientReference")]


class Bates(TypedDict, total=False):
    pad_to: Annotated[int, PropertyInfo(alias="padTo")]

    prefix: str

    start: int

    suffix: str
