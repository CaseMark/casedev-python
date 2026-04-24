# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VaultCreateParams"]


class VaultCreateParams(TypedDict, total=False):
    name: Required[str]
    """Display name for the vault"""

    description: str
    """Optional description of the vault's purpose"""

    embedding_model: Annotated[
        Literal[
            "openai/text-embedding-3-small",
            "openai/text-embedding-3-large",
            "voyage/voyage-3.5",
            "voyage/voyage-law-2",
            "cohere/embed-v4.0",
            "google/gemini-embedding-2",
            "casemark/embed-v1",
            "casemark/llama-nemotron-embed-vl-1b-v2",
        ],
        PropertyInfo(alias="embeddingModel"),
    ]
    """Optional embedding model for this vault.

    Defaults to casemark/embed-v1. Determines the S3 Vectors index dimension and
    which model is used at both ingest and search time. The vault is locked to this
    model after creation — use a re-embed flow to change later. Ignored when
    enableIndexing is false. Note: `casemark/llama-nemotron-embed-vl-1b-v2` is a
    deprecated alias for `casemark/embed-v1` (retained for SDK backward
    compatibility); new integrations should use `casemark/embed-v1` directly.
    """

    enable_graph: Annotated[bool, PropertyInfo(alias="enableGraph")]
    """Enable knowledge graph for entity relationship mapping.

    Only applies when enableIndexing is true.
    """

    enable_indexing: Annotated[bool, PropertyInfo(alias="enableIndexing")]
    """Enable vector indexing and search capabilities.

    Set to false for storage-only vaults.
    """

    group_id: Annotated[str, PropertyInfo(alias="groupId")]
    """Assign the vault to a vault group for access control.

    Required when using a group-scoped API key.
    """

    metadata: object
    """
    Optional metadata to attach to the vault (e.g., { containsPHI: true } for HIPAA
    compliance tracking)
    """
