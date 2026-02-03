# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProjectGetConnectionResponse"]


class ProjectGetConnectionResponse(BaseModel):
    branch: str
    """Branch name for this connection"""

    connection_uri: str = FieldInfo(alias="connectionUri")
    """PostgreSQL connection string (includes credentials)"""

    pooled: bool
    """Whether this is a pooled connection"""
