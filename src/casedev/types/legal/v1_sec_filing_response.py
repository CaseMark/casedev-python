# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1SecFilingResponse", "Filing", "FilingDocument", "FilingEntity"]


class FilingDocument(BaseModel):
    description: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None


class FilingEntity(BaseModel):
    cik: Optional[str] = None

    entity_type: Optional[str] = FieldInfo(alias="entityType", default=None)

    name: Optional[str] = None

    sic: Optional[str] = None

    sic_description: Optional[str] = FieldInfo(alias="sicDescription", default=None)

    state_of_incorporation: Optional[str] = FieldInfo(alias="stateOfIncorporation", default=None)

    ticker: Optional[str] = None


class Filing(BaseModel):
    accession_number: Optional[str] = FieldInfo(alias="accessionNumber", default=None)

    description: Optional[str] = None

    documents: Optional[List[FilingDocument]] = None

    entity: Optional[FilingEntity] = None

    filed_at: Optional[date] = FieldInfo(alias="filedAt", default=None)

    form_type: Optional[str] = FieldInfo(alias="formType", default=None)

    period_of_report: Optional[date] = FieldInfo(alias="periodOfReport", default=None)

    sec_url: Optional[str] = FieldInfo(alias="secUrl", default=None)

    snippet: Optional[str] = None


class V1SecFilingResponse(BaseModel):
    cik: Optional[str] = None

    date_after: Optional[date] = FieldInfo(alias="dateAfter", default=None)

    date_before: Optional[date] = FieldInfo(alias="dateBefore", default=None)

    entity: Optional[str] = None

    filings: Optional[List[Filing]] = None

    form_types: Optional[List[str]] = FieldInfo(alias="formTypes", default=None)

    limit: Optional[int] = None

    offset: Optional[int] = None

    query: Optional[str] = None

    ticker: Optional[str] = None

    total: Optional[int] = None

    type: Optional[Literal["search", "entity"]] = None
