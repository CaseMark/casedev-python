# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ObjectMoveParams"]


class ObjectMoveParams(TypedDict, total=False):
    destination_vault_id: Required[Annotated[str, PropertyInfo(alias="destinationVaultId")]]

    mode: Required[Literal["move", "copy"]]

    object_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="objectIds")]]

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    path: Optional[str]
