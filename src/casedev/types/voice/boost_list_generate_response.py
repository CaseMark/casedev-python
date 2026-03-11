# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BoostListGenerateResponse", "Item"]


class Item(BaseModel):
    boost_param: Optional[Literal["low", "default", "high"]] = None

    category: Optional[str] = None

    word: Optional[str] = None


class BoostListGenerateResponse(BaseModel):
    items: Optional[List[Item]] = None

    source: Optional[Literal["transcript"]] = None

    source_ids: Optional[List[str]] = None
