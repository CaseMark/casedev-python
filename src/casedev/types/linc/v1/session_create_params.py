# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["SessionCreateParams", "VaultScope"]


class SessionCreateParams(TypedDict, total=False):
    capability_policy: Annotated[Literal["read_only"], PropertyInfo(alias="capabilityPolicy")]
    """Optional server-enforced capability profile.

    read_only grants only retrieval/inference service reads; session event ingestion
    remains bound to the exact managed runtime credential.
    """

    conversation_key: Annotated[str, PropertyInfo(alias="conversationKey")]
    """Stable conversation identity within workspaceKey.

    Required in workspace mode and idempotent for repeated creates.
    """

    document_template_slugs: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="documentTemplateSlugs")]
    """
    Specific document template slugs to inject into the using-document-templates
    skill.
    """

    idle_timeout_ms: Annotated[Optional[int], PropertyInfo(alias="idleTimeoutMs")]

    include_document_templates: Annotated[Optional[bool], PropertyInfo(alias="includeDocumentTemplates")]
    """
    When true, inject all active org document templates into the
    using-document-templates skill.
    """

    instructions: Optional[str]
    """Privileged C3-only hidden app instructions to append to the sandbox AGENTS.md."""

    model: Optional[str]

    scoped_api_key: Annotated[Optional[str], PropertyInfo(alias="scopedApiKey")]
    """Optional caller-provided scoped Case.dev API key for the runtime."""

    service_tier: Annotated[Literal["default", "priority"], PropertyInfo(alias="serviceTier")]
    """Processing tier for eligible OpenAI GPT models.

    Priority provides lower latency at premium cost.
    """

    skill_slugs: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="skillSlugs")]
    """
    Skills API slugs to install into the runtime sandbox before the native session
    starts.
    """

    title: str

    vault_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="vaultIds")]
    """Legacy explicit whole-vault scope. Mutually exclusive with vaultScopes."""

    vault_scopes: Annotated[Optional[Iterable[VaultScope]], PropertyInfo(alias="vaultScopes")]
    """Exact object allowlist per vault.

    Empty objectIds denies object access for that vault. Mutually exclusive with
    vaultIds.
    """

    workspace_key: Annotated[str, PropertyInfo(alias="workspaceKey")]
    """Opt-in persistent workspace identity.

    Requires conversationKey. Omit both fields to preserve isolated legacy session
    behavior.
    """

    ai_reporting_tags: Annotated[str, PropertyInfo(alias="ai-reporting-tags")]

    ai_reporting_user: Annotated[str, PropertyInfo(alias="ai-reporting-user")]


class VaultScope(TypedDict, total=False):
    object_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="objectIds")]]

    vault_id: Required[Annotated[str, PropertyInfo(alias="vaultId")]]
