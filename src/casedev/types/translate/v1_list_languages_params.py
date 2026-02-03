# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["V1ListLanguagesParams"]


class V1ListLanguagesParams(TypedDict, total=False):
    model: Literal["nmt", "base"]
    """Translation model to check language support for"""

    target: str
    """
    Target language code for translating language names (e.g., 'es' for Spanish
    names)
    """
