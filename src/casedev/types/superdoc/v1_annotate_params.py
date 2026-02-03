# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["V1AnnotateParams", "Document", "Field", "FieldOptions"]


class V1AnnotateParams(TypedDict, total=False):
    document: Required[Document]
    """Document source - provide either URL or base64"""

    fields: Required[Iterable[Field]]
    """Fields to populate in the template"""

    output_format: Literal["docx", "pdf"]
    """Output format for the annotated document"""


class Document(TypedDict, total=False):
    """Document source - provide either URL or base64"""

    base64: str
    """Base64-encoded DOCX template"""

    url: str
    """URL to the DOCX template"""


class FieldOptions(TypedDict, total=False):
    """Optional configuration (e.g., image dimensions)"""

    height: float
    """Image height in pixels"""

    width: float
    """Image width in pixels"""


class Field(TypedDict, total=False):
    type: Required[Literal["text", "image", "date", "number"]]
    """Field data type"""

    value: Required[Union[str, float]]
    """Value to populate"""

    id: str
    """Target field ID (for single field)"""

    group: str
    """Target field group (for multiple fields with same tag)"""

    options: FieldOptions
    """Optional configuration (e.g., image dimensions)"""
