# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1RetrieveParams"]


class V1RetrieveParams(TypedDict, total=False):
    granularity: Literal["summary", "daily"]
    """Whether to return period totals only or include daily buckets."""

    period_end: Annotated[Union[str, datetime], PropertyInfo(alias="periodEnd", format="iso8601")]
    """Period end date. Defaults to now."""

    period_start: Annotated[Union[str, datetime], PropertyInfo(alias="periodStart", format="iso8601")]
    """Period start date. Defaults to the start of the current calendar month."""
