# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ProjectDeleteResponse"]


class ProjectDeleteResponse(BaseModel):
    message: str
    """Confirmation message"""

    success: bool
    """Deletion success indicator"""
