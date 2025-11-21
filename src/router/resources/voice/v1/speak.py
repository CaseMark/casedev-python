# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.voice.v1 import speak_create_params, speak_stream_params

__all__ = ["SpeakResource", "AsyncSpeakResource"]


class SpeakResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpeakResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/router-python#accessing-raw-response-data-eg-headers
        """
        return SpeakResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeakResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/router-python#with_streaming_response
        """
        return SpeakResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        POST /voice/v1/speak

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/voice/v1/speak",
            body=maybe_transform(body, speak_create_params.SpeakCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def stream(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        POST /voice/v1/speak/stream

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/voice/v1/speak/stream",
            body=maybe_transform(body, speak_stream_params.SpeakStreamParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncSpeakResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpeakResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/router-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpeakResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeakResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/router-python#with_streaming_response
        """
        return AsyncSpeakResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        POST /voice/v1/speak

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/voice/v1/speak",
            body=await async_maybe_transform(body, speak_create_params.SpeakCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def stream(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        POST /voice/v1/speak/stream

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/voice/v1/speak/stream",
            body=await async_maybe_transform(body, speak_stream_params.SpeakStreamParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SpeakResourceWithRawResponse:
    def __init__(self, speak: SpeakResource) -> None:
        self._speak = speak

        self.create = to_raw_response_wrapper(
            speak.create,
        )
        self.stream = to_raw_response_wrapper(
            speak.stream,
        )


class AsyncSpeakResourceWithRawResponse:
    def __init__(self, speak: AsyncSpeakResource) -> None:
        self._speak = speak

        self.create = async_to_raw_response_wrapper(
            speak.create,
        )
        self.stream = async_to_raw_response_wrapper(
            speak.stream,
        )


class SpeakResourceWithStreamingResponse:
    def __init__(self, speak: SpeakResource) -> None:
        self._speak = speak

        self.create = to_streamed_response_wrapper(
            speak.create,
        )
        self.stream = to_streamed_response_wrapper(
            speak.stream,
        )


class AsyncSpeakResourceWithStreamingResponse:
    def __init__(self, speak: AsyncSpeakResource) -> None:
        self._speak = speak

        self.create = async_to_streamed_response_wrapper(
            speak.create,
        )
        self.stream = async_to_streamed_response_wrapper(
            speak.stream,
        )
