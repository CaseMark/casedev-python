# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V1VerifyParams"]


class V1VerifyParams(TypedDict, total=False):
    text: Required[str]
    """Text containing citations to verify.

    Can be a single citation (e.g., "531 U.S. 98") or a full document with multiple
    citations.
    """
