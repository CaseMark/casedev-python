# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ObjectOrganizeParams", "Variant0", "Variant1", "Variant1Move"]


class Variant0(TypedDict, total=False):
    object_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="objectIds")]]

    path: Required[str]

    expected_paths: Annotated[Dict[str, str], PropertyInfo(alias="expectedPaths")]
    """Optional current folder preconditions for the supplied object IDs only.

    Automatically included transcription results do not require entries; supplied
    result entries are checked.
    """


class Variant1(TypedDict, total=False):
    moves: Required[Iterable[Variant1Move]]
    """Restore confirmed move receipts with optimistic concurrency checks.

    Include every receipt for each media/transcription family. Cannot combine with
    objectIds or path.
    """


class Variant1Move(TypedDict, total=False):
    id: Required[str]

    expected_path: Required[Annotated[str, PropertyInfo(alias="expectedPath")]]

    path: Required[str]


ObjectOrganizeParams: TypeAlias = Union[Variant0, Variant1]
