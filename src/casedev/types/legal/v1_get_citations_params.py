# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V1GetCitationsParams"]


class V1GetCitationsParams(TypedDict, total=False):
    text: Required[str]
    """Text containing citations to extract.

    Can be a single citation (e.g., "531 U.S. 98") or a full document with multiple
    citations.
    """
