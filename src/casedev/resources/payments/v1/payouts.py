# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...._base_client import make_request_options
from ....types.payments.v1 import payout_list_params, payout_create_params

__all__ = ["PayoutsResource", "AsyncPayoutsResource"]


class PayoutsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PayoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return PayoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return PayoutsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        destination_type: Literal["bank_account", "card"],
        from_account_id: str,
        currency: str | Omit = omit,
        memo: str | Omit = omit,
        metadata: object | Omit = omit,
        party_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a payout to send money to an external bank account

        Args:
          amount: Amount in cents

          from_account_id: Source account

          party_id: Recipient party (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/payments/v1/payouts",
            body=maybe_transform(
                {
                    "amount": amount,
                    "destination_type": destination_type,
                    "from_account_id": from_account_id,
                    "currency": currency,
                    "memo": memo,
                    "metadata": metadata,
                    "party_id": party_id,
                },
                payout_create_params.PayoutCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get payout details by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/payments/v1/payouts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        from_account_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        party_id: str | Omit = omit,
        status: Literal["pending", "processing", "completed", "failed", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List payouts with optional filters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/payments/v1/payouts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_account_id": from_account_id,
                        "limit": limit,
                        "offset": offset,
                        "party_id": party_id,
                        "status": status,
                    },
                    payout_list_params.PayoutListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Cancel a pending payout before it is processed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/payments/v1/payouts/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPayoutsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPayoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPayoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncPayoutsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        destination_type: Literal["bank_account", "card"],
        from_account_id: str,
        currency: str | Omit = omit,
        memo: str | Omit = omit,
        metadata: object | Omit = omit,
        party_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a payout to send money to an external bank account

        Args:
          amount: Amount in cents

          from_account_id: Source account

          party_id: Recipient party (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/payments/v1/payouts",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "destination_type": destination_type,
                    "from_account_id": from_account_id,
                    "currency": currency,
                    "memo": memo,
                    "metadata": metadata,
                    "party_id": party_id,
                },
                payout_create_params.PayoutCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get payout details by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/payments/v1/payouts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        from_account_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        party_id: str | Omit = omit,
        status: Literal["pending", "processing", "completed", "failed", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List payouts with optional filters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/payments/v1/payouts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_account_id": from_account_id,
                        "limit": limit,
                        "offset": offset,
                        "party_id": party_id,
                        "status": status,
                    },
                    payout_list_params.PayoutListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Cancel a pending payout before it is processed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/payments/v1/payouts/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PayoutsResourceWithRawResponse:
    def __init__(self, payouts: PayoutsResource) -> None:
        self._payouts = payouts

        self.create = to_raw_response_wrapper(
            payouts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            payouts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            payouts.list,
        )
        self.cancel = to_raw_response_wrapper(
            payouts.cancel,
        )


class AsyncPayoutsResourceWithRawResponse:
    def __init__(self, payouts: AsyncPayoutsResource) -> None:
        self._payouts = payouts

        self.create = async_to_raw_response_wrapper(
            payouts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            payouts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            payouts.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            payouts.cancel,
        )


class PayoutsResourceWithStreamingResponse:
    def __init__(self, payouts: PayoutsResource) -> None:
        self._payouts = payouts

        self.create = to_streamed_response_wrapper(
            payouts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payouts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payouts.list,
        )
        self.cancel = to_streamed_response_wrapper(
            payouts.cancel,
        )


class AsyncPayoutsResourceWithStreamingResponse:
    def __init__(self, payouts: AsyncPayoutsResource) -> None:
        self._payouts = payouts

        self.create = async_to_streamed_response_wrapper(
            payouts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payouts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payouts.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            payouts.cancel,
        )
