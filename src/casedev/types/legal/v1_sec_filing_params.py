# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["V1SecFilingParams"]


class V1SecFilingParams(TypedDict, total=False):
    type: Required[Literal["search", "entity"]]
    """Run a full-text search or fetch a single entity filing history"""

    cik: str
    """CIK for entity lookups. Accepts padded or unpadded digits."""

    date_after: Annotated[Union[str, date], PropertyInfo(alias="dateAfter", format="iso8601")]
    """Optional lower filing date bound (YYYY-MM-DD)"""

    date_before: Annotated[Union[str, date], PropertyInfo(alias="dateBefore", format="iso8601")]
    """Optional upper filing date bound (YYYY-MM-DD)"""

    entity: str
    """Optional entity filter passed through to EDGAR full-text search"""

    form_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="formTypes")]
    """Optional SEC form type filter such as 10-K, 10-Q, 8-K, or 4"""

    limit: int
    """Maximum filings to return"""

    offset: int
    """Result offset for pagination"""

    query: str
    """Full-text SEC search query (required for type: search)"""

    ticker: str
    """Optional company ticker. Valid for both search and entity lookups."""
