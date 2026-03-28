# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return SubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return SubscriptionsResourceWithRawResponse(self._events.subscriptions)


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncSubscriptionsResourceWithRawResponse(self._events.subscriptions)


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return SubscriptionsResourceWithStreamingResponse(self._events.subscriptions)


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncSubscriptionsResourceWithStreamingResponse(self._events.subscriptions)
