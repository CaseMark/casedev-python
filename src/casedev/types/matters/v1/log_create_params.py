# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["LogCreateParams"]


class LogCreateParams(TypedDict, total=False):
    summary: Required[str]

    details: Dict[str, object]

    event_type: str

    work_item_id: str
