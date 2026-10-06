# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["KeyBindResponse"]


class KeyBindResponse(BaseModel):
    id: str

    api_key_id: str

    application_id: str
