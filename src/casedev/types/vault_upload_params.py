# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VaultUploadParams"]


class VaultUploadParams(TypedDict, total=False):
    content_type: Required[Annotated[str, PropertyInfo(alias="contentType")]]
    """MIME type of the file (e.g., application/pdf, image/jpeg)"""

    filename: Required[str]
    """Name of the file to upload"""

    auto_index: bool
    """Whether to automatically process and index the file for search"""

    is_ai_generated: bool
    """Marks the file as AI-generated work product (e.g.

    uploaded by an agent) rather than a user-provided source document. Persisted on
    the object and returned by object listings so clients can distinguish
    provenance.
    """

    metadata: object
    """Additional metadata to associate with the file"""

    path: str
    """Optional folder path for hierarchy preservation.

    Allows integrations to maintain source folder structure from systems like
    NetDocs, Clio, or Smokeball. Example: '/Discovery/Depositions/2024'
    """

    size_bytes: Annotated[int, PropertyInfo(alias="sizeBytes")]
    """File size in bytes (optional, max 5GB for single PUT uploads).

    When provided, enforces exact file size at S3 level.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
