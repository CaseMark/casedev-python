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

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        """Usage reporting and webhook subscriptions"""
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return UsageResourceWithStreamingResponse(self)


class AsyncUsageResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        """Usage reporting and webhook subscriptions"""
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncUsageResourceWithStreamingResponse(self)


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        """Usage reporting and webhook subscriptions"""
        return V1ResourceWithRawResponse(self._usage.v1)


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        """Usage reporting and webhook subscriptions"""
        return AsyncV1ResourceWithRawResponse(self._usage.v1)


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        """Usage reporting and webhook subscriptions"""
        return V1ResourceWithStreamingResponse(self._usage.v1)


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        """Usage reporting and webhook subscriptions"""
        return AsyncV1ResourceWithStreamingResponse(self._usage.v1)
