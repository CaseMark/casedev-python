# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["AgentCreateParams", "Sandbox"]


class AgentCreateParams(TypedDict, total=False):
    instructions: Required[str]
    """System instructions that define agent behavior"""

    name: Required[str]
    """Display name for the agent"""

    description: str
    """Optional description of the agent"""

    disabled_tools: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="disabledTools")]
    """Denylist of tools the agent cannot use"""

    enabled_tools: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="enabledTools")]
    """Allowlist of tools the agent can use"""

    model: str
    """LLM model identifier (e.g.

    anthropic/claude-sonnet-4.6). Defaults to anthropic/claude-sonnet-4.6
    """

    sandbox: Optional[Sandbox]
    """Custom sandbox configuration (cpu, memoryMiB)"""

    vault_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="vaultIds")]
    """Restrict agent to specific vault IDs"""


class Sandbox(TypedDict, total=False):
    """Custom sandbox configuration (cpu, memoryMiB)"""

    cpu: int
    """Number of CPUs"""

    memory_mi_b: Annotated[int, PropertyInfo(alias="memoryMiB")]
    """Memory in MiB"""
