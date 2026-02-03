# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1DetectResponse", "Data", "DataDetection"]


class DataDetection(BaseModel):
    confidence: Optional[float] = None
    """Confidence score (0-1)"""

    is_reliable: Optional[bool] = FieldInfo(alias="isReliable", default=None)
    """Whether the detection is reliable"""

    language: Optional[str] = None
    """Detected language code (ISO 639-1)"""


class Data(BaseModel):
    detections: Optional[List[List[DataDetection]]] = None


class V1DetectResponse(BaseModel):
    data: Optional[Data] = None
