# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["WorkItemCreateParams"]


class WorkItemCreateParams(TypedDict, total=False):
    title: Required[str]

    assignee_id: str

    description: str

    due_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    exit_criteria: SequenceNotStr[str]

    instructions: str

    metadata: Dict[str, object]

    priority: Literal["low", "normal", "high", "urgent"]

    type: Literal[
        "task", "deadline", "review", "filing", "communication", "research", "drafting", "collection", "intake"
    ]
