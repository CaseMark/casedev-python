# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["V1ListEnvVarsParams"]


class V1ListEnvVarsParams(TypedDict, total=False):
    environment: Literal["production", "preview", "development", "shared"]
