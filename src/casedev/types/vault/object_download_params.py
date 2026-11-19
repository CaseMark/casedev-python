# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ObjectDownloadParams"]


class ObjectDownloadParams(TypedDict, total=False):
    id: Required[str]

    format: Literal["original", "pdf"]
    """original (default) returns the file as uploaded.

    pdf returns a spreadsheet's PDF version, or a PDF as usual.
    """
