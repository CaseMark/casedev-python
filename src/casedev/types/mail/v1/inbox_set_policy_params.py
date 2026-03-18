# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["InboxSetPolicyParams"]


class InboxSetPolicyParams(TypedDict, total=False):
    allowed_sender_patterns: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedSenderPatterns")]
    """Exact emails, @domain rules, or \\**"""

    enforce_sender_allowlist: Annotated[bool, PropertyInfo(alias="enforceSenderAllowlist")]

    read_access_rules: Annotated[SequenceNotStr[str], PropertyInfo(alias="readAccessRules")]
    """
    Rules like organization, operator, user:<id>, api_key, api_key:<id>,
    clerk_session, or \\**
    """

    reply_access_rules: Annotated[SequenceNotStr[str], PropertyInfo(alias="replyAccessRules")]
    """
    Rules like organization, operator, user:<id>, api_key, api_key:<id>,
    clerk_session, or \\**
    """

    send_access_rules: Annotated[SequenceNotStr[str], PropertyInfo(alias="sendAccessRules")]
    """Rules like organization, user:<id>, api_key, api_key:<id>, clerk_session, or \\**"""
