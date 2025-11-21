# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["IndexResource", "AsyncIndexResource"]


class IndexResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndexResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/router-python#accessing-raw-response-data-eg-headers
        """
        return IndexResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndexResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/router-python#with_streaming_response
        """
        return IndexResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """GET /index"""
        return self._get(
            "/index",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncIndexResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndexResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/router-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndexResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndexResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/router-python#with_streaming_response
        """
        return AsyncIndexResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """GET /index"""
        return await self._get(
            "/index",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class IndexResourceWithRawResponse:
    def __init__(self, index: IndexResource) -> None:
        self._index = index

        self.retrieve = to_raw_response_wrapper(
            index.retrieve,
        )


class AsyncIndexResourceWithRawResponse:
    def __init__(self, index: AsyncIndexResource) -> None:
        self._index = index

        self.retrieve = async_to_raw_response_wrapper(
            index.retrieve,
        )


class IndexResourceWithStreamingResponse:
    def __init__(self, index: IndexResource) -> None:
        self._index = index

        self.retrieve = to_streamed_response_wrapper(
            index.retrieve,
        )


class AsyncIndexResourceWithStreamingResponse:
    def __init__(self, index: AsyncIndexResource) -> None:
        self._index = index

        self.retrieve = async_to_streamed_response_wrapper(
            index.retrieve,
        )
