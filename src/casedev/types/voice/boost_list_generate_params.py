# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BoostListGenerateParams"]


class BoostListGenerateParams(TypedDict, total=False):
    transcription_job_id: Required[str]
    """Completed pass-1 transcription job ID (tr\\__...)"""

    categories: List[Literal["person", "organization", "legal_term", "medical", "citation", "email"]]
    """Optional filter for entity categories to extract"""
