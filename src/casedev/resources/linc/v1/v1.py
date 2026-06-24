# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def sessions(self) -> SessionsResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return SessionsResource(self._client)

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
    def sessions(self) -> AsyncSessionsResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncSessionsResource(self._client)

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
    def sessions(self) -> SessionsResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return SessionsResourceWithRawResponse(self._v1.sessions)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncSessionsResourceWithRawResponse(self._v1.sessions)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return SessionsResourceWithStreamingResponse(self._v1.sessions)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncSessionsResourceWithStreamingResponse(self._v1.sessions)
