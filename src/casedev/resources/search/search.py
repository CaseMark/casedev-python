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

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        """Web search, AI answers, and deep research"""
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        """Web search, AI answers, and deep research"""
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        """Web search, AI answers, and deep research"""
        return V1ResourceWithRawResponse(self._search.v1)


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        """Web search, AI answers, and deep research"""
        return AsyncV1ResourceWithRawResponse(self._search.v1)


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        """Web search, AI answers, and deep research"""
        return V1ResourceWithStreamingResponse(self._search.v1)


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        """Web search, AI answers, and deep research"""
        return AsyncV1ResourceWithStreamingResponse(self._search.v1)
