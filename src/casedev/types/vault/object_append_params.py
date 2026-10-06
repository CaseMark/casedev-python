# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ObjectAppendParams", "Bates"]


class ObjectAppendParams(TypedDict, total=False):
    id: Required[str]

    append_object_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="appendObjectIds")]]
    """Vault object IDs whose pages will be appended onto the target object, in order.

    Must not include the target object itself. Sync mode accepts at most 20; async
    mode accepts at most 1000.
    """

    back_links: Annotated[bool, PropertyInfo(alias="backLinks")]
    """Adds back links on appended pages"""

    back_links_text: Annotated[str, PropertyInfo(alias="backLinksText")]
    """Label text for the back link.

    Used only when backLinks is true and rendered centered at the bottom of each
    appended page.
    """

    bates: Bates
    """Optional Bates stamping for appended source PDFs.

    Numbering is deterministic across appendObjectIds order and does not stamp the
    target report pages.
    """

    client_reference: Annotated[str, PropertyInfo(alias="clientReference")]
    """Caller-provided correlation value returned in async responses and webhooks."""

    mode: Literal["sync", "async"]
    """
    Use async to return immediately and receive completion through
    vault.object.append webhooks.
    """

    rewrite_links: Annotated[bool, PropertyInfo(alias="rewriteLinks")]
    """
    When true, rewrites links in the target object to internal PDF jumps when the
    URL contains exactly one appended object ID as a standalone query parameter
    value or decoded path segment.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Bates(TypedDict, total=False):
    """Optional Bates stamping for appended source PDFs.

    Numbering is deterministic across appendObjectIds order and does not stamp the target report pages.
    """

    enabled: bool

    pad_to: Annotated[int, PropertyInfo(alias="padTo")]

    prefix: str

    start: int

    suffix: str
