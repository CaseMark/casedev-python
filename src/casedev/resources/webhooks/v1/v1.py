# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .endpoints import (
    EndpointsResource,
    AsyncEndpointsResource,
    EndpointsResourceWithRawResponse,
    AsyncEndpointsResourceWithRawResponse,
    EndpointsResourceWithStreamingResponse,
    AsyncEndpointsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .deliveries import (
    DeliveriesResource,
    AsyncDeliveriesResource,
    DeliveriesResourceWithRawResponse,
    AsyncDeliveriesResourceWithRawResponse,
    DeliveriesResourceWithStreamingResponse,
    AsyncDeliveriesResourceWithStreamingResponse,
)
from .event_types import (
    EventTypesResource,
    AsyncEventTypesResource,
    EventTypesResourceWithRawResponse,
    AsyncEventTypesResourceWithRawResponse,
    EventTypesResourceWithStreamingResponse,
    AsyncEventTypesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def endpoints(self) -> EndpointsResource:
        """Webhook endpoint management"""
        return EndpointsResource(self._client)

    @cached_property
    def deliveries(self) -> DeliveriesResource:
        """Webhook endpoint management"""
        return DeliveriesResource(self._client)

    @cached_property
    def event_types(self) -> EventTypesResource:
        """Webhook endpoint management"""
        return EventTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def endpoints(self) -> AsyncEndpointsResource:
        """Webhook endpoint management"""
        return AsyncEndpointsResource(self._client)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResource:
        """Webhook endpoint management"""
        return AsyncDeliveriesResource(self._client)

    @cached_property
    def event_types(self) -> AsyncEventTypesResource:
        """Webhook endpoint management"""
        return AsyncEventTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def endpoints(self) -> EndpointsResourceWithRawResponse:
        """Webhook endpoint management"""
        return EndpointsResourceWithRawResponse(self._v1.endpoints)

    @cached_property
    def deliveries(self) -> DeliveriesResourceWithRawResponse:
        """Webhook endpoint management"""
        return DeliveriesResourceWithRawResponse(self._v1.deliveries)

    @cached_property
    def event_types(self) -> EventTypesResourceWithRawResponse:
        """Webhook endpoint management"""
        return EventTypesResourceWithRawResponse(self._v1.event_types)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def endpoints(self) -> AsyncEndpointsResourceWithRawResponse:
        """Webhook endpoint management"""
        return AsyncEndpointsResourceWithRawResponse(self._v1.endpoints)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResourceWithRawResponse:
        """Webhook endpoint management"""
        return AsyncDeliveriesResourceWithRawResponse(self._v1.deliveries)

    @cached_property
    def event_types(self) -> AsyncEventTypesResourceWithRawResponse:
        """Webhook endpoint management"""
        return AsyncEventTypesResourceWithRawResponse(self._v1.event_types)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def endpoints(self) -> EndpointsResourceWithStreamingResponse:
        """Webhook endpoint management"""
        return EndpointsResourceWithStreamingResponse(self._v1.endpoints)

    @cached_property
    def deliveries(self) -> DeliveriesResourceWithStreamingResponse:
        """Webhook endpoint management"""
        return DeliveriesResourceWithStreamingResponse(self._v1.deliveries)

    @cached_property
    def event_types(self) -> EventTypesResourceWithStreamingResponse:
        """Webhook endpoint management"""
        return EventTypesResourceWithStreamingResponse(self._v1.event_types)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def endpoints(self) -> AsyncEndpointsResourceWithStreamingResponse:
        """Webhook endpoint management"""
        return AsyncEndpointsResourceWithStreamingResponse(self._v1.endpoints)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        """Webhook endpoint management"""
        return AsyncDeliveriesResourceWithStreamingResponse(self._v1.deliveries)

    @cached_property
    def event_types(self) -> AsyncEventTypesResourceWithStreamingResponse:
        """Webhook endpoint management"""
        return AsyncEventTypesResourceWithStreamingResponse(self._v1.event_types)
