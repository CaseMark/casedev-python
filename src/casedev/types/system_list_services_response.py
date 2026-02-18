# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["SystemListServicesResponse", "Service"]


class Service(BaseModel):
    id: str

    description: str

    href: str

    icon: str

    name: str

    order: int


class SystemListServicesResponse(BaseModel):
    services: List[Service]
