# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ExecuteCreateParams", "Sandbox"]


class ExecuteCreateParams(TypedDict, total=False):
    prompt: Required[str]

    agent_runtime: Annotated[Optional[bool], PropertyInfo(alias="agentRuntime")]
    """Set to true to opt into the legacy Daytona-backed agent runtime."""

    disabled_tools: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="disabledTools")]

    enabled_tools: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="enabledTools")]

    guidance: Optional[str]

    instructions: str

    model: str

    object_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="objectIds")]

    sandbox: Optional[Sandbox]

    vault_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="vaultIds")]


class Sandbox(TypedDict, total=False):
    cpu: int

    memory_mi_b: Annotated[int, PropertyInfo(alias="memoryMiB")]
