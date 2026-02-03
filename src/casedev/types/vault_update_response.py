# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VaultUpdateResponse"]


class VaultUpdateResponse(BaseModel):
    id: Optional[str] = None
    """Vault identifier"""

    chunk_strategy: Optional[object] = FieldInfo(alias="chunkStrategy", default=None)
    """Document chunking strategy configuration"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Vault creation timestamp"""

    description: Optional[str] = None
    """Vault description"""

    enable_graph: Optional[bool] = FieldInfo(alias="enableGraph", default=None)
    """Whether GraphRAG is enabled for future uploads"""

    files_bucket: Optional[str] = FieldInfo(alias="filesBucket", default=None)
    """S3 bucket for document storage"""

    index_name: Optional[str] = FieldInfo(alias="indexName", default=None)
    """Search index name"""

    kms_key_id: Optional[str] = FieldInfo(alias="kmsKeyId", default=None)
    """KMS key for encryption"""

    metadata: Optional[object] = None
    """Additional vault metadata"""

    name: Optional[str] = None
    """Vault name"""

    region: Optional[str] = None
    """AWS region"""

    total_bytes: Optional[int] = FieldInfo(alias="totalBytes", default=None)
    """Total storage size in bytes"""

    total_objects: Optional[int] = FieldInfo(alias="totalObjects", default=None)
    """Number of stored documents"""

    total_vectors: Optional[int] = FieldInfo(alias="totalVectors", default=None)
    """Number of vector embeddings"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Last update timestamp"""

    vector_bucket: Optional[str] = FieldInfo(alias="vectorBucket", default=None)
    """S3 bucket for vector embeddings"""
