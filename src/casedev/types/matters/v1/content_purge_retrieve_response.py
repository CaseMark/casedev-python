# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ContentPurgeRetrieveResponse"]


class ContentPurgeRetrieveResponse(BaseModel):
    attempt: int

    matter_id: str

    purge_id: str

    request_id: str

    status: Literal["queued", "in_progress", "failed", "completed"]

    vault_id: str

    workflow_id: Optional[str] = None

    completed_at: Optional[datetime] = None

    counts: Optional[Dict[str, int]] = None

    failed_at: Optional[datetime] = None

    failure_code: Optional[str] = None

    requested_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

    terminal_event_id: Optional[str] = None
