# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["HoldCreateParams", "ReleaseCondition"]


class HoldCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account to hold funds in"""

    amount: Required[int]
    """Amount in cents to hold"""

    currency: str

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    memo: str

    metadata: object

    on_release_action: str
    """Action to take when released"""

    on_release_config: object

    release_conditions: Iterable[ReleaseCondition]


class ReleaseCondition(TypedDict, total=False):
    approvers: SequenceNotStr[str]

    date: str

    document_id: str

    type: Literal["manual_approval", "document_signed", "date_reached"]
