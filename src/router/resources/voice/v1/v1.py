# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .speak import (
    SpeakResource,
    AsyncSpeakResource,
    SpeakResourceWithRawResponse,
    AsyncSpeakResourceWithRawResponse,
    SpeakResourceWithStreamingResponse,
    AsyncSpeakResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def speak(self) -> SpeakResource:
        return SpeakResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/router-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/router-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def list_voices(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """GET /voice/v1/voices"""
        return self._get(
            "/voice/v1/voices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def speak(self) -> AsyncSpeakResource:
        return AsyncSpeakResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/router-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/router-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def list_voices(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """GET /voice/v1/voices"""
        return await self._get(
            "/voice/v1/voices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.list_voices = to_raw_response_wrapper(
            v1.list_voices,
        )

    @cached_property
    def speak(self) -> SpeakResourceWithRawResponse:
        return SpeakResourceWithRawResponse(self._v1.speak)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.list_voices = async_to_raw_response_wrapper(
            v1.list_voices,
        )

    @cached_property
    def speak(self) -> AsyncSpeakResourceWithRawResponse:
        return AsyncSpeakResourceWithRawResponse(self._v1.speak)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.list_voices = to_streamed_response_wrapper(
            v1.list_voices,
        )

    @cached_property
    def speak(self) -> SpeakResourceWithStreamingResponse:
        return SpeakResourceWithStreamingResponse(self._v1.speak)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.list_voices = async_to_streamed_response_wrapper(
            v1.list_voices,
        )

    @cached_property
    def speak(self) -> AsyncSpeakResourceWithStreamingResponse:
        return AsyncSpeakResourceWithStreamingResponse(self._v1.speak)
