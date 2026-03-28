# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ShareCreateParams"]


class ShareCreateParams(TypedDict, total=False):
    target_org_id: Required[str]

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    permission: Literal["read", "edit"]
