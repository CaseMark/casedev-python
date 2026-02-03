# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.payments.v1 import charge_list_params, charge_create_params, charge_refund_params

__all__ = ["ChargesResource", "AsyncChargesResource"]


class ChargesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChargesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return ChargesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChargesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return ChargesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        destination_account_id: str,
        party_id: str,
        currency: str | Omit = omit,
        description: str | Omit = omit,
        metadata: object | Omit = omit,
        payment_methods: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a charge (payment request) to collect money from a party

        Args:
          amount: Amount in cents

          destination_account_id: Account to receive funds

          party_id: Party to charge

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/payments/v1/charges",
            body=maybe_transform(
                {
                    "amount": amount,
                    "destination_account_id": destination_account_id,
                    "party_id": party_id,
                    "currency": currency,
                    "description": description,
                    "metadata": metadata,
                    "payment_methods": payment_methods,
                },
                charge_create_params.ChargeCreateParams,
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
        Get charge details by ID

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
            f"/payments/v1/charges/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        destination_account_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        party_id: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List charges with optional filters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/payments/v1/charges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "destination_account_id": destination_account_id,
                        "limit": limit,
                        "offset": offset,
                        "party_id": party_id,
                        "status": status,
                    },
                    charge_list_params.ChargeListParams,
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
        Cancel a pending charge before payment is collected

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
            f"/payments/v1/charges/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def refund(
        self,
        id: str,
        *,
        amount: int | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Refund a succeeded charge (full or partial)

        Args:
          amount: Amount to refund in cents. If not provided, full refund.

          reason: Reason for refund

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/payments/v1/charges/{id}/refund",
            body=maybe_transform(
                {
                    "amount": amount,
                    "reason": reason,
                },
                charge_refund_params.ChargeRefundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncChargesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChargesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChargesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChargesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncChargesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        destination_account_id: str,
        party_id: str,
        currency: str | Omit = omit,
        description: str | Omit = omit,
        metadata: object | Omit = omit,
        payment_methods: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a charge (payment request) to collect money from a party

        Args:
          amount: Amount in cents

          destination_account_id: Account to receive funds

          party_id: Party to charge

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/payments/v1/charges",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "destination_account_id": destination_account_id,
                    "party_id": party_id,
                    "currency": currency,
                    "description": description,
                    "metadata": metadata,
                    "payment_methods": payment_methods,
                },
                charge_create_params.ChargeCreateParams,
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
        Get charge details by ID

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
            f"/payments/v1/charges/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        destination_account_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        party_id: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List charges with optional filters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/payments/v1/charges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "destination_account_id": destination_account_id,
                        "limit": limit,
                        "offset": offset,
                        "party_id": party_id,
                        "status": status,
                    },
                    charge_list_params.ChargeListParams,
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
        Cancel a pending charge before payment is collected

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
            f"/payments/v1/charges/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def refund(
        self,
        id: str,
        *,
        amount: int | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Refund a succeeded charge (full or partial)

        Args:
          amount: Amount to refund in cents. If not provided, full refund.

          reason: Reason for refund

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/payments/v1/charges/{id}/refund",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "reason": reason,
                },
                charge_refund_params.ChargeRefundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ChargesResourceWithRawResponse:
    def __init__(self, charges: ChargesResource) -> None:
        self._charges = charges

        self.create = to_raw_response_wrapper(
            charges.create,
        )
        self.retrieve = to_raw_response_wrapper(
            charges.retrieve,
        )
        self.list = to_raw_response_wrapper(
            charges.list,
        )
        self.cancel = to_raw_response_wrapper(
            charges.cancel,
        )
        self.refund = to_raw_response_wrapper(
            charges.refund,
        )


class AsyncChargesResourceWithRawResponse:
    def __init__(self, charges: AsyncChargesResource) -> None:
        self._charges = charges

        self.create = async_to_raw_response_wrapper(
            charges.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            charges.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            charges.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            charges.cancel,
        )
        self.refund = async_to_raw_response_wrapper(
            charges.refund,
        )


class ChargesResourceWithStreamingResponse:
    def __init__(self, charges: ChargesResource) -> None:
        self._charges = charges

        self.create = to_streamed_response_wrapper(
            charges.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            charges.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            charges.list,
        )
        self.cancel = to_streamed_response_wrapper(
            charges.cancel,
        )
        self.refund = to_streamed_response_wrapper(
            charges.refund,
        )


class AsyncChargesResourceWithStreamingResponse:
    def __init__(self, charges: AsyncChargesResource) -> None:
        self._charges = charges

        self.create = async_to_streamed_response_wrapper(
            charges.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            charges.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            charges.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            charges.cancel,
        )
        self.refund = async_to_streamed_response_wrapper(
            charges.refund,
        )
