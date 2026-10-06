# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .transfer_run import TransferRun
from .transfer_link_run import TransferLinkRun

__all__ = ["V1TransferResponse"]


class V1TransferResponse(BaseModel):
    links: Optional[List[object]] = None

    run: Optional[TransferRun] = None
    """Whether a provider scan started or was deferred."""

    runs: Optional[List[TransferLinkRun]] = None
    """Start result for each link when direction is both."""
