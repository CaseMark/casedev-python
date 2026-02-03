# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["V1CreateResponse", "Result"]


class Result(BaseModel):
    id: Optional[str] = None
    """Memory ID"""

    event: Optional[Literal["ADD", "UPDATE", "DELETE", "NONE"]] = None
    """What happened to this memory"""

    memory: Optional[str] = None
    """Extracted memory text"""


class V1CreateResponse(BaseModel):
    results: Optional[List[Result]] = None
