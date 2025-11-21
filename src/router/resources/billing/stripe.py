# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.billing import stripe_handle_webhook_params

__all__ = ["StripeResource", "AsyncStripeResource"]


class StripeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StripeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/router-python#accessing-raw-response-data-eg-headers
        """
        return StripeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StripeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/router-python#with_streaming_response
        """
        return StripeResourceWithStreamingResponse(self)

    def handle_webhook(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        POST /billing/stripe/webhook

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/billing/stripe/webhook",
            body=maybe_transform(body, stripe_handle_webhook_params.StripeHandleWebhookParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncStripeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStripeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/router-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStripeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStripeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/router-python#with_streaming_response
        """
        return AsyncStripeResourceWithStreamingResponse(self)

    async def handle_webhook(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        POST /billing/stripe/webhook

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/billing/stripe/webhook",
            body=await async_maybe_transform(body, stripe_handle_webhook_params.StripeHandleWebhookParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class StripeResourceWithRawResponse:
    def __init__(self, stripe: StripeResource) -> None:
        self._stripe = stripe

        self.handle_webhook = to_raw_response_wrapper(
            stripe.handle_webhook,
        )


class AsyncStripeResourceWithRawResponse:
    def __init__(self, stripe: AsyncStripeResource) -> None:
        self._stripe = stripe

        self.handle_webhook = async_to_raw_response_wrapper(
            stripe.handle_webhook,
        )


class StripeResourceWithStreamingResponse:
    def __init__(self, stripe: StripeResource) -> None:
        self._stripe = stripe

        self.handle_webhook = to_streamed_response_wrapper(
            stripe.handle_webhook,
        )


class AsyncStripeResourceWithStreamingResponse:
    def __init__(self, stripe: AsyncStripeResource) -> None:
        self._stripe = stripe

        self.handle_webhook = async_to_streamed_response_wrapper(
            stripe.handle_webhook,
        )
