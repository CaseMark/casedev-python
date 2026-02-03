# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["V1DetectResponse", "Category"]


class Category(BaseModel):
    confidence: Optional[float] = None
    """Confidence for this category (0-1)"""

    detected: Optional[bool] = None
    """Whether this privilege type was detected"""

    indicators: Optional[List[str]] = None
    """Specific phrases or patterns found"""

    rationale: Optional[str] = None
    """Explanation of detection result"""

    type: Optional[str] = None
    """Privilege category"""


class V1DetectResponse(BaseModel):
    categories: List[Category]

    confidence: float
    """Overall confidence score (0-1)"""

    policy_rationale: str
    """Policy-friendly explanation for privilege log"""

    privileged: bool
    """Whether any privilege was detected"""

    recommendation: Literal["withhold", "redact", "produce", "review"]
    """Recommended action for discovery"""
