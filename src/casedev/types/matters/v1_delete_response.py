# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["V1DeleteResponse", "Counts"]


class Counts(BaseModel):
    chats: Optional[int] = None

    objects: Optional[int] = None

    sessions: Optional[int] = None

    transcriptions: Optional[int] = None


class V1DeleteResponse(BaseModel):
    attempt: int

    matter_id: str

    purge_id: str

    status: Literal["queued", "in_progress", "failed", "completed"]

    vault_id: str

    workflow_id: Optional[str] = None

    completed_at: Optional[datetime] = None

    counts: Optional[Counts] = None

    failed_at: Optional[datetime] = None

    failure_code: Optional[str] = None

    requested_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

    terminal_event_id: Optional[str] = None
    """Stable ID of the failed or completed terminal webhook event"""
