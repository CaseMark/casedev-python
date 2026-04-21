# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VaultCreateResponse", "EmbeddingProfile"]


class EmbeddingProfile(BaseModel):
    """The resolved embedding profile for this vault. Null for storage-only vaults."""

    dimensions: Optional[int] = None
    """Vector dimension used by this vault"""

    model: Optional[str] = None
    """Embedding model catalog key"""

    provider: Optional[str] = None
    """Embedding provider"""


class VaultCreateResponse(BaseModel):
    id: Optional[str] = None
    """Unique vault identifier"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Vault creation timestamp"""

    description: Optional[str] = None
    """Vault description"""

    embedding_profile: Optional[EmbeddingProfile] = FieldInfo(alias="embeddingProfile", default=None)
    """The resolved embedding profile for this vault. Null for storage-only vaults."""

    enable_indexing: Optional[bool] = FieldInfo(alias="enableIndexing", default=None)
    """Whether vector indexing is enabled for this vault"""

    files_bucket: Optional[str] = FieldInfo(alias="filesBucket", default=None)
    """S3 bucket name for document storage"""

    index_name: Optional[str] = FieldInfo(alias="indexName", default=None)
    """Vector search index name. Null for storage-only vaults."""

    name: Optional[str] = None
    """Vault display name"""

    region: Optional[str] = None
    """AWS region for storage"""

    vector_bucket: Optional[str] = FieldInfo(alias="vectorBucket", default=None)
    """S3 bucket name for vector embeddings. Null for storage-only vaults."""
