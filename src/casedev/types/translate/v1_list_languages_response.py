# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["V1ListLanguagesResponse", "Data", "DataLanguage"]


class DataLanguage(BaseModel):
    language: Optional[str] = None
    """Language code (ISO 639-1)"""

    name: Optional[str] = None
    """Language name (if target specified)"""


class Data(BaseModel):
    languages: Optional[List[DataLanguage]] = None


class V1ListLanguagesResponse(BaseModel):
    data: Optional[Data] = None
