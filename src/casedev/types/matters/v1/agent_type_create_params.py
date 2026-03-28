# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["AgentTypeCreateParams"]


class AgentTypeCreateParams(TypedDict, total=False):
    instructions: Required[str]

    name: Required[str]

    description: str

    disabled_tools: SequenceNotStr[str]

    enabled_tools: SequenceNotStr[str]

    is_active: bool

    is_default: bool

    metadata: Dict[str, object]

    model: str

    skill_refs: SequenceNotStr[str]

    slug: str
