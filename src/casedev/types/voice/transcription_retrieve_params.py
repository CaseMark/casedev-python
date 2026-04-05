# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TranscriptionRetrieveParams"]


class TranscriptionRetrieveParams(TypedDict, total=False):
    include_text: Literal["true", "false"]
    """Include full transcript text in response for vault-based jobs (default: false)"""
