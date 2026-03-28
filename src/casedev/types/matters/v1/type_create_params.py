# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["TypeCreateParams"]


class TypeCreateParams(TypedDict, total=False):
    name: Required[str]

    default_agent_type_id: str

    default_metadata: Dict[str, object]

    default_work_items: Iterable[Dict[str, object]]

    description: str

    exit_criteria: SequenceNotStr[str]

    instructions: str

    intake_requirements: SequenceNotStr[str]

    is_active: bool

    orchestration_mode: Literal["auto", "human"]

    review_agent_type_id: str

    review_criteria: SequenceNotStr[str]

    skill_refs: SequenceNotStr[str]

    slug: str
