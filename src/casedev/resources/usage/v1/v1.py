# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)
from ....types.usage import v1_retrieve_params
from ...._base_client import make_request_options

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    """Usage reporting and webhook subscriptions"""

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        """Usage reporting and webhook subscriptions"""
        return SubscriptionsResource(self._client)

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

    def retrieve(
        self,
        *,
        granularity: Literal["summary", "daily"] | Omit = omit,
        period_end: Union[str, datetime] | Omit = omit,
        period_start: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns customer-facing usage metrics and costs for the requested period.
        Supports summary totals and daily buckets for timestamped usage sources. Vault
        storage is intentionally omitted from totals because it is not yet periodized
        for arbitrary windows.

        Args:
          granularity: Whether to return period totals only or include daily buckets.

          period_end: Period end date. Defaults to now.

          period_start: Period start date. Defaults to the start of the current calendar month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/usage/v1",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "granularity": granularity,
                        "period_end": period_end,
                        "period_start": period_start,
                    },
                    v1_retrieve_params.V1RetrieveParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncV1Resource(AsyncAPIResource):
    """Usage reporting and webhook subscriptions"""

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        """Usage reporting and webhook subscriptions"""
        return AsyncSubscriptionsResource(self._client)

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

    async def retrieve(
        self,
        *,
        granularity: Literal["summary", "daily"] | Omit = omit,
        period_end: Union[str, datetime] | Omit = omit,
        period_start: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns customer-facing usage metrics and costs for the requested period.
        Supports summary totals and daily buckets for timestamped usage sources. Vault
        storage is intentionally omitted from totals because it is not yet periodized
        for arbitrary windows.

        Args:
          granularity: Whether to return period totals only or include daily buckets.

          period_end: Period end date. Defaults to now.

          period_start: Period start date. Defaults to the start of the current calendar month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/usage/v1",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "granularity": granularity,
                        "period_end": period_end,
                        "period_start": period_start,
                    },
                    v1_retrieve_params.V1RetrieveParams,
                ),
            ),
            cast_to=NoneType,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.retrieve = to_raw_response_wrapper(
            v1.retrieve,
        )

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        """Usage reporting and webhook subscriptions"""
        return SubscriptionsResourceWithRawResponse(self._v1.subscriptions)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.retrieve = async_to_raw_response_wrapper(
            v1.retrieve,
        )

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """Usage reporting and webhook subscriptions"""
        return AsyncSubscriptionsResourceWithRawResponse(self._v1.subscriptions)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.retrieve = to_streamed_response_wrapper(
            v1.retrieve,
        )

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        """Usage reporting and webhook subscriptions"""
        return SubscriptionsResourceWithStreamingResponse(self._v1.subscriptions)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.retrieve = async_to_streamed_response_wrapper(
            v1.retrieve,
        )

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """Usage reporting and webhook subscriptions"""
        return AsyncSubscriptionsResourceWithStreamingResponse(self._v1.subscriptions)
