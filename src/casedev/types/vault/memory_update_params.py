# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MemoryUpdateParams"]


class MemoryUpdateParams(TypedDict, total=False):
    id: Required[str]

    content: str

    source: Optional[str]

    tags: SequenceNotStr[str]
