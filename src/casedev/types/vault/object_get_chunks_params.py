# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ObjectGetChunksParams"]


class ObjectGetChunksParams(TypedDict, total=False):
    id: Required[str]

    end: int
    """The last chunk index to return (inclusive).

    If omitted, only the `start` chunk is returned. Ranges are limited to 10 chunks.
    """

    start: int
    """The first chunk index to return (0-based). Defaults to 0."""
