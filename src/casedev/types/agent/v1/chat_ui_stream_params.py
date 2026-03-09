# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ChatUiStreamParams"]


class ChatUiStreamParams(TypedDict, total=False):
    body: Required[object]
    """OpenCode message payload. Passed through 1:1."""
