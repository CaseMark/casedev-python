# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v1.v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MattersResource", "AsyncMattersResource"]


class MattersResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        """Matter-native legal workspaces and orchestration primitives"""
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> MattersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return MattersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MattersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return MattersResourceWithStreamingResponse(self)


class AsyncMattersResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMattersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMattersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMattersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncMattersResourceWithStreamingResponse(self)


class MattersResourceWithRawResponse:
    def __init__(self, matters: MattersResource) -> None:
        self._matters = matters

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return V1ResourceWithRawResponse(self._matters.v1)


class AsyncMattersResourceWithRawResponse:
    def __init__(self, matters: AsyncMattersResource) -> None:
        self._matters = matters

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncV1ResourceWithRawResponse(self._matters.v1)


class MattersResourceWithStreamingResponse:
    def __init__(self, matters: MattersResource) -> None:
        self._matters = matters

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return V1ResourceWithStreamingResponse(self._matters.v1)


class AsyncMattersResourceWithStreamingResponse:
    def __init__(self, matters: AsyncMattersResource) -> None:
        self._matters = matters

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncV1ResourceWithStreamingResponse(self._matters.v1)
