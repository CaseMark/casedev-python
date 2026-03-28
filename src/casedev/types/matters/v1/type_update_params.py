# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, TypedDict

from ...._types import SequenceNotStr

__all__ = ["TypeUpdateParams"]


class TypeUpdateParams(TypedDict, total=False):
    default_agent_type_id: Optional[str]

    default_metadata: Dict[str, object]

    default_work_items: Iterable[Dict[str, object]]

    description: Optional[str]

    exit_criteria: SequenceNotStr[str]

    instructions: Optional[str]

    intake_requirements: SequenceNotStr[str]

    is_active: bool

    name: str

    orchestration_mode: Literal["auto", "human"]

    review_agent_type_id: Optional[str]

    review_criteria: SequenceNotStr[str]

    skill_refs: SequenceNotStr[str]

    slug: str
