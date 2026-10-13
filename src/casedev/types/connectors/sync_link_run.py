# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SyncLinkRun"]


class SyncLinkRun(BaseModel):
    """Whether a provider scan started or was deferred."""

    started: bool

    backlog: Optional[int] = None

    reason: Optional[Literal["stale_run_recovery", "already_running", "ingestion_backlog"]] = None
