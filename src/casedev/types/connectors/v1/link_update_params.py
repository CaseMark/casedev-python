# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LinkUpdateParams"]


class LinkUpdateParams(TypedDict, total=False):
    mode: Literal["once", "synced"]

    policy: object

    state: Literal["paused", "ready"]
