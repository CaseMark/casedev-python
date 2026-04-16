# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["V1RetrieveParams"]


class V1RetrieveParams(TypedDict, total=False):
    include_text: Literal["true", "false"]
    """Include full OCR text in completed responses (default: true)"""
