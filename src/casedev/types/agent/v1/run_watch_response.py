# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RunWatchResponse"]


class RunWatchResponse(BaseModel):
    callback_url: Optional[str] = FieldInfo(alias="callbackUrl", default=None)

    ok: Optional[bool] = None
