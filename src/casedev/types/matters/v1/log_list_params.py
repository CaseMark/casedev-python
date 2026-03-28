# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["LogListParams"]


class LogListParams(TypedDict, total=False):
    actor_id: str
    """Filter by actor ID"""

    actor_type: str
    """Filter by actor type"""

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of time range (ISO 8601)"""

    event_type: str
    """Filter by exact event type"""

    limit: int
    """Maximum number of log entries to return (max 200)"""

    offset: int
    """Number of log entries to skip for pagination"""

    scope: Union[str, SequenceNotStr[str]]
    """Filter by scope: matter, work_item, execution, sharing, all"""

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start of time range (ISO 8601)"""

    work_item_id: str
    """Filter by work item ID"""
