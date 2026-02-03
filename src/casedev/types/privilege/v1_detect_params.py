# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["V1DetectParams"]


class V1DetectParams(TypedDict, total=False):
    categories: List[Literal["attorney_client", "work_product", "common_interest", "litigation_hold"]]
    """Privilege categories to check.

    Defaults to all: attorney_client, work_product, common_interest, litigation_hold
    """

    content: str
    """Text content to analyze (required if document_id not provided)"""

    document_id: str
    """Vault object ID to analyze (required if content not provided)"""

    include_rationale: bool
    """Include detailed rationale for each category"""

    jurisdiction: Literal["US-Federal"]
    """Jurisdiction for privilege rules"""

    model: str
    """LLM model to use for analysis"""

    vault_id: str
    """Vault ID (required when using document_id)"""
