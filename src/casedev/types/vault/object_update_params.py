# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ObjectUpdateParams"]


class ObjectUpdateParams(TypedDict, total=False):
    id: Required[str]

    filename: str
    """New filename for the document (affects display name and downloads)"""

    metadata: object
    """Additional metadata to merge with existing metadata"""

    path: Optional[str]
    """Folder path for hierarchy preservation (e.g., '/Discovery/Depositions').

    Set to null or empty string to remove.
    """
