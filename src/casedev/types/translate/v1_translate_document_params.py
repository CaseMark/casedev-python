# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["V1TranslateDocumentParams"]


class V1TranslateDocumentParams(TypedDict, total=False):
    file: Required[FileTypes]
    """TXT, DOCX, or searchable PDF document (max 20MB)"""

    target: Required[str]
    """Target BCP-47 language code"""

    source: str
    """Optional source BCP-47 language code. Auto-detected when omitted."""
