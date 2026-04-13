# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ChatCreateStreamTokenResponse"]


class ChatCreateStreamTokenResponse(BaseModel):
    token: str

    expires_at: datetime = FieldInfo(alias="expiresAt")

    stream_url: str = FieldInfo(alias="streamUrl")
