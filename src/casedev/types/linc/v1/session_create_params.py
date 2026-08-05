# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["SessionCreateParams"]


class SessionCreateParams(TypedDict, total=False):
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
