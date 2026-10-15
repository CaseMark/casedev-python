# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1SecXbrlResponse", "Concept", "Data", "Fact"]


class Concept(BaseModel):
    fact_count: Optional[int] = FieldInfo(alias="factCount", default=None)

    label: Optional[str] = None

    latest_period_end: Optional[date] = FieldInfo(alias="latestPeriodEnd", default=None)

    tag: Optional[str] = None

    taxonomy: Optional[str] = None

    units: Optional[List[str]] = None


class Data(BaseModel):
    accession_number: Optional[str] = FieldInfo(alias="accessionNumber", default=None)

    cik: Optional[str] = None

    end: Optional[date] = None

    entity_name: Optional[str] = FieldInfo(alias="entityName", default=None)

    filed: Optional[date] = None

    fiscal_period: Optional[str] = FieldInfo(alias="fiscalPeriod", default=None)

    fiscal_year: Optional[int] = FieldInfo(alias="fiscalYear", default=None)

    form: Optional[str] = None

    frame: Optional[str] = None
    """SEC calendar frame, null if not assigned"""

    label: Optional[str] = None

    loc: Optional[str] = None
    """frames only. Reporting company location code"""

    sec_url: Optional[str] = FieldInfo(alias="secUrl", default=None)
    """EDGAR filing index URL"""

    start: Optional[date] = None
    """Null for instantaneous facts"""

    tag: Optional[str] = None

    taxonomy: Optional[str] = None

    unit: Optional[str] = None
    """For example USD, shares, or USD/shares"""

    value: Optional[float] = None


class Fact(BaseModel):
    accession_number: Optional[str] = FieldInfo(alias="accessionNumber", default=None)

    cik: Optional[str] = None

    end: Optional[date] = None

    entity_name: Optional[str] = FieldInfo(alias="entityName", default=None)

    filed: Optional[date] = None

    fiscal_period: Optional[str] = FieldInfo(alias="fiscalPeriod", default=None)

    fiscal_year: Optional[int] = FieldInfo(alias="fiscalYear", default=None)

    form: Optional[str] = None

    frame: Optional[str] = None
    """SEC calendar frame, null if not assigned"""

    label: Optional[str] = None

    loc: Optional[str] = None
    """frames only. Reporting company location code"""

    sec_url: Optional[str] = FieldInfo(alias="secUrl", default=None)
    """EDGAR filing index URL"""

    start: Optional[date] = None
    """Null for instantaneous facts"""

    tag: Optional[str] = None

    taxonomy: Optional[str] = None

    unit: Optional[str] = None
    """For example USD, shares, or USD/shares"""

    value: Optional[float] = None


class V1SecXbrlResponse(BaseModel):
    cik: Optional[str] = None
    """Padded CIK (concept and facts)"""

    concepts: Optional[List[Concept]] = None
    """facts without concepts: the catalog of concepts the company reports"""

    data: Optional[List[Data]] = None
    """frames: one row per reporting company"""

    date_after: Optional[date] = FieldInfo(alias="dateAfter", default=None)

    date_before: Optional[date] = FieldInfo(alias="dateBefore", default=None)

    dedupe: Optional[bool] = None
    """concept and facts with concepts"""

    description: Optional[str] = None

    entity_name: Optional[str] = FieldInfo(alias="entityName", default=None)

    facts: Optional[List[Fact]] = None
    """concept, and facts when concepts is provided"""

    fiscal_periods: Optional[List[str]] = FieldInfo(alias="fiscalPeriods", default=None)

    form_types: Optional[List[str]] = FieldInfo(alias="formTypes", default=None)

    label: Optional[str] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    period: Optional[str] = None
    """frames only"""

    sort: Optional[str] = None
    """frames only"""

    tag: Optional[str] = None
    """concept and frames"""

    taxonomy: Optional[str] = None

    ticker: Optional[str] = None

    total: Optional[int] = None
    """Rows matching before pagination"""

    type: Optional[Literal["concept", "facts", "frames"]] = None

    unit: Optional[str] = None
