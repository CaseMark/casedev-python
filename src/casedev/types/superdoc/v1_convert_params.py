# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1ConvertParams"]


class V1ConvertParams(TypedDict, total=False):
    from_: Required[Annotated[Literal["docx", "md", "html"], PropertyInfo(alias="from")]]
    """Source format of the document"""

    document_base64: str
    """Base64-encoded document content"""

    document_url: str
    """URL to the document to convert"""

    to: Literal["pdf", "docx"]
    """Target format for conversion"""
