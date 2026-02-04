# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
    multipart_init_params,
    multipart_abort_params,
    multipart_complete_params,
    multipart_get_part_urls_params,
)
from ..._base_client import make_request_options
from ...types.vault.multipart_init_response import MultipartInitResponse
from ...types.vault.multipart_get_part_urls_response import MultipartGetPartURLsResponse

__all__ = ["MultipartResource", "AsyncMultipartResource"]


class MultipartResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MultipartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return MultipartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MultipartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return MultipartResourceWithStreamingResponse(self)

    def abort(
        self,
        id: str,
        *,
        object_id: str,
        upload_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Abort a multipart upload and discard uploaded parts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/vault/{id}/multipart/abort",
            body=maybe_transform(
                {
                    "object_id": object_id,
                    "upload_id": upload_id,
                },
                multipart_abort_params.MultipartAbortParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def complete(
        self,
        id: str,
        *,
        object_id: str,
        parts: Iterable[multipart_complete_params.Part],
        size_bytes: int,
        upload_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Complete a multipart upload by providing the list of part numbers and ETags.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/vault/{id}/multipart/complete",
            body=maybe_transform(
                {
                    "object_id": object_id,
                    "parts": parts,
                    "size_bytes": size_bytes,
                    "upload_id": upload_id,
                },
                multipart_complete_params.MultipartCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_part_urls(
        self,
        id: str,
        *,
        object_id: str,
        parts: Iterable[multipart_get_part_urls_params.Part],
        upload_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MultipartGetPartURLsResponse:
        """
        Generate presigned URLs for individual multipart upload parts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/vault/{id}/multipart/part-urls",
            body=maybe_transform(
                {
                    "object_id": object_id,
                    "parts": parts,
                    "upload_id": upload_id,
                },
                multipart_get_part_urls_params.MultipartGetPartURLsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipartGetPartURLsResponse,
        )

    def init(
        self,
        id: str,
        *,
        content_type: str,
        filename: str,
        size_bytes: int,
        auto_index: bool | Omit = omit,
        metadata: object | Omit = omit,
        part_size_bytes: int | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MultipartInitResponse:
        """Initiate a multipart upload for large files (>5GB).

        Returns an uploadId and
        object metadata. Use part URLs endpoint to upload parts and complete endpoint to
        finalize.

        Args:
          content_type: MIME type of the file

          filename: Name of the file to upload

          size_bytes: File size in bytes (required, max 8GB).

          auto_index: Whether to automatically process and index the file for search

          metadata: Additional metadata to associate with the file

          part_size_bytes: Multipart part size in bytes (min 5MB). Defaults to 64MB.

          path: Optional folder path for hierarchy preservation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/vault/{id}/multipart/init",
            body=maybe_transform(
                {
                    "content_type": content_type,
                    "filename": filename,
                    "size_bytes": size_bytes,
                    "auto_index": auto_index,
                    "metadata": metadata,
                    "part_size_bytes": part_size_bytes,
                    "path": path,
                },
                multipart_init_params.MultipartInitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipartInitResponse,
        )


class AsyncMultipartResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMultipartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMultipartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMultipartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncMultipartResourceWithStreamingResponse(self)

    async def abort(
        self,
        id: str,
        *,
        object_id: str,
        upload_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Abort a multipart upload and discard uploaded parts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/vault/{id}/multipart/abort",
            body=await async_maybe_transform(
                {
                    "object_id": object_id,
                    "upload_id": upload_id,
                },
                multipart_abort_params.MultipartAbortParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def complete(
        self,
        id: str,
        *,
        object_id: str,
        parts: Iterable[multipart_complete_params.Part],
        size_bytes: int,
        upload_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Complete a multipart upload by providing the list of part numbers and ETags.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/vault/{id}/multipart/complete",
            body=await async_maybe_transform(
                {
                    "object_id": object_id,
                    "parts": parts,
                    "size_bytes": size_bytes,
                    "upload_id": upload_id,
                },
                multipart_complete_params.MultipartCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_part_urls(
        self,
        id: str,
        *,
        object_id: str,
        parts: Iterable[multipart_get_part_urls_params.Part],
        upload_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MultipartGetPartURLsResponse:
        """
        Generate presigned URLs for individual multipart upload parts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/vault/{id}/multipart/part-urls",
            body=await async_maybe_transform(
                {
                    "object_id": object_id,
                    "parts": parts,
                    "upload_id": upload_id,
                },
                multipart_get_part_urls_params.MultipartGetPartURLsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipartGetPartURLsResponse,
        )

    async def init(
        self,
        id: str,
        *,
        content_type: str,
        filename: str,
        size_bytes: int,
        auto_index: bool | Omit = omit,
        metadata: object | Omit = omit,
        part_size_bytes: int | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MultipartInitResponse:
        """Initiate a multipart upload for large files (>5GB).

        Returns an uploadId and
        object metadata. Use part URLs endpoint to upload parts and complete endpoint to
        finalize.

        Args:
          content_type: MIME type of the file

          filename: Name of the file to upload

          size_bytes: File size in bytes (required, max 8GB).

          auto_index: Whether to automatically process and index the file for search

          metadata: Additional metadata to associate with the file

          part_size_bytes: Multipart part size in bytes (min 5MB). Defaults to 64MB.

          path: Optional folder path for hierarchy preservation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/vault/{id}/multipart/init",
            body=await async_maybe_transform(
                {
                    "content_type": content_type,
                    "filename": filename,
                    "size_bytes": size_bytes,
                    "auto_index": auto_index,
                    "metadata": metadata,
                    "part_size_bytes": part_size_bytes,
                    "path": path,
                },
                multipart_init_params.MultipartInitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MultipartInitResponse,
        )


class MultipartResourceWithRawResponse:
    def __init__(self, multipart: MultipartResource) -> None:
        self._multipart = multipart

        self.abort = to_raw_response_wrapper(
            multipart.abort,
        )
        self.complete = to_raw_response_wrapper(
            multipart.complete,
        )
        self.get_part_urls = to_raw_response_wrapper(
            multipart.get_part_urls,
        )
        self.init = to_raw_response_wrapper(
            multipart.init,
        )


class AsyncMultipartResourceWithRawResponse:
    def __init__(self, multipart: AsyncMultipartResource) -> None:
        self._multipart = multipart

        self.abort = async_to_raw_response_wrapper(
            multipart.abort,
        )
        self.complete = async_to_raw_response_wrapper(
            multipart.complete,
        )
        self.get_part_urls = async_to_raw_response_wrapper(
            multipart.get_part_urls,
        )
        self.init = async_to_raw_response_wrapper(
            multipart.init,
        )


class MultipartResourceWithStreamingResponse:
    def __init__(self, multipart: MultipartResource) -> None:
        self._multipart = multipart

        self.abort = to_streamed_response_wrapper(
            multipart.abort,
        )
        self.complete = to_streamed_response_wrapper(
            multipart.complete,
        )
        self.get_part_urls = to_streamed_response_wrapper(
            multipart.get_part_urls,
        )
        self.init = to_streamed_response_wrapper(
            multipart.init,
        )


class AsyncMultipartResourceWithStreamingResponse:
    def __init__(self, multipart: AsyncMultipartResource) -> None:
        self._multipart = multipart

        self.abort = async_to_streamed_response_wrapper(
            multipart.abort,
        )
        self.complete = async_to_streamed_response_wrapper(
            multipart.complete,
        )
        self.get_part_urls = async_to_streamed_response_wrapper(
            multipart.get_part_urls,
        )
        self.init = async_to_streamed_response_wrapper(
            multipart.init,
        )
