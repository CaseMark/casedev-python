# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BoostListExtractParams"]


class BoostListExtractParams(TypedDict, total=False):
    categories: List[Literal["person", "organization", "legal_term", "medical", "citation", "email"]]
    """Optional filter for entity categories to extract"""

    object_ids: SequenceNotStr[str]
    """Object IDs of documents to extract entities from (PDFs, text files)"""

    text: str
    """Raw text input for entity extraction (alternative to vault documents)"""

    vault_id: str
    """Vault ID containing the source documents (use with object_ids)"""
