# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .inboxes import (
    InboxesResource,
    AsyncInboxesResource,
    InboxesResourceWithRawResponse,
    AsyncInboxesResourceWithRawResponse,
    InboxesResourceWithStreamingResponse,
    AsyncInboxesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def inboxes(self) -> InboxesResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return InboxesResource(self._client)

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
    def inboxes(self) -> AsyncInboxesResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncInboxesResource(self._client)

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
    def inboxes(self) -> InboxesResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return InboxesResourceWithRawResponse(self._v1.inboxes)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def inboxes(self) -> AsyncInboxesResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncInboxesResourceWithRawResponse(self._v1.inboxes)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def inboxes(self) -> InboxesResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return InboxesResourceWithStreamingResponse(self._v1.inboxes)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def inboxes(self) -> AsyncInboxesResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncInboxesResourceWithStreamingResponse(self._v1.inboxes)
