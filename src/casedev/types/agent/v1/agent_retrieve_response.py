# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AgentRetrieveResponse"]


class AgentRetrieveResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    disabled_tools: Optional[List[str]] = FieldInfo(alias="disabledTools", default=None)

    enabled_tools: Optional[List[str]] = FieldInfo(alias="enabledTools", default=None)

    instructions: Optional[str] = None

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    model: Optional[str] = None

    name: Optional[str] = None

    sandbox: Optional[object] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    vault_ids: Optional[List[str]] = FieldInfo(alias="vaultIds", default=None)
