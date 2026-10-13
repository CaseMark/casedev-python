# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ApplicationsResource", "AsyncApplicationsResource"]


class ApplicationsResource(SyncAPIResource):
    @cached_property
    def keys(self) -> KeysResource:
        """Import and export between provider folders and vaults"""
        return KeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> ApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return ApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return ApplicationsResourceWithStreamingResponse(self)


class AsyncApplicationsResource(AsyncAPIResource):
    @cached_property
    def keys(self) -> AsyncKeysResource:
        """Import and export between provider folders and vaults"""
        return AsyncKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncApplicationsResourceWithStreamingResponse(self)


class ApplicationsResourceWithRawResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        """Import and export between provider folders and vaults"""
        return KeysResourceWithRawResponse(self._applications.keys)


class AsyncApplicationsResourceWithRawResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        """Import and export between provider folders and vaults"""
        return AsyncKeysResourceWithRawResponse(self._applications.keys)


class ApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        """Import and export between provider folders and vaults"""
        return KeysResourceWithStreamingResponse(self._applications.keys)


class AsyncApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        """Import and export between provider folders and vaults"""
        return AsyncKeysResourceWithStreamingResponse(self._applications.keys)
