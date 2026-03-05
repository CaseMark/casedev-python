# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DocketSearchResult"]


class DocketSearchResult(BaseModel):
    id: Optional[str] = None

    assigned_to: Optional[str] = FieldInfo(alias="assignedTo", default=None)

    case_name: Optional[str] = FieldInfo(alias="caseName", default=None)

    cause: Optional[str] = None

    court: Optional[str] = None

    court_id: Optional[str] = FieldInfo(alias="courtId", default=None)

    date_filed: Optional[date] = FieldInfo(alias="dateFiled", default=None)

    date_terminated: Optional[date] = FieldInfo(alias="dateTerminated", default=None)

    docket_number: Optional[str] = FieldInfo(alias="docketNumber", default=None)

    nature_of_suit: Optional[str] = FieldInfo(alias="natureOfSuit", default=None)

    pacer_case_id: Optional[str] = FieldInfo(alias="pacerCaseId", default=None)

    parties: Optional[List[str]] = None

    url: Optional[str] = None
