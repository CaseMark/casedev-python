# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["V1DraftResponse"]


class V1DraftResponse(BaseModel):
    agent_id: Optional[str] = None
    """Ephemeral agent ID"""

    message: Optional[str] = None

    run_id: Optional[str] = None
    """Run ID — poll /agent/v1/run/:id/status for progress"""

    status: Optional[Literal["running"]] = None
