# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.matters.v1.purge_retrieve_response import PurgeRetrieveResponse

__all__ = ["PurgesResource", "AsyncPurgesResource"]


class PurgesResource(SyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> PurgesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return PurgesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PurgesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return PurgesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        purge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PurgeRetrieveResponse:
        """Returns a Matter purge receipt for manual diagnostics.

        Integrations should
        subscribe to Matter purge webhooks rather than polling this route.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not purge_id:
            raise ValueError(f"Expected a non-empty value for `purge_id` but received {purge_id!r}")
        return self._get(
            path_template("/matters/v1/purges/{purge_id}", purge_id=purge_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurgeRetrieveResponse,
        )


class AsyncPurgesResource(AsyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> AsyncPurgesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPurgesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPurgesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncPurgesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        purge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PurgeRetrieveResponse:
        """Returns a Matter purge receipt for manual diagnostics.

        Integrations should
        subscribe to Matter purge webhooks rather than polling this route.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not purge_id:
            raise ValueError(f"Expected a non-empty value for `purge_id` but received {purge_id!r}")
        return await self._get(
            path_template("/matters/v1/purges/{purge_id}", purge_id=purge_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurgeRetrieveResponse,
        )


class PurgesResourceWithRawResponse:
    def __init__(self, purges: PurgesResource) -> None:
        self._purges = purges

        self.retrieve = to_raw_response_wrapper(
            purges.retrieve,
        )


class AsyncPurgesResourceWithRawResponse:
    def __init__(self, purges: AsyncPurgesResource) -> None:
        self._purges = purges

        self.retrieve = async_to_raw_response_wrapper(
            purges.retrieve,
        )


class PurgesResourceWithStreamingResponse:
    def __init__(self, purges: PurgesResource) -> None:
        self._purges = purges

        self.retrieve = to_streamed_response_wrapper(
            purges.retrieve,
        )


class AsyncPurgesResourceWithStreamingResponse:
    def __init__(self, purges: AsyncPurgesResource) -> None:
        self._purges = purges

        self.retrieve = async_to_streamed_response_wrapper(
            purges.retrieve,
        )
