# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ObjectDeleteParams"]


class ObjectDeleteParams(TypedDict, total=False):
    id: Required[str]

    force: Literal["true"]
    """Force delete a stuck document that is still in 'processing' state.

    Use this if a document got stuck during ingestion (e.g., OCR timeout).
    """
