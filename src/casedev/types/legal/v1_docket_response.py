# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .docket_detail import DocketDetail
from .docket_search_result import DocketSearchResult

__all__ = ["V1DocketResponse", "Entry", "EntryDocument", "Pagination"]


class EntryDocument(BaseModel):
    id: Optional[str] = None

    attachment_number: Optional[int] = FieldInfo(alias="attachmentNumber", default=None)

    description: Optional[str] = None

    document_number: Optional[str] = FieldInfo(alias="documentNumber", default=None)

    is_available: Optional[bool] = FieldInfo(alias="isAvailable", default=None)

    page_count: Optional[int] = FieldInfo(alias="pageCount", default=None)

    pdf_url: Optional[str] = FieldInfo(alias="pdfUrl", default=None)


class Entry(BaseModel):
    date: Optional[datetime.date] = None

    description: Optional[str] = None

    documents: Optional[List[EntryDocument]] = None

    entry_number: Optional[int] = FieldInfo(alias="entryNumber", default=None)


class Pagination(BaseModel):
    """Pagination info for entry list (lookup mode with includeEntries)"""

    limit: Optional[int] = None

    offset: Optional[int] = None

    returned: Optional[int] = None


class V1DocketResponse(BaseModel):
    court: Optional[str] = None
    """Echo of court filter (search mode only)"""

    date_filed_after: Optional[datetime.date] = FieldInfo(alias="dateFiledAfter", default=None)
    """Echo of date filter"""

    date_filed_before: Optional[datetime.date] = FieldInfo(alias="dateFiledBefore", default=None)
    """Echo of date filter"""

    docket: Optional[DocketDetail] = None
    """Full docket record (lookup mode)"""

    dockets: Optional[List[DocketSearchResult]] = None
    """Search results (search mode)"""

    entries: Optional[List[Entry]] = None
    """Docket entries/filings (lookup mode with includeEntries)"""

    found: Optional[int] = None

    include_entries: Optional[bool] = FieldInfo(alias="includeEntries", default=None)
    """Whether entries were requested (lookup mode only)"""

    pagination: Optional[Pagination] = None
    """Pagination info for entry list (lookup mode with includeEntries)"""

    query: Optional[str] = None
    """Echo of search query (search mode only)"""

    type: Optional[Literal["search", "lookup"]] = None
