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

__all__ = ["ConnectorsResource", "AsyncConnectorsResource"]


class ConnectorsResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        """Import and export between provider folders (Google Drive) and vaults"""
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return ConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return ConnectorsResourceWithStreamingResponse(self)


class AsyncConnectorsResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        """Import and export between provider folders (Google Drive) and vaults"""
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncConnectorsResourceWithStreamingResponse(self)


class ConnectorsResourceWithRawResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        """Import and export between provider folders (Google Drive) and vaults"""
        return V1ResourceWithRawResponse(self._connectors.v1)


class AsyncConnectorsResourceWithRawResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        """Import and export between provider folders (Google Drive) and vaults"""
        return AsyncV1ResourceWithRawResponse(self._connectors.v1)


class ConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        """Import and export between provider folders (Google Drive) and vaults"""
        return V1ResourceWithStreamingResponse(self._connectors.v1)


class AsyncConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        """Import and export between provider folders (Google Drive) and vaults"""
        return AsyncV1ResourceWithStreamingResponse(self._connectors.v1)
