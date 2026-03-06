# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["V1DraftParams", "Length"]


class V1DraftParams(TypedDict, total=False):
    instructions: Required[str]
    """What to draft — the core task.

    E.g., "Motion to compel defendant to produce discovery responses"
    """

    vault_id: Required[str]
    """Vault ID where the final document will be uploaded"""

    citations: bool
    """Research and include legal citations"""

    format: Optional[str]
    """Court or jurisdiction formatting hint.

    Triggers a legal-skills search. E.g., "California Superior Court", "SDNY",
    "federal pleading"
    """

    length: Optional[Length]
    """Target document length"""

    model: Optional[str]
    """LLM model override. Defaults to anthropic/claude-sonnet-4.6"""

    object_ids: Optional[SequenceNotStr[str]]
    """Vault object IDs to use as source/reference documents"""

    output_name: Optional[str]
    """Filename for the output document. Auto-generated if omitted."""

    output_type: Literal["pdf", "docx", "xlsx", "pptx", "md"]
    """Output file format"""

    verified: bool
    """
    Verify all citations in a loop — re-run verification and repair bad citations
    until they pass
    """


class Length(TypedDict, total=False):
    """Target document length"""

    target: float
    """Target value (e.g., 2000 words or 5 pages)"""

    unit: Literal["words", "pages"]
