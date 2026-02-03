# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["InstanceRetrieveResponse", "SSH"]


class SSH(BaseModel):
    command: Optional[str] = None

    host: Optional[str] = None

    instructions: Optional[List[object]] = None

    private_key: Optional[str] = FieldInfo(alias="privateKey", default=None)

    user: Optional[str] = None


class InstanceRetrieveResponse(BaseModel):
    id: Optional[str] = None

    auto_shutdown_minutes: Optional[int] = FieldInfo(alias="autoShutdownMinutes", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    current_cost: Optional[str] = FieldInfo(alias="currentCost", default=None)

    current_runtime_seconds: Optional[int] = FieldInfo(alias="currentRuntimeSeconds", default=None)

    gpu: Optional[str] = None

    instance_type: Optional[str] = FieldInfo(alias="instanceType", default=None)

    ip: Optional[str] = None

    name: Optional[str] = None

    price_per_hour: Optional[str] = FieldInfo(alias="pricePerHour", default=None)

    region: Optional[str] = None

    specs: Optional[object] = None

    ssh: Optional[SSH] = None

    started_at: Optional[str] = FieldInfo(alias="startedAt", default=None)

    status: Optional[str] = None

    vault_mounts: Optional[object] = FieldInfo(alias="vaultMounts", default=None)
