# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["InstanceTypeListResponse", "InstanceType", "InstanceTypeSpecs"]


class InstanceTypeSpecs(BaseModel):
    memory_gib: Optional[int] = FieldInfo(alias="memoryGib", default=None)
    """RAM in GiB"""

    storage_gib: Optional[int] = FieldInfo(alias="storageGib", default=None)
    """Storage in GiB"""

    vcpus: Optional[int] = None
    """Number of vCPUs"""


class InstanceType(BaseModel):
    description: Optional[str] = None
    """Instance description"""

    gpu: Optional[str] = None
    """GPU model and count"""

    name: Optional[str] = None
    """Instance type identifier"""

    price_per_hour: Optional[str] = FieldInfo(alias="pricePerHour", default=None)
    """Price per hour (e.g. '$1.20')"""

    regions_available: Optional[List[str]] = FieldInfo(alias="regionsAvailable", default=None)
    """Available regions"""

    specs: Optional[InstanceTypeSpecs] = None


class InstanceTypeListResponse(BaseModel):
    count: int
    """Total number of instance types"""

    instance_types: List[InstanceType] = FieldInfo(alias="instanceTypes")
