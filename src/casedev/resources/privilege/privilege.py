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

__all__ = ["PrivilegeResource", "AsyncPrivilegeResource"]


class PrivilegeResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> PrivilegeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return PrivilegeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrivilegeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return PrivilegeResourceWithStreamingResponse(self)


class AsyncPrivilegeResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPrivilegeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrivilegeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrivilegeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncPrivilegeResourceWithStreamingResponse(self)


class PrivilegeResourceWithRawResponse:
    def __init__(self, privilege: PrivilegeResource) -> None:
        self._privilege = privilege

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        return V1ResourceWithRawResponse(self._privilege.v1)


class AsyncPrivilegeResourceWithRawResponse:
    def __init__(self, privilege: AsyncPrivilegeResource) -> None:
        self._privilege = privilege

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        return AsyncV1ResourceWithRawResponse(self._privilege.v1)


class PrivilegeResourceWithStreamingResponse:
    def __init__(self, privilege: PrivilegeResource) -> None:
        self._privilege = privilege

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        return V1ResourceWithStreamingResponse(self._privilege.v1)


class AsyncPrivilegeResourceWithStreamingResponse:
    def __init__(self, privilege: AsyncPrivilegeResource) -> None:
        self._privilege = privilege

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        return AsyncV1ResourceWithStreamingResponse(self._privilege.v1)
