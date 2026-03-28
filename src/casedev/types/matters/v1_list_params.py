# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V1ListParams"]


class V1ListParams(TypedDict, total=False):
    matter_type: str

    practice_area: str

    query: str

    status: str
