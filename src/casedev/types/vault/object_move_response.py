# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectMoveResponse"]


class ObjectMoveResponse(BaseModel):
    destination_vault_id: Optional[str] = FieldInfo(alias="destinationVaultId", default=None)

    mode: Optional[str] = None

    results: Optional[List[object]] = None

    source_vault_id: Optional[str] = FieldInfo(alias="sourceVaultId", default=None)
