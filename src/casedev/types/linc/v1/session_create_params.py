# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["SessionCreateParams", "Extension", "VaultScope"]


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

    extensions: Optional[Iterable[Extension]]
    """
    Optional caller-supplied executable tool files to install into .linc/extensions/
    before the agent starts. Only supported for standalone sessions without
    capabilityPolicy: read_only. Rejected with a 400 on persistent
    (workspaceKey/conversationKey) or read_only sessions. At most 10 files, 64KB
    each, 256KB total. Extension destinations and content hashes are recorded in the
    session-created audit event; raw code is not logged.
    """

    idle_timeout_ms: Annotated[Optional[int], PropertyInfo(alias="idleTimeoutMs")]

    include_document_templates: Annotated[Optional[bool], PropertyInfo(alias="includeDocumentTemplates")]
    """
    When true, inject all active org document templates into the
    using-document-templates skill.
    """

    model: Optional[str]

    model_fallbacks: Annotated[SequenceNotStr[str], PropertyInfo(alias="modelFallbacks")]
    """Optional ordered availability fallbacks for this session.

    Requires an explicit model. An empty array disables fallbacks; omission
    preserves existing runtime behavior. Linc switches within the same session,
    preserving context.
    """

    runtime_retention: Annotated[Literal["indefinite"], PropertyInfo(alias="runtimeRetention")]
    """
    indefinite keeps the runtime and its saved state until the session (or, in
    workspace mode, its last conversation) is deleted, so a chat can resume after
    any idle gap. The default in workspace mode; standalone chats opt in with it,
    one-off runs leave it unset. Raises an existing workspace to indefinite.
    Mutually exclusive with runtimeRetentionDays.
    """

    runtime_retention_days: Annotated[int, PropertyInfo(alias="runtimeRetentionDays")]
    """Days the runtime and its saved state are kept after the last activity.

    Defaults to 1 for standalone sessions; workspace-mode conversations
    (workspaceKey) and the C3 system key default to indefinite (see
    runtimeRetention). Once they are deleted, commands to the session answer 410
    linc_runtime_expired; its events stay readable. A workspace keeps the value it
    was created with; a larger value on a later conversation raises it. Applies to
    Vercel Sandbox runtimes; accepted and stored on Daytona, where it has no effect.
    Mutually exclusive with runtimeRetention.
    """

    scoped_api_key: Annotated[Optional[str], PropertyInfo(alias="scopedApiKey")]
    """Optional caller-provided scoped Case.dev API key for the runtime."""

    service_tier: Annotated[Literal["default", "priority"], PropertyInfo(alias="serviceTier")]
    """Processing tier for eligible OpenAI GPT models.

    Priority provides lower latency at premium cost.
    """

    skills_delivery: Annotated[Literal["local", "mcp"], PropertyInfo(alias="skillsDelivery")]
    """Defaults to local preinstallation.

    MCP is an opt-in, org-allowlisted rollout on a separately pinned image; requires
    a new standalone session and no skillSlugs preinstallation. Execution remains
    content-approval gated.
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


class Extension(TypedDict, total=False):
    content: Required[str]
    """UTF-8 tool file content, at most 64KB."""

    path: Required[str]
    """Bare .ts/.js filename or one-level subdir (e.g.

    create-automations.ts or automations/index.ts). Each directory must include
    exactly one index.ts or index.js entrypoint; helper files may accompany it.
    Platform names (casedev/subagent), root index.ts/index.js, node_modules, hidden
    top-level names, absolute paths, "..", and other extensions or nesting are
    rejected.
    """


class VaultScope(TypedDict, total=False):
    object_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="objectIds")]]

    vault_id: Required[Annotated[str, PropertyInfo(alias="vaultId")]]
