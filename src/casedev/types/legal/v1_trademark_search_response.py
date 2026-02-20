# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1TrademarkSearchResponse", "GoodsAndService", "Owner"]


class GoodsAndService(BaseModel):
    class_number: Optional[str] = FieldInfo(alias="classNumber", default=None)

    description: Optional[str] = None


class Owner(BaseModel):
    """Current owner/applicant information"""

    address: Optional[str] = None

    entity_type: Optional[str] = FieldInfo(alias="entityType", default=None)

    name: Optional[str] = None


class V1TrademarkSearchResponse(BaseModel):
    attorney: Optional[str] = None
    """Attorney of record"""

    filing_date: Optional[date] = FieldInfo(alias="filingDate", default=None)
    """Date the application was filed"""

    goods_and_services: Optional[List[GoodsAndService]] = FieldInfo(alias="goodsAndServices", default=None)
    """Goods and services descriptions with class numbers"""

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)
    """URL to the mark image on USPTO CDN"""

    mark_text: Optional[str] = FieldInfo(alias="markText", default=None)
    """The text of the trademark"""

    mark_type: Optional[str] = FieldInfo(alias="markType", default=None)
    """Type of mark (e.g. "Standard Character Mark", "Design Mark")"""

    nice_classes: Optional[List[int]] = FieldInfo(alias="niceClasses", default=None)
    """Nice classification class numbers"""

    owner: Optional[Owner] = None
    """Current owner/applicant information"""

    registration_date: Optional[date] = FieldInfo(alias="registrationDate", default=None)
    """Date the mark was registered"""

    registration_number: Optional[str] = FieldInfo(alias="registrationNumber", default=None)
    """USPTO registration number (if registered)"""

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """USPTO serial number"""

    status: Optional[str] = None
    """Current status (e.g. "Registered", "Pending", "Abandoned", "Cancelled")"""

    status_date: Optional[date] = FieldInfo(alias="statusDate", default=None)
    """Date of most recent status update"""

    uspto_url: Optional[str] = FieldInfo(alias="usptoUrl", default=None)
    """Canonical TSDR link for this mark"""
