# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["LogExportParams"]


class LogExportParams(TypedDict, total=False):
    actor_id: str
    """Filter by actor ID"""

    actor_type: str
    """Filter by actor type"""

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of time range (ISO 8601)"""

    event_type: str
    """Filter by exact event type"""

    format: Literal["json", "jsonl", "csv", "tsv"]
    """Export format. Defaults to jsonl."""

    scope: Union[str, SequenceNotStr[str]]
    """Filter by scope: matter, work_item, execution, sharing, all"""

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start of time range (ISO 8601)"""

    work_item_id: str
    """Filter by work item ID"""
