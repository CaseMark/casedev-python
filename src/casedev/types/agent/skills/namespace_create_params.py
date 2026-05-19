# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["NamespaceCreateParams"]


class NamespaceCreateParams(TypedDict, total=False):
    namespace_id: Required[Annotated[str, PropertyInfo(alias="namespaceId")]]
    """URL-safe slug, e.g.

    "curi" or "client-firm-abc". Lowercase alphanumeric with single hyphens, 2-64
    chars.
    """

    description: Optional[str]

    label: Optional[str]

    metadata: Optional[object]
