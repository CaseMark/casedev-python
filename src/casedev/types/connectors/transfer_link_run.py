# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TransferLinkRun"]


class TransferLinkRun(BaseModel):
    link_id: str

    started: bool

    backlog: Optional[int] = None

    reason: Optional[Literal["stale_run_recovery", "already_running", "ingestion_backlog"]] = None
