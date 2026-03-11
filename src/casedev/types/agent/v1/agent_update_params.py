# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Updated agent description. Pass null to clear if supported by the client."""

    disabled_tools: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="disabledTools")]
    """Denylist of tools the agent cannot use.

    Mutually exclusive with enabledTools — set one or the other, not both. Pass null
    to clear.
    """

    enabled_tools: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="enabledTools")]
    """Allowlist of tools the agent can use.

    Mutually exclusive with disabledTools — set one or the other, not both. Pass
    null to clear.
    """

    instructions: str
    """Updated system instructions that guide agent behavior"""

    model: str
    """Model identifier the agent should use for future runs"""

    name: str
    """Updated agent display name"""

    sandbox: Optional[object]
    """Sandbox configuration override for future agent runs. Pass null to clear."""

    vault_groups: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="vaultGroups")]
    """Vault group IDs the agent can access. Pass null to clear."""

    vault_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="vaultIds")]
    """Vault IDs the agent can access directly. Pass null to clear."""
