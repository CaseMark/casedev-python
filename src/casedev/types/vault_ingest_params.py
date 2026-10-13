# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["VaultIngestParams"]


class VaultIngestParams(TypedDict, total=False):
    id: Required[str]

    callback_url: str
    """Optional callback URL for asynchronous workflow completion."""

    page_boundaries: Iterable[int]
    """Optional PDF pages that must begin a new chunk segment.

    Overlap never crosses these boundaries.
    """
