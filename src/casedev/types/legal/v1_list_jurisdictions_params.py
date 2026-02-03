# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V1ListJurisdictionsParams"]


class V1ListJurisdictionsParams(TypedDict, total=False):
    name: Required[str]
    """Jurisdiction name (e.g., "California", "US Federal", "NY")"""
