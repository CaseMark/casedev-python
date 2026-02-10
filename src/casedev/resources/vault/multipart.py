# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.vault import multipart_abort_params, multipart_get_part_urls_params
from ..._base_client import make_request_options
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
        Abort a multipart upload and discard uploaded parts (live).

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
        Generate presigned URLs for individual multipart upload parts (live).

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
        Abort a multipart upload and discard uploaded parts (live).

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
        Generate presigned URLs for individual multipart upload parts (live).

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


class MultipartResourceWithRawResponse:
    def __init__(self, multipart: MultipartResource) -> None:
        self._multipart = multipart

        self.abort = to_raw_response_wrapper(
            multipart.abort,
        )
        self.get_part_urls = to_raw_response_wrapper(
            multipart.get_part_urls,
        )


class AsyncMultipartResourceWithRawResponse:
    def __init__(self, multipart: AsyncMultipartResource) -> None:
        self._multipart = multipart

        self.abort = async_to_raw_response_wrapper(
            multipart.abort,
        )
        self.get_part_urls = async_to_raw_response_wrapper(
            multipart.get_part_urls,
        )


class MultipartResourceWithStreamingResponse:
    def __init__(self, multipart: MultipartResource) -> None:
        self._multipart = multipart

        self.abort = to_streamed_response_wrapper(
            multipart.abort,
        )
        self.get_part_urls = to_streamed_response_wrapper(
            multipart.get_part_urls,
        )


class AsyncMultipartResourceWithStreamingResponse:
    def __init__(self, multipart: AsyncMultipartResource) -> None:
        self._multipart = multipart

        self.abort = async_to_streamed_response_wrapper(
            multipart.abort,
        )
        self.get_part_urls = async_to_streamed_response_wrapper(
            multipart.get_part_urls,
        )
