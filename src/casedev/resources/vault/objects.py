# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.vault import (
    object_delete_params,
    object_update_params,
    object_get_ocr_words_params,
    object_create_presigned_url_params,
)
from ..._base_client import make_request_options
from ...types.vault.object_list_response import ObjectListResponse
from ...types.vault.object_delete_response import ObjectDeleteResponse
from ...types.vault.object_update_response import ObjectUpdateResponse
from ...types.vault.object_get_text_response import ObjectGetTextResponse
from ...types.vault.object_retrieve_response import ObjectRetrieveResponse
from ...types.vault.object_get_ocr_words_response import ObjectGetOcrWordsResponse
from ...types.vault.object_get_summarize_job_response import ObjectGetSummarizeJobResponse
from ...types.vault.object_create_presigned_url_response import ObjectCreatePresignedURLResponse

__all__ = ["ObjectsResource", "AsyncObjectsResource"]


class ObjectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return ObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return ObjectsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        object_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectRetrieveResponse:
        """
        Retrieves metadata for a specific document in a vault and generates a temporary
        download URL. The download URL expires after 1 hour for security. This endpoint
        also updates the file size if it wasn't previously calculated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            f"/vault/{id}/objects/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectRetrieveResponse,
        )

    def update(
        self,
        object_id: str,
        *,
        id: str,
        filename: str | Omit = omit,
        metadata: object | Omit = omit,
        path: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectUpdateResponse:
        """Update a document's filename, path, or metadata.

        Use this to rename files or
        organize them into virtual folders. The path is stored in metadata.path and can
        be used to build folder hierarchies in your application.

        Args:
          filename: New filename for the document (affects display name and downloads)

          metadata: Additional metadata to merge with existing metadata

          path: Folder path for hierarchy preservation (e.g., '/Discovery/Depositions'). Set to
              null or empty string to remove.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._patch(
            f"/vault/{id}/objects/{object_id}",
            body=maybe_transform(
                {
                    "filename": filename,
                    "metadata": metadata,
                    "path": path,
                },
                object_update_params.ObjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectUpdateResponse,
        )

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectListResponse:
        """
        Retrieve all objects stored in a specific vault, including document metadata,
        ingestion status, and processing statistics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/vault/{id}/objects",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectListResponse,
        )

    def delete(
        self,
        object_id: str,
        *,
        id: str,
        force: Literal["true"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectDeleteResponse:
        """
        Permanently deletes a document from the vault including all associated vectors,
        chunks, graph data, and the original file. This operation cannot be undone.

        Args:
          force: Force delete a stuck document that is still in 'processing' state. Use this if a
              document got stuck during ingestion (e.g., OCR timeout).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._delete(
            f"/vault/{id}/objects/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force": force}, object_delete_params.ObjectDeleteParams),
            ),
            cast_to=ObjectDeleteResponse,
        )

    def create_presigned_url(
        self,
        object_id: str,
        *,
        id: str,
        content_type: str | Omit = omit,
        expires_in: int | Omit = omit,
        operation: Literal["GET", "PUT", "DELETE", "HEAD"] | Omit = omit,
        size_bytes: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectCreatePresignedURLResponse:
        """
        Generate presigned URLs for direct S3 operations (GET, PUT, DELETE, HEAD) on
        vault objects. This allows secure, time-limited access to files without proxying
        through the API. Essential for large document uploads/downloads in legal
        workflows.

        Args:
          content_type: Content type for PUT operations (optional, defaults to object's content type)

          expires_in: URL expiration time in seconds (1 minute to 7 days)

          operation: The S3 operation to generate URL for

          size_bytes: File size in bytes (optional, max 5GB for single PUT uploads). When provided for
              PUT operations, enforces exact file size at S3 level.

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
            f"/vault/{id}/objects/{object_id}/presigned-url",
            body=maybe_transform(
                {
                    "content_type": content_type,
                    "expires_in": expires_in,
                    "operation": operation,
                    "size_bytes": size_bytes,
                },
                object_create_presigned_url_params.ObjectCreatePresignedURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectCreatePresignedURLResponse,
        )

    def download(
        self,
        object_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Downloads a file from a vault.

        Returns the actual file content as a binary
        stream with appropriate headers for file download. Useful for retrieving
        contracts, depositions, case files, and other legal documents stored in your
        vault.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            f"/vault/{id}/objects/{object_id}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def get_ocr_words(
        self,
        object_id: str,
        *,
        id: str,
        page: int | Omit = omit,
        word_end: int | Omit = omit,
        word_start: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectGetOcrWordsResponse:
        """Retrieves word-level OCR bounding box data for a processed PDF document.

        Each
        word includes its text, normalized bounding box coordinates (0-1 range),
        confidence score, and global word index. Use this data to highlight specific
        text ranges in a PDF viewer based on word indices from search results.

        Args:
          page: Filter to a specific page number (1-indexed). If omitted, returns all pages.

          word_end: Filter to words ending at this index (inclusive). Useful for retrieving words
              for a specific chunk.

          word_start: Filter to words starting at this index (inclusive). Useful for retrieving words
              for a specific chunk.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            f"/vault/{id}/objects/{object_id}/ocr-words",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "word_end": word_end,
                        "word_start": word_start,
                    },
                    object_get_ocr_words_params.ObjectGetOcrWordsParams,
                ),
            ),
            cast_to=ObjectGetOcrWordsResponse,
        )

    def get_summarize_job(
        self,
        job_id: str,
        *,
        id: str,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectGetSummarizeJobResponse:
        """Get the status of a CaseMark summary workflow job.

        If the job has been
        processing for too long, this endpoint will poll CaseMark directly to recover
        stuck jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/vault/{id}/objects/{object_id}/summarize/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectGetSummarizeJobResponse,
        )

    def get_text(
        self,
        object_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectGetTextResponse:
        """Retrieves the full extracted text content from a processed vault object.

        Returns
        the concatenated text from all chunks, useful for document review, analysis, or
        export. The object must have completed processing before text can be retrieved.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            f"/vault/{id}/objects/{object_id}/text",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectGetTextResponse,
        )


class AsyncObjectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncObjectsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        object_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectRetrieveResponse:
        """
        Retrieves metadata for a specific document in a vault and generates a temporary
        download URL. The download URL expires after 1 hour for security. This endpoint
        also updates the file size if it wasn't previously calculated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            f"/vault/{id}/objects/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectRetrieveResponse,
        )

    async def update(
        self,
        object_id: str,
        *,
        id: str,
        filename: str | Omit = omit,
        metadata: object | Omit = omit,
        path: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectUpdateResponse:
        """Update a document's filename, path, or metadata.

        Use this to rename files or
        organize them into virtual folders. The path is stored in metadata.path and can
        be used to build folder hierarchies in your application.

        Args:
          filename: New filename for the document (affects display name and downloads)

          metadata: Additional metadata to merge with existing metadata

          path: Folder path for hierarchy preservation (e.g., '/Discovery/Depositions'). Set to
              null or empty string to remove.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._patch(
            f"/vault/{id}/objects/{object_id}",
            body=await async_maybe_transform(
                {
                    "filename": filename,
                    "metadata": metadata,
                    "path": path,
                },
                object_update_params.ObjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectUpdateResponse,
        )

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectListResponse:
        """
        Retrieve all objects stored in a specific vault, including document metadata,
        ingestion status, and processing statistics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/vault/{id}/objects",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectListResponse,
        )

    async def delete(
        self,
        object_id: str,
        *,
        id: str,
        force: Literal["true"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectDeleteResponse:
        """
        Permanently deletes a document from the vault including all associated vectors,
        chunks, graph data, and the original file. This operation cannot be undone.

        Args:
          force: Force delete a stuck document that is still in 'processing' state. Use this if a
              document got stuck during ingestion (e.g., OCR timeout).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._delete(
            f"/vault/{id}/objects/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"force": force}, object_delete_params.ObjectDeleteParams),
            ),
            cast_to=ObjectDeleteResponse,
        )

    async def create_presigned_url(
        self,
        object_id: str,
        *,
        id: str,
        content_type: str | Omit = omit,
        expires_in: int | Omit = omit,
        operation: Literal["GET", "PUT", "DELETE", "HEAD"] | Omit = omit,
        size_bytes: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectCreatePresignedURLResponse:
        """
        Generate presigned URLs for direct S3 operations (GET, PUT, DELETE, HEAD) on
        vault objects. This allows secure, time-limited access to files without proxying
        through the API. Essential for large document uploads/downloads in legal
        workflows.

        Args:
          content_type: Content type for PUT operations (optional, defaults to object's content type)

          expires_in: URL expiration time in seconds (1 minute to 7 days)

          operation: The S3 operation to generate URL for

          size_bytes: File size in bytes (optional, max 5GB for single PUT uploads). When provided for
              PUT operations, enforces exact file size at S3 level.

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
            f"/vault/{id}/objects/{object_id}/presigned-url",
            body=await async_maybe_transform(
                {
                    "content_type": content_type,
                    "expires_in": expires_in,
                    "operation": operation,
                    "size_bytes": size_bytes,
                },
                object_create_presigned_url_params.ObjectCreatePresignedURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectCreatePresignedURLResponse,
        )

    async def download(
        self,
        object_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Downloads a file from a vault.

        Returns the actual file content as a binary
        stream with appropriate headers for file download. Useful for retrieving
        contracts, depositions, case files, and other legal documents stored in your
        vault.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            f"/vault/{id}/objects/{object_id}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def get_ocr_words(
        self,
        object_id: str,
        *,
        id: str,
        page: int | Omit = omit,
        word_end: int | Omit = omit,
        word_start: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectGetOcrWordsResponse:
        """Retrieves word-level OCR bounding box data for a processed PDF document.

        Each
        word includes its text, normalized bounding box coordinates (0-1 range),
        confidence score, and global word index. Use this data to highlight specific
        text ranges in a PDF viewer based on word indices from search results.

        Args:
          page: Filter to a specific page number (1-indexed). If omitted, returns all pages.

          word_end: Filter to words ending at this index (inclusive). Useful for retrieving words
              for a specific chunk.

          word_start: Filter to words starting at this index (inclusive). Useful for retrieving words
              for a specific chunk.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            f"/vault/{id}/objects/{object_id}/ocr-words",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "word_end": word_end,
                        "word_start": word_start,
                    },
                    object_get_ocr_words_params.ObjectGetOcrWordsParams,
                ),
            ),
            cast_to=ObjectGetOcrWordsResponse,
        )

    async def get_summarize_job(
        self,
        job_id: str,
        *,
        id: str,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectGetSummarizeJobResponse:
        """Get the status of a CaseMark summary workflow job.

        If the job has been
        processing for too long, this endpoint will poll CaseMark directly to recover
        stuck jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/vault/{id}/objects/{object_id}/summarize/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectGetSummarizeJobResponse,
        )

    async def get_text(
        self,
        object_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectGetTextResponse:
        """Retrieves the full extracted text content from a processed vault object.

        Returns
        the concatenated text from all chunks, useful for document review, analysis, or
        export. The object must have completed processing before text can be retrieved.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            f"/vault/{id}/objects/{object_id}/text",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectGetTextResponse,
        )


class ObjectsResourceWithRawResponse:
    def __init__(self, objects: ObjectsResource) -> None:
        self._objects = objects

        self.retrieve = to_raw_response_wrapper(
            objects.retrieve,
        )
        self.update = to_raw_response_wrapper(
            objects.update,
        )
        self.list = to_raw_response_wrapper(
            objects.list,
        )
        self.delete = to_raw_response_wrapper(
            objects.delete,
        )
        self.create_presigned_url = to_raw_response_wrapper(
            objects.create_presigned_url,
        )
        self.download = to_raw_response_wrapper(
            objects.download,
        )
        self.get_ocr_words = to_raw_response_wrapper(
            objects.get_ocr_words,
        )
        self.get_summarize_job = to_raw_response_wrapper(
            objects.get_summarize_job,
        )
        self.get_text = to_raw_response_wrapper(
            objects.get_text,
        )


class AsyncObjectsResourceWithRawResponse:
    def __init__(self, objects: AsyncObjectsResource) -> None:
        self._objects = objects

        self.retrieve = async_to_raw_response_wrapper(
            objects.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            objects.update,
        )
        self.list = async_to_raw_response_wrapper(
            objects.list,
        )
        self.delete = async_to_raw_response_wrapper(
            objects.delete,
        )
        self.create_presigned_url = async_to_raw_response_wrapper(
            objects.create_presigned_url,
        )
        self.download = async_to_raw_response_wrapper(
            objects.download,
        )
        self.get_ocr_words = async_to_raw_response_wrapper(
            objects.get_ocr_words,
        )
        self.get_summarize_job = async_to_raw_response_wrapper(
            objects.get_summarize_job,
        )
        self.get_text = async_to_raw_response_wrapper(
            objects.get_text,
        )


class ObjectsResourceWithStreamingResponse:
    def __init__(self, objects: ObjectsResource) -> None:
        self._objects = objects

        self.retrieve = to_streamed_response_wrapper(
            objects.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            objects.update,
        )
        self.list = to_streamed_response_wrapper(
            objects.list,
        )
        self.delete = to_streamed_response_wrapper(
            objects.delete,
        )
        self.create_presigned_url = to_streamed_response_wrapper(
            objects.create_presigned_url,
        )
        self.download = to_streamed_response_wrapper(
            objects.download,
        )
        self.get_ocr_words = to_streamed_response_wrapper(
            objects.get_ocr_words,
        )
        self.get_summarize_job = to_streamed_response_wrapper(
            objects.get_summarize_job,
        )
        self.get_text = to_streamed_response_wrapper(
            objects.get_text,
        )


class AsyncObjectsResourceWithStreamingResponse:
    def __init__(self, objects: AsyncObjectsResource) -> None:
        self._objects = objects

        self.retrieve = async_to_streamed_response_wrapper(
            objects.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            objects.update,
        )
        self.list = async_to_streamed_response_wrapper(
            objects.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            objects.delete,
        )
        self.create_presigned_url = async_to_streamed_response_wrapper(
            objects.create_presigned_url,
        )
        self.download = async_to_streamed_response_wrapper(
            objects.download,
        )
        self.get_ocr_words = async_to_streamed_response_wrapper(
            objects.get_ocr_words,
        )
        self.get_summarize_job = async_to_streamed_response_wrapper(
            objects.get_summarize_job,
        )
        self.get_text = async_to_streamed_response_wrapper(
            objects.get_text,
        )
