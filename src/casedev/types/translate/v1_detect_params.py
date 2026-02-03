# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["V1DetectParams"]


class V1DetectParams(TypedDict, total=False):
    q: Required[Union[str, SequenceNotStr[str]]]
    """Text to detect language for.

    Can be a single string or an array for batch detection.
    """
