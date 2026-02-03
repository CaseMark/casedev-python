# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V1GetCitationsFromURLParams"]


class V1GetCitationsFromURLParams(TypedDict, total=False):
    url: Required[str]
    """URL of the legal document to extract citations from"""
