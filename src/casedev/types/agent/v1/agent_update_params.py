# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    description: str

    disabled_tools: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="disabledTools")]

    enabled_tools: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="enabledTools")]

    instructions: str

    model: str

    name: str

    sandbox: Optional[object]

    vault_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="vaultIds")]
