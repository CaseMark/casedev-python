# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1ListCourtsResponse", "Court"]


class Court(BaseModel):
    id: Optional[str] = None
    """Court slug (use as the court parameter in legal.docket())"""

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    jurisdiction: Optional[str] = None

    pacer_court_id: Optional[int] = FieldInfo(alias="pacerCourtId", default=None)

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)


class V1ListCourtsResponse(BaseModel):
    courts: Optional[List[Court]] = None

    found: Optional[int] = None

    in_use_only: Optional[bool] = FieldInfo(alias="inUseOnly", default=None)
    """Whether results are filtered to in-use courts only"""

    jurisdiction: Optional[str] = None

    query: Optional[str] = None
