# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GraphragProcessObjectResponse", "Stats"]


class Stats(BaseModel):
    """Extraction statistics"""

    community_count: Optional[int] = None

    entity_count: Optional[int] = None

    relationship_count: Optional[int] = None


class GraphragProcessObjectResponse(BaseModel):
    communities: int
    """Number of communities detected"""

    entities: int
    """Number of entities extracted"""

    object_id: str = FieldInfo(alias="objectId")
    """ID of the indexed object"""

    relationships: int
    """Number of relationships extracted"""

    stats: Stats
    """Extraction statistics"""

    status: str
    """Status from GraphRAG service"""

    success: bool
    """Whether indexing completed successfully"""

    vault_id: str = FieldInfo(alias="vaultId")
    """ID of the vault"""
