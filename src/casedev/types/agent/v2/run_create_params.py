# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["RunCreateParams"]


class RunCreateParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    prompt: Required[str]

    callback_url: Annotated[Optional[str], PropertyInfo(alias="callbackUrl")]

    guidance: Optional[str]

    model: Optional[str]

    object_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="objectIds")]
