# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WorkItemDecideParams"]


class WorkItemDecideParams(TypedDict, total=False):
    id: Required[str]

    decision: Required[Literal["approve", "revise", "block", "reassign"]]

    agent_type_id: Optional[str]

    metadata: Dict[str, object]

    reason: Optional[str]
