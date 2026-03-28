# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["WorkItemUpdateParams"]


class WorkItemUpdateParams(TypedDict, total=False):
    id: Required[str]

    assignee_id: Optional[str]

    completed_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    description: str

    due_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    exit_criteria: SequenceNotStr[str]

    instructions: Optional[str]

    metadata: Dict[str, object]

    priority: Literal["low", "normal", "high", "urgent"]

    started_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    status: Literal["draft", "queued", "in_progress", "blocked", "in_review", "awaiting_human", "done", "canceled"]

    title: str

    type: Literal[
        "task", "deadline", "review", "filing", "communication", "research", "drafting", "collection", "intake"
    ]
