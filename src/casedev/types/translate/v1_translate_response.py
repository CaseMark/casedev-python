# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1TranslateResponse", "Data", "DataTranslation"]


class DataTranslation(BaseModel):
    detected_source_language: Optional[str] = FieldInfo(alias="detectedSourceLanguage", default=None)
    """Detected source language (if source not specified)"""

    model: Optional[str] = None
    """Model used for translation"""

    translated_text: Optional[str] = FieldInfo(alias="translatedText", default=None)
    """Translated text"""


class Data(BaseModel):
    translations: Optional[List[DataTranslation]] = None


class V1TranslateResponse(BaseModel):
    data: Optional[Data] = None
