# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["V1ListJurisdictionsResponse", "Jurisdiction"]


class Jurisdiction(BaseModel):
    id: Optional[str] = None
    """Jurisdiction ID to use in other endpoints"""

    level: Optional[Literal["federal", "state", "county", "municipal"]] = None
    """Jurisdiction level"""

    name: Optional[str] = None
    """Full jurisdiction name"""

    state: Optional[str] = None
    """State abbreviation (if applicable)"""


class V1ListJurisdictionsResponse(BaseModel):
    found: Optional[int] = None
    """Number of matching jurisdictions"""

    hint: Optional[str] = None
    """Usage guidance"""

    jurisdictions: Optional[List[Jurisdiction]] = None

    query: Optional[str] = None
    """Original search query"""
