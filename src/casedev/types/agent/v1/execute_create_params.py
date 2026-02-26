# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ExecuteCreateParams", "Sandbox"]


class ExecuteCreateParams(TypedDict, total=False):
    prompt: Required[str]
    """Task prompt for the agent"""

    disabled_tools: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="disabledTools")]
    """Denylist of tools the agent cannot use"""

    enabled_tools: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="enabledTools")]
    """Allowlist of tools the agent can use"""

    guidance: Optional[str]
    """Additional context or constraints for this run"""

    instructions: str
    """System instructions.

    Defaults to a general-purpose legal assistant prompt if not provided.
    """

    model: str
    """LLM model identifier. Defaults to anthropic/claude-sonnet-4.6"""

    object_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="objectIds")]
    """Scope this run to specific vault object IDs.

    The agent will only access these objects.
    """

    sandbox: Optional[Sandbox]
    """Custom sandbox resources (cpu, memoryMiB)"""

    vault_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="vaultIds")]
    """Restrict agent to specific vault IDs"""


class Sandbox(TypedDict, total=False):
    """Custom sandbox resources (cpu, memoryMiB)"""

    cpu: int
    """Number of CPUs"""

    memory_mi_b: Annotated[int, PropertyInfo(alias="memoryMiB")]
    """Memory in MiB"""
