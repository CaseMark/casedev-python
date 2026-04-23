# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["EventTypesResource", "AsyncEventTypesResource"]


class EventTypesResource(SyncAPIResource):
    """Webhook endpoint management"""

    @cached_property
    def with_raw_response(self) -> EventTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return EventTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return EventTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns the catalog of event types that can be subscribed to via webhook
        endpoints. Each entry lists the required service scope the API key must carry to
        subscribe, plus the stability level.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/webhooks/v1/event_types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEventTypesResource(AsyncAPIResource):
    """Webhook endpoint management"""

    @cached_property
    def with_raw_response(self) -> AsyncEventTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncEventTypesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns the catalog of event types that can be subscribed to via webhook
        endpoints. Each entry lists the required service scope the API key must carry to
        subscribe, plus the stability level.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/webhooks/v1/event_types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EventTypesResourceWithRawResponse:
    def __init__(self, event_types: EventTypesResource) -> None:
        self._event_types = event_types

        self.list = to_raw_response_wrapper(
            event_types.list,
        )


class AsyncEventTypesResourceWithRawResponse:
    def __init__(self, event_types: AsyncEventTypesResource) -> None:
        self._event_types = event_types

        self.list = async_to_raw_response_wrapper(
            event_types.list,
        )


class EventTypesResourceWithStreamingResponse:
    def __init__(self, event_types: EventTypesResource) -> None:
        self._event_types = event_types

        self.list = to_streamed_response_wrapper(
            event_types.list,
        )


class AsyncEventTypesResourceWithStreamingResponse:
    def __init__(self, event_types: AsyncEventTypesResource) -> None:
        self._event_types = event_types

        self.list = async_to_streamed_response_wrapper(
            event_types.list,
        )
