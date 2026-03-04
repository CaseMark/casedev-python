# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MemoryResource", "AsyncMemoryResource"]


class MemoryResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        """
        Persistent memory for AI agents with semantic search and 12 generic indexed tag fields
        """
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> MemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return MemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return MemoryResourceWithStreamingResponse(self)


class AsyncMemoryResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        """
        Persistent memory for AI agents with semantic search and 12 generic indexed tag fields
        """
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncMemoryResourceWithStreamingResponse(self)


class MemoryResourceWithRawResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        """
        Persistent memory for AI agents with semantic search and 12 generic indexed tag fields
        """
        return V1ResourceWithRawResponse(self._memory.v1)


class AsyncMemoryResourceWithRawResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        """
        Persistent memory for AI agents with semantic search and 12 generic indexed tag fields
        """
        return AsyncV1ResourceWithRawResponse(self._memory.v1)


class MemoryResourceWithStreamingResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        """
        Persistent memory for AI agents with semantic search and 12 generic indexed tag fields
        """
        return V1ResourceWithStreamingResponse(self._memory.v1)


class AsyncMemoryResourceWithStreamingResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        Persistent memory for AI agents with semantic search and 12 generic indexed tag fields
        """
        return AsyncV1ResourceWithStreamingResponse(self._memory.v1)
