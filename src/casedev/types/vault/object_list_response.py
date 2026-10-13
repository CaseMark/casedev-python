# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectListResponse", "Object", "Pagination", "Totals"]


class Object(BaseModel):
    id: str
    """Unique object identifier"""

    content_type: str = FieldInfo(alias="contentType")
    """MIME type of the document"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Document upload timestamp"""

    filename: str
    """Original filename of the uploaded document"""

    ingestion_status: str = FieldInfo(alias="ingestionStatus")
    """Processing status of the document"""

    chunk_count: Optional[float] = FieldInfo(alias="chunkCount", default=None)
    """Number of text chunks created for vectorization"""

    file_origin: Optional[Dict[str, object]] = None
    """Client-defined provenance metadata associated with the file"""

    ingestion_completed_at: Optional[datetime] = FieldInfo(alias="ingestionCompletedAt", default=None)
    """Processing completion timestamp"""

    ingestion_error: Optional[str] = FieldInfo(alias="ingestionError", default=None)
    """Failure reason when ingestion status is a failed state"""

    ingestion_started_at: Optional[datetime] = FieldInfo(alias="ingestionStartedAt", default=None)
    """When ingestion processing began"""

    ingestion_workflow_id: Optional[str] = FieldInfo(alias="ingestionWorkflowId", default=None)
    """Durable workflow run ID for the active or last ingestion attempt.

    Null while a dispatch claim is being reconciled or when no workflow applies.
    """

    is_ai_generated: Optional[bool] = None
    """Whether the file was marked as AI-generated work product at upload time"""

    metadata: Optional[object] = None
    """Custom metadata associated with the document"""

    page_count: Optional[float] = FieldInfo(alias="pageCount", default=None)
    """Number of pages in the document"""

    path: Optional[str] = None
    """Optional folder path for hierarchy preservation from source systems"""

    size_bytes: Optional[float] = FieldInfo(alias="sizeBytes", default=None)
    """File size in bytes"""

    tags: Optional[List[str]] = None
    """Custom tags associated with the document"""

    text_length: Optional[float] = FieldInfo(alias="textLength", default=None)
    """Total character count of extracted text"""

    vector_count: Optional[float] = FieldInfo(alias="vectorCount", default=None)
    """Number of vectors generated for semantic search"""


class Pagination(BaseModel):
    has_more: bool
    """Whether more objects exist beyond this page."""

    limit: Optional[int] = None
    """Page size applied, or null when every object was returned."""

    next_cursor: Optional[str] = None
    """Pass as `cursor` to fetch the next page. Null on the final page."""


class Totals(BaseModel):
    """Present only with `include_totals=true`.

    Covers every object matching the filters, across all pages.
    """

    objects: Optional[int] = None
    """Number of matching objects"""

    total_bytes: Optional[float] = FieldInfo(alias="totalBytes", default=None)
    """Combined size of matching objects"""


class ObjectListResponse(BaseModel):
    count: float
    """Number of objects in this response.

    Equals the vault total only when `pagination.has_more` is false; use
    `totals.objects` for the total across pages.
    """

    objects: List[Object]

    pagination: Pagination

    vault_id: str = FieldInfo(alias="vaultId")
    """The ID of the vault"""

    totals: Optional[Totals] = None
    """Present only with `include_totals=true`.

    Covers every object matching the filters, across all pages.
    """
