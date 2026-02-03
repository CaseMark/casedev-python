# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["V1TranslateParams"]


class V1TranslateParams(TypedDict, total=False):
    q: Required[Union[str, SequenceNotStr[str]]]
    """Text to translate. Can be a single string or an array for batch translation."""

    target: Required[str]
    """Target language code (ISO 639-1)"""

    format: Literal["text", "html"]
    """Format of the source text. Use 'html' to preserve HTML tags."""

    model: Literal["nmt", "base"]
    """Translation model.

    'nmt' (Neural Machine Translation) is recommended for quality.
    """

    source: str
    """Source language code (ISO 639-1). If not specified, language is auto-detected."""
