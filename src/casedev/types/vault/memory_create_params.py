# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MemoryCreateParams"]


class MemoryCreateParams(TypedDict, total=False):
    content: Required[str]

    type: Required[Literal["fact", "party", "issue", "deadline", "discovery", "correction", "preference"]]

    source: str

    tags: SequenceNotStr[str]
