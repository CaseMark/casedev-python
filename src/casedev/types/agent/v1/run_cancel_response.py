# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["RunCancelResponse"]


class RunCancelResponse(BaseModel):
    id: Optional[str] = None

    message: Optional[str] = None
    """Present if run was already finished"""

    status: Optional[Literal["cancelled", "completed", "failed"]] = None
