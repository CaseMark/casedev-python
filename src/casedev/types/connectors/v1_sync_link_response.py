# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .sync_link_run import SyncLinkRun
from .sync_link_link_run import SyncLinkLinkRun

__all__ = ["V1SyncLinkResponse"]


class V1SyncLinkResponse(BaseModel):
    links: Optional[List[object]] = None

    run: Optional[SyncLinkRun] = None
    """Whether a provider scan started or was deferred."""

    runs: Optional[List[SyncLinkLinkRun]] = None
    """Start result for each link when direction is both."""
