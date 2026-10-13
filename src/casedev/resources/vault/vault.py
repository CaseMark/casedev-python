# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from .groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from .memory import (
    MemoryResource,
    AsyncMemoryResource,
    MemoryResourceWithRawResponse,
    AsyncMemoryResourceWithRawResponse,
    MemoryResourceWithStreamingResponse,
    AsyncMemoryResourceWithStreamingResponse,
)
from ...types import (
    vault_list_params,
    vault_create_params,
    vault_delete_params,
    vault_ingest_params,
    vault_search_params,
    vault_update_params,
    vault_upload_params,
    vault_confirm_upload_params,
)
from .objects import (
    ObjectsResource,
    AsyncObjectsResource,
    ObjectsResourceWithRawResponse,
    AsyncObjectsResourceWithRawResponse,
    ObjectsResourceWithStreamingResponse,
    AsyncObjectsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from .multipart import (
    MultipartResource,
    AsyncMultipartResource,
    MultipartResourceWithRawResponse,
    AsyncMultipartResourceWithRawResponse,
    MultipartResourceWithStreamingResponse,
    AsyncMultipartResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .events.events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.vault_list_response import VaultListResponse
from ...types.vault_create_response import VaultCreateResponse
from ...types.vault_delete_response import VaultDeleteResponse
from ...types.vault_ingest_response import VaultIngestResponse
from ...types.vault_search_response import VaultSearchResponse
from ...types.vault_update_response import VaultUpdateResponse
from ...types.vault_upload_response import VaultUploadResponse
from ...types.vault_retrieve_response import VaultRetrieveResponse
from ...types.vault_confirm_upload_response import VaultConfirmUploadResponse

__all__ = ["VaultResource", "AsyncVaultResource"]


class VaultResource(SyncAPIResource):
    """Secure document storage with semantic search"""

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def groups(self) -> GroupsResource:
        """Secure document storage with semantic search"""
        return GroupsResource(self._client)

    @cached_property
    def multipart(self) -> MultipartResource:
        """Secure document storage with semantic search"""
        return MultipartResource(self._client)

    @cached_property
    def objects(self) -> ObjectsResource:
        """Vault object management, content access, and document operations"""
        return ObjectsResource(self._client)

    @cached_property
    def memory(self) -> MemoryResource:
        """Vault-scoped persistent memory and semantic retrieval"""
        return MemoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> VaultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return VaultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VaultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return VaultResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        embedding_model: Literal[
            "openai/text-embedding-3-small",
            "openai/text-embedding-3-large",
            "voyage/voyage-3.5",
            "voyage/voyage-law-2",
            "cohere/embed-v4.0",
            "google/gemini-embedding-2",
            "casemark/embed-v1",
            "casemark/llama-nemotron-embed-vl-1b-v2",
        ]
        | Omit = omit,
        enable_indexing: bool | Omit = omit,
        group_id: str | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultCreateResponse:
        """
        Creates a new secure vault with dedicated S3 storage and vector search
        capabilities. Each vault provides isolated document storage with semantic search
        and OCR processing for legal document analysis and discovery.

        Args:
          name: Display name for the vault

          description: Optional description of the vault's purpose

          embedding_model: Optional embedding model for this vault. Defaults to casemark/embed-v1.
              Determines the S3 Vectors index dimension and which model is used at both ingest
              and search time. The vault is locked to this model after creation — use a
              re-embed flow to change later. Ignored when enableIndexing is false. Note:
              `casemark/llama-nemotron-embed-vl-1b-v2` is a deprecated alias for
              `casemark/embed-v1` (retained for SDK backward compatibility); new integrations
              should use `casemark/embed-v1` directly.

          enable_indexing: Enable vector indexing and search capabilities. Set to false for storage-only
              vaults.

          group_id: Assign the vault to a vault group for access control. Required when using a
              group-scoped API key.

          metadata: Optional metadata to attach to the vault (e.g., { containsPHI: true } for HIPAA
              compliance tracking)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/vault",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "embedding_model": embedding_model,
                    "enable_indexing": enable_indexing,
                    "group_id": group_id,
                    "metadata": metadata,
                },
                vault_create_params.VaultCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultRetrieveResponse:
        """
        Retrieve detailed information about a specific vault, including storage
        configuration, chunking strategy, and usage statistics. Returns vault metadata,
        bucket information, and vector storage details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/vault/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultUpdateResponse:
        """
        Update vault settings including name, description, and group membership.

        Args:
          description: New description for the vault. Set to null to remove.

          group_id: Move the vault to a different group, or set to null to remove from its current
              group.

          name: New name for the vault

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/vault/{id}", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "group_id": group_id,
                    "name": name,
                },
                vault_update_params.VaultUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        include_totals: bool | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultListResponse:
        """List all vaults for the authenticated organization.

        Returns vault metadata
        including name, description, storage configuration, and usage statistics.
        Pagination is opt-in: pass `limit` (1-200) to receive a bounded page, then
        replay `pagination.next_cursor` as `?cursor=` while `pagination.has_more` is
        true. A request with neither `limit` nor `cursor` still returns every vault, and
        `pagination.limit` is null. That default will become a bounded page in a future
        release — paginate now to avoid the change.

        Args:
          cursor: Opaque continuation cursor from `pagination.next_cursor` of the previous page.
              Must be replayed with the same API key scope and `query` that produced it.

          include_totals: When `true`, adds `totals` covering every vault matching the filters, not just
              this page. Scans all objects in those vaults, so request it once per filter
              change rather than on every page.

          limit: Vaults per page (1-200). Omit to receive every vault. Supplying a cursor without
              a limit uses 50.

          query: Case-insensitive substring match on the vault name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/vault",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_totals": include_totals,
                        "limit": limit,
                        "query": query,
                    },
                    vault_list_params.VaultListParams,
                ),
            ),
            cast_to=VaultListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        async_: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultDeleteResponse:
        """
        Permanently deletes a vault and all its contents including documents, vectors,
        graph data, and S3 buckets. This operation cannot be undone. For large vaults,
        use the async=true query parameter to queue deletion in the background.

        Args:
          async_: If true and vault has many objects, queue deletion in background and return
              immediately

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/vault/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"async_": async_}, vault_delete_params.VaultDeleteParams),
            ),
            cast_to=VaultDeleteResponse,
        )

    def confirm_upload(
        self,
        object_id: str,
        *,
        id: str,
        success: bool,
        auto_ingest: bool | Omit = omit,
        error_code: str | Omit = omit,
        error_message: str | Omit = omit,
        etag: str | Omit = omit,
        size_bytes: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultConfirmUploadResponse:
        """Confirm whether a direct-to-S3 vault upload succeeded or failed.

        This endpoint
        emits vault.upload.completed or vault.upload.failed events and is idempotent for
        repeated confirmations. Conditional fields: when success=true, sizeBytes is
        required; when success=false, errorCode and errorMessage are required. These
        rules are enforced server-side with specific 400 responses.

        Args:
          success: Whether the upload succeeded

          auto_ingest: When true and the object was uploaded with auto_index, trigger ingestion
              immediately after a successful confirmation (no separate ingest call needed).
              The ingest outcome is reported in the `ingest` response field; an ingest failure
              does not fail the confirmation.

          error_code: Client-side error code. Required when success=false.

          error_message: Client-side error message. Required when success=false.

          etag: S3 ETag for the uploaded object (optional if client cannot access ETag header).
              Only meaningful when success=true.

          size_bytes: Uploaded file size in bytes, including zero. Required when success=true and
              verified against S3. Empty files can be stored and transferred, but cannot be
              ingested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._post(
            path_template("/vault/{id}/upload/{object_id}/confirm", id=id, object_id=object_id),
            body=maybe_transform(
                {
                    "success": success,
                    "auto_ingest": auto_ingest,
                    "error_code": error_code,
                    "error_message": error_message,
                    "etag": etag,
                    "size_bytes": size_bytes,
                },
                vault_confirm_upload_params.VaultConfirmUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultConfirmUploadResponse,
        )

    def ingest(
        self,
        object_id: str,
        *,
        id: str,
        callback_url: str | Omit = omit,
        page_boundaries: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultIngestResponse:
        """
        Triggers ingestion workflow for a vault object to extract text, generate chunks,
        and create embeddings. For supported file types (PDF, DOCX, PPTX, XLSX, TXT,
        RTF, XML, HTML, Markdown, CSV/TSV, JSON/YAML/TOML, common source code files,
        ZIP, audio, video), processing happens asynchronously. ZIP archives always
        return a processing response, are unpacked recursively up to 5 levels, and each
        extracted file is created as an independent vault object and ingested via the
        normal pipeline. For unsupported types (images, etc.), the file is marked as
        completed immediately without text extraction.

        Args:
          callback_url: Optional callback URL for asynchronous workflow completion.

          page_boundaries: Optional PDF pages that must begin a new chunk segment. Overlap never crosses
              these boundaries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._post(
            path_template("/vault/{id}/ingest/{object_id}", id=id, object_id=object_id),
            body=maybe_transform(
                {
                    "callback_url": callback_url,
                    "page_boundaries": page_boundaries,
                },
                vault_ingest_params.VaultIngestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultIngestResponse,
        )

    def search(
        self,
        id: str,
        *,
        query: str,
        filters: vault_search_params.Filters | Omit = omit,
        method: Literal["hybrid", "fast", "vector"] | Omit = omit,
        top_k: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultSearchResponse:
        """
        Search across vault documents using hybrid vector + BM25 search (default), fast
        vector similarity search, or a simple vector fallback. Returns matching chunks
        and their source documents.

        Args:
          query: Search query or question to find relevant documents

          filters: Filters to narrow search results to specific documents

          method: Search method: 'hybrid' for combined vector + keyword ranking (default), 'fast'
              for quick vector similarity search, 'vector' for a simple document listing
              fallback

          top_k: Maximum number of results to return. Hybrid search supports 1 to 50; other
              methods may support up to 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/vault/{id}/search", id=id),
            body=maybe_transform(
                {
                    "query": query,
                    "filters": filters,
                    "method": method,
                    "top_k": top_k,
                },
                vault_search_params.VaultSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultSearchResponse,
        )

    def upload(
        self,
        id: str,
        *,
        content_type: str,
        filename: str,
        auto_index: bool | Omit = omit,
        file_origin: Dict[str, object] | Omit = omit,
        is_ai_generated: bool | Omit = omit,
        metadata: object | Omit = omit,
        path: str | Omit = omit,
        size_bytes: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultUploadResponse:
        """
        Generate a presigned URL for uploading files directly to a vault's S3 storage.
        After uploading to S3, confirm the upload result via POST
        /vault/:vaultId/upload/:objectId/confirm before triggering ingestion.

        Args:
          content_type: MIME type of the file (e.g., application/pdf, image/jpeg)

          filename: Name of the file to upload

          auto_index: Whether to automatically process and index the file for search

          file_origin: Optional client-defined provenance metadata. Returned with the object and
              queryable through the object-list API.

          is_ai_generated: Marks the file as AI-generated work product (e.g. uploaded by an agent) rather
              than a user-provided source document. Persisted on the object and returned by
              object listings so clients can distinguish provenance.

          metadata: Additional metadata to associate with the file

          path: Optional folder path, excluding the filename, for hierarchy preservation. Allows
              integrations to maintain source folder structure from systems like NetDocs,
              Clio, or Smokeball. Example: '/Discovery/Depositions/2024'

          size_bytes: File size in bytes (optional, including zero, max 5GB for single PUT uploads).
              When provided, enforces exact file size at S3 level. Empty files can be stored
              and transferred, but cannot be ingested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/vault/{id}/upload", id=id),
            body=maybe_transform(
                {
                    "content_type": content_type,
                    "filename": filename,
                    "auto_index": auto_index,
                    "file_origin": file_origin,
                    "is_ai_generated": is_ai_generated,
                    "metadata": metadata,
                    "path": path,
                    "size_bytes": size_bytes,
                },
                vault_upload_params.VaultUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultUploadResponse,
        )


class AsyncVaultResource(AsyncAPIResource):
    """Secure document storage with semantic search"""

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        """Secure document storage with semantic search"""
        return AsyncGroupsResource(self._client)

    @cached_property
    def multipart(self) -> AsyncMultipartResource:
        """Secure document storage with semantic search"""
        return AsyncMultipartResource(self._client)

    @cached_property
    def objects(self) -> AsyncObjectsResource:
        """Vault object management, content access, and document operations"""
        return AsyncObjectsResource(self._client)

    @cached_property
    def memory(self) -> AsyncMemoryResource:
        """Vault-scoped persistent memory and semantic retrieval"""
        return AsyncMemoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVaultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVaultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVaultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncVaultResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        embedding_model: Literal[
            "openai/text-embedding-3-small",
            "openai/text-embedding-3-large",
            "voyage/voyage-3.5",
            "voyage/voyage-law-2",
            "cohere/embed-v4.0",
            "google/gemini-embedding-2",
            "casemark/embed-v1",
            "casemark/llama-nemotron-embed-vl-1b-v2",
        ]
        | Omit = omit,
        enable_indexing: bool | Omit = omit,
        group_id: str | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultCreateResponse:
        """
        Creates a new secure vault with dedicated S3 storage and vector search
        capabilities. Each vault provides isolated document storage with semantic search
        and OCR processing for legal document analysis and discovery.

        Args:
          name: Display name for the vault

          description: Optional description of the vault's purpose

          embedding_model: Optional embedding model for this vault. Defaults to casemark/embed-v1.
              Determines the S3 Vectors index dimension and which model is used at both ingest
              and search time. The vault is locked to this model after creation — use a
              re-embed flow to change later. Ignored when enableIndexing is false. Note:
              `casemark/llama-nemotron-embed-vl-1b-v2` is a deprecated alias for
              `casemark/embed-v1` (retained for SDK backward compatibility); new integrations
              should use `casemark/embed-v1` directly.

          enable_indexing: Enable vector indexing and search capabilities. Set to false for storage-only
              vaults.

          group_id: Assign the vault to a vault group for access control. Required when using a
              group-scoped API key.

          metadata: Optional metadata to attach to the vault (e.g., { containsPHI: true } for HIPAA
              compliance tracking)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/vault",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "embedding_model": embedding_model,
                    "enable_indexing": enable_indexing,
                    "group_id": group_id,
                    "metadata": metadata,
                },
                vault_create_params.VaultCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultRetrieveResponse:
        """
        Retrieve detailed information about a specific vault, including storage
        configuration, chunking strategy, and usage statistics. Returns vault metadata,
        bucket information, and vector storage details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/vault/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultUpdateResponse:
        """
        Update vault settings including name, description, and group membership.

        Args:
          description: New description for the vault. Set to null to remove.

          group_id: Move the vault to a different group, or set to null to remove from its current
              group.

          name: New name for the vault

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/vault/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "group_id": group_id,
                    "name": name,
                },
                vault_update_params.VaultUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultUpdateResponse,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        include_totals: bool | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultListResponse:
        """List all vaults for the authenticated organization.

        Returns vault metadata
        including name, description, storage configuration, and usage statistics.
        Pagination is opt-in: pass `limit` (1-200) to receive a bounded page, then
        replay `pagination.next_cursor` as `?cursor=` while `pagination.has_more` is
        true. A request with neither `limit` nor `cursor` still returns every vault, and
        `pagination.limit` is null. That default will become a bounded page in a future
        release — paginate now to avoid the change.

        Args:
          cursor: Opaque continuation cursor from `pagination.next_cursor` of the previous page.
              Must be replayed with the same API key scope and `query` that produced it.

          include_totals: When `true`, adds `totals` covering every vault matching the filters, not just
              this page. Scans all objects in those vaults, so request it once per filter
              change rather than on every page.

          limit: Vaults per page (1-200). Omit to receive every vault. Supplying a cursor without
              a limit uses 50.

          query: Case-insensitive substring match on the vault name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/vault",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "include_totals": include_totals,
                        "limit": limit,
                        "query": query,
                    },
                    vault_list_params.VaultListParams,
                ),
            ),
            cast_to=VaultListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        async_: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultDeleteResponse:
        """
        Permanently deletes a vault and all its contents including documents, vectors,
        graph data, and S3 buckets. This operation cannot be undone. For large vaults,
        use the async=true query parameter to queue deletion in the background.

        Args:
          async_: If true and vault has many objects, queue deletion in background and return
              immediately

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/vault/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"async_": async_}, vault_delete_params.VaultDeleteParams),
            ),
            cast_to=VaultDeleteResponse,
        )

    async def confirm_upload(
        self,
        object_id: str,
        *,
        id: str,
        success: bool,
        auto_ingest: bool | Omit = omit,
        error_code: str | Omit = omit,
        error_message: str | Omit = omit,
        etag: str | Omit = omit,
        size_bytes: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultConfirmUploadResponse:
        """Confirm whether a direct-to-S3 vault upload succeeded or failed.

        This endpoint
        emits vault.upload.completed or vault.upload.failed events and is idempotent for
        repeated confirmations. Conditional fields: when success=true, sizeBytes is
        required; when success=false, errorCode and errorMessage are required. These
        rules are enforced server-side with specific 400 responses.

        Args:
          success: Whether the upload succeeded

          auto_ingest: When true and the object was uploaded with auto_index, trigger ingestion
              immediately after a successful confirmation (no separate ingest call needed).
              The ingest outcome is reported in the `ingest` response field; an ingest failure
              does not fail the confirmation.

          error_code: Client-side error code. Required when success=false.

          error_message: Client-side error message. Required when success=false.

          etag: S3 ETag for the uploaded object (optional if client cannot access ETag header).
              Only meaningful when success=true.

          size_bytes: Uploaded file size in bytes, including zero. Required when success=true and
              verified against S3. Empty files can be stored and transferred, but cannot be
              ingested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._post(
            path_template("/vault/{id}/upload/{object_id}/confirm", id=id, object_id=object_id),
            body=await async_maybe_transform(
                {
                    "success": success,
                    "auto_ingest": auto_ingest,
                    "error_code": error_code,
                    "error_message": error_message,
                    "etag": etag,
                    "size_bytes": size_bytes,
                },
                vault_confirm_upload_params.VaultConfirmUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultConfirmUploadResponse,
        )

    async def ingest(
        self,
        object_id: str,
        *,
        id: str,
        callback_url: str | Omit = omit,
        page_boundaries: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultIngestResponse:
        """
        Triggers ingestion workflow for a vault object to extract text, generate chunks,
        and create embeddings. For supported file types (PDF, DOCX, PPTX, XLSX, TXT,
        RTF, XML, HTML, Markdown, CSV/TSV, JSON/YAML/TOML, common source code files,
        ZIP, audio, video), processing happens asynchronously. ZIP archives always
        return a processing response, are unpacked recursively up to 5 levels, and each
        extracted file is created as an independent vault object and ingested via the
        normal pipeline. For unsupported types (images, etc.), the file is marked as
        completed immediately without text extraction.

        Args:
          callback_url: Optional callback URL for asynchronous workflow completion.

          page_boundaries: Optional PDF pages that must begin a new chunk segment. Overlap never crosses
              these boundaries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._post(
            path_template("/vault/{id}/ingest/{object_id}", id=id, object_id=object_id),
            body=await async_maybe_transform(
                {
                    "callback_url": callback_url,
                    "page_boundaries": page_boundaries,
                },
                vault_ingest_params.VaultIngestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultIngestResponse,
        )

    async def search(
        self,
        id: str,
        *,
        query: str,
        filters: vault_search_params.Filters | Omit = omit,
        method: Literal["hybrid", "fast", "vector"] | Omit = omit,
        top_k: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultSearchResponse:
        """
        Search across vault documents using hybrid vector + BM25 search (default), fast
        vector similarity search, or a simple vector fallback. Returns matching chunks
        and their source documents.

        Args:
          query: Search query or question to find relevant documents

          filters: Filters to narrow search results to specific documents

          method: Search method: 'hybrid' for combined vector + keyword ranking (default), 'fast'
              for quick vector similarity search, 'vector' for a simple document listing
              fallback

          top_k: Maximum number of results to return. Hybrid search supports 1 to 50; other
              methods may support up to 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/vault/{id}/search", id=id),
            body=await async_maybe_transform(
                {
                    "query": query,
                    "filters": filters,
                    "method": method,
                    "top_k": top_k,
                },
                vault_search_params.VaultSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultSearchResponse,
        )

    async def upload(
        self,
        id: str,
        *,
        content_type: str,
        filename: str,
        auto_index: bool | Omit = omit,
        file_origin: Dict[str, object] | Omit = omit,
        is_ai_generated: bool | Omit = omit,
        metadata: object | Omit = omit,
        path: str | Omit = omit,
        size_bytes: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultUploadResponse:
        """
        Generate a presigned URL for uploading files directly to a vault's S3 storage.
        After uploading to S3, confirm the upload result via POST
        /vault/:vaultId/upload/:objectId/confirm before triggering ingestion.

        Args:
          content_type: MIME type of the file (e.g., application/pdf, image/jpeg)

          filename: Name of the file to upload

          auto_index: Whether to automatically process and index the file for search

          file_origin: Optional client-defined provenance metadata. Returned with the object and
              queryable through the object-list API.

          is_ai_generated: Marks the file as AI-generated work product (e.g. uploaded by an agent) rather
              than a user-provided source document. Persisted on the object and returned by
              object listings so clients can distinguish provenance.

          metadata: Additional metadata to associate with the file

          path: Optional folder path, excluding the filename, for hierarchy preservation. Allows
              integrations to maintain source folder structure from systems like NetDocs,
              Clio, or Smokeball. Example: '/Discovery/Depositions/2024'

          size_bytes: File size in bytes (optional, including zero, max 5GB for single PUT uploads).
              When provided, enforces exact file size at S3 level. Empty files can be stored
              and transferred, but cannot be ingested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/vault/{id}/upload", id=id),
            body=await async_maybe_transform(
                {
                    "content_type": content_type,
                    "filename": filename,
                    "auto_index": auto_index,
                    "file_origin": file_origin,
                    "is_ai_generated": is_ai_generated,
                    "metadata": metadata,
                    "path": path,
                    "size_bytes": size_bytes,
                },
                vault_upload_params.VaultUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultUploadResponse,
        )


class VaultResourceWithRawResponse:
    def __init__(self, vault: VaultResource) -> None:
        self._vault = vault

        self.create = to_raw_response_wrapper(
            vault.create,
        )
        self.retrieve = to_raw_response_wrapper(
            vault.retrieve,
        )
        self.update = to_raw_response_wrapper(
            vault.update,
        )
        self.list = to_raw_response_wrapper(
            vault.list,
        )
        self.delete = to_raw_response_wrapper(
            vault.delete,
        )
        self.confirm_upload = to_raw_response_wrapper(
            vault.confirm_upload,
        )
        self.ingest = to_raw_response_wrapper(
            vault.ingest,
        )
        self.search = to_raw_response_wrapper(
            vault.search,
        )
        self.upload = to_raw_response_wrapper(
            vault.upload,
        )

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._vault.events)

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        """Secure document storage with semantic search"""
        return GroupsResourceWithRawResponse(self._vault.groups)

    @cached_property
    def multipart(self) -> MultipartResourceWithRawResponse:
        """Secure document storage with semantic search"""
        return MultipartResourceWithRawResponse(self._vault.multipart)

    @cached_property
    def objects(self) -> ObjectsResourceWithRawResponse:
        """Vault object management, content access, and document operations"""
        return ObjectsResourceWithRawResponse(self._vault.objects)

    @cached_property
    def memory(self) -> MemoryResourceWithRawResponse:
        """Vault-scoped persistent memory and semantic retrieval"""
        return MemoryResourceWithRawResponse(self._vault.memory)


class AsyncVaultResourceWithRawResponse:
    def __init__(self, vault: AsyncVaultResource) -> None:
        self._vault = vault

        self.create = async_to_raw_response_wrapper(
            vault.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            vault.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            vault.update,
        )
        self.list = async_to_raw_response_wrapper(
            vault.list,
        )
        self.delete = async_to_raw_response_wrapper(
            vault.delete,
        )
        self.confirm_upload = async_to_raw_response_wrapper(
            vault.confirm_upload,
        )
        self.ingest = async_to_raw_response_wrapper(
            vault.ingest,
        )
        self.search = async_to_raw_response_wrapper(
            vault.search,
        )
        self.upload = async_to_raw_response_wrapper(
            vault.upload,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._vault.events)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        """Secure document storage with semantic search"""
        return AsyncGroupsResourceWithRawResponse(self._vault.groups)

    @cached_property
    def multipart(self) -> AsyncMultipartResourceWithRawResponse:
        """Secure document storage with semantic search"""
        return AsyncMultipartResourceWithRawResponse(self._vault.multipart)

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithRawResponse:
        """Vault object management, content access, and document operations"""
        return AsyncObjectsResourceWithRawResponse(self._vault.objects)

    @cached_property
    def memory(self) -> AsyncMemoryResourceWithRawResponse:
        """Vault-scoped persistent memory and semantic retrieval"""
        return AsyncMemoryResourceWithRawResponse(self._vault.memory)


class VaultResourceWithStreamingResponse:
    def __init__(self, vault: VaultResource) -> None:
        self._vault = vault

        self.create = to_streamed_response_wrapper(
            vault.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            vault.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            vault.update,
        )
        self.list = to_streamed_response_wrapper(
            vault.list,
        )
        self.delete = to_streamed_response_wrapper(
            vault.delete,
        )
        self.confirm_upload = to_streamed_response_wrapper(
            vault.confirm_upload,
        )
        self.ingest = to_streamed_response_wrapper(
            vault.ingest,
        )
        self.search = to_streamed_response_wrapper(
            vault.search,
        )
        self.upload = to_streamed_response_wrapper(
            vault.upload,
        )

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._vault.events)

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        """Secure document storage with semantic search"""
        return GroupsResourceWithStreamingResponse(self._vault.groups)

    @cached_property
    def multipart(self) -> MultipartResourceWithStreamingResponse:
        """Secure document storage with semantic search"""
        return MultipartResourceWithStreamingResponse(self._vault.multipart)

    @cached_property
    def objects(self) -> ObjectsResourceWithStreamingResponse:
        """Vault object management, content access, and document operations"""
        return ObjectsResourceWithStreamingResponse(self._vault.objects)

    @cached_property
    def memory(self) -> MemoryResourceWithStreamingResponse:
        """Vault-scoped persistent memory and semantic retrieval"""
        return MemoryResourceWithStreamingResponse(self._vault.memory)


class AsyncVaultResourceWithStreamingResponse:
    def __init__(self, vault: AsyncVaultResource) -> None:
        self._vault = vault

        self.create = async_to_streamed_response_wrapper(
            vault.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            vault.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            vault.update,
        )
        self.list = async_to_streamed_response_wrapper(
            vault.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            vault.delete,
        )
        self.confirm_upload = async_to_streamed_response_wrapper(
            vault.confirm_upload,
        )
        self.ingest = async_to_streamed_response_wrapper(
            vault.ingest,
        )
        self.search = async_to_streamed_response_wrapper(
            vault.search,
        )
        self.upload = async_to_streamed_response_wrapper(
            vault.upload,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._vault.events)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        """Secure document storage with semantic search"""
        return AsyncGroupsResourceWithStreamingResponse(self._vault.groups)

    @cached_property
    def multipart(self) -> AsyncMultipartResourceWithStreamingResponse:
        """Secure document storage with semantic search"""
        return AsyncMultipartResourceWithStreamingResponse(self._vault.multipart)

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithStreamingResponse:
        """Vault object management, content access, and document operations"""
        return AsyncObjectsResourceWithStreamingResponse(self._vault.objects)

    @cached_property
    def memory(self) -> AsyncMemoryResourceWithStreamingResponse:
        """Vault-scoped persistent memory and semantic retrieval"""
        return AsyncMemoryResourceWithStreamingResponse(self._vault.memory)
