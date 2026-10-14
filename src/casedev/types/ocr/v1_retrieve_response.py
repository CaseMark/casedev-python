# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["V1RetrieveResponse", "FailedChunk"]


class FailedChunk(BaseModel):
    chunk_id: Optional[str] = None

    error: Optional[str] = None

    error_code: Optional[str] = None

    error_stage: Optional[str] = None

    page_end: Optional[int] = None

    page_start: Optional[int] = None

    retryable: Optional[bool] = None


class V1RetrieveResponse(BaseModel):
    id: str
    """OCR job ID"""

    created_at: datetime
    """Job creation timestamp"""

    status: Literal["pending", "processing", "completed", "failed"]
    """Current job status"""

    chunk_count: Optional[int] = None
    """Total number of OCR chunks."""

    chunks_failed: Optional[int] = None
    """Exact number of failed OCR chunks."""

    completed_at: Optional[datetime] = None
    """Job completion timestamp"""

    error: Optional[str] = None
    """Safe human-readable failure message; null when no failure is recorded."""

    error_code: Optional[str] = None
    """
    Stable failure identifier, such as source_access_denied, invalid_pdf,
    inference_failed, chunks_failed, or result_upload_failed. Historic failures may
    be unclassified.
    """

    error_stage: Optional[
        Literal[
            "dispatch",
            "download",
            "document_validation",
            "chunking",
            "engine_init",
            "inference",
            "feature_processing",
            "result_write",
            "chunk_processing",
            "result_assembly",
            "result_upload",
        ]
    ] = None
    """Operation that failed."""

    failed_chunks: Optional[List[FailedChunk]] = None
    """Bounded failure samples.

    Page ranges are one-based and inclusive; chunks_failed and chunk_count retain
    exact totals.
    """

    metadata: Optional[object] = None
    """Additional processing metadata"""

    page_count: Optional[int] = None
    """Number of pages processed"""

    retryable: Optional[bool] = None
    """Whether retrying the same document may help.

    Unknown failures retain bounded retry behavior.
    """

    text: Optional[str] = None
    """Extracted text content when completed and include_text=true"""
