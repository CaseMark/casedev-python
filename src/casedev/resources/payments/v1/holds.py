# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

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
from ....types.payments.v1 import hold_list_params, hold_create_params, hold_approve_params

__all__ = ["HoldsResource", "AsyncHoldsResource"]


class HoldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HoldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return HoldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HoldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return HoldsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: int,
        currency: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        memo: str | Omit = omit,
        metadata: object | Omit = omit,
        on_release_action: str | Omit = omit,
        on_release_config: object | Omit = omit,
        release_conditions: Iterable[hold_create_params.ReleaseCondition] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a hold on funds in an account with release conditions

        Args:
          account_id: Account to hold funds in

          amount: Amount in cents to hold

          on_release_action: Action to take when released

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/payments/v1/holds",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "currency": currency,
                    "expires_at": expires_at,
                    "memo": memo,
                    "metadata": metadata,
                    "on_release_action": on_release_action,
                    "on_release_config": on_release_config,
                    "release_conditions": release_conditions,
                },
                hold_create_params.HoldCreateParams,
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
        Get hold details by ID

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
            f"/payments/v1/holds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List holds with optional filters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/payments/v1/holds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    hold_list_params.HoldListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def approve(
        self,
        id: str,
        *,
        approver_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Record an approval for a hold release condition

        Args:
          approver_id: ID of the approver (party or user)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/payments/v1/holds/{id}/approve",
            body=maybe_transform({"approver_id": approver_id}, hold_approve_params.HoldApproveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        Cancel an active hold

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
            f"/payments/v1/holds/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def release(
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
        Manually release a hold

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
            f"/payments/v1/holds/{id}/release",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncHoldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHoldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHoldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHoldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncHoldsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        currency: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        memo: str | Omit = omit,
        metadata: object | Omit = omit,
        on_release_action: str | Omit = omit,
        on_release_config: object | Omit = omit,
        release_conditions: Iterable[hold_create_params.ReleaseCondition] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a hold on funds in an account with release conditions

        Args:
          account_id: Account to hold funds in

          amount: Amount in cents to hold

          on_release_action: Action to take when released

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/payments/v1/holds",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "currency": currency,
                    "expires_at": expires_at,
                    "memo": memo,
                    "metadata": metadata,
                    "on_release_action": on_release_action,
                    "on_release_config": on_release_config,
                    "release_conditions": release_conditions,
                },
                hold_create_params.HoldCreateParams,
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
        Get hold details by ID

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
            f"/payments/v1/holds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List holds with optional filters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/payments/v1/holds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    hold_list_params.HoldListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def approve(
        self,
        id: str,
        *,
        approver_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Record an approval for a hold release condition

        Args:
          approver_id: ID of the approver (party or user)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/payments/v1/holds/{id}/approve",
            body=await async_maybe_transform({"approver_id": approver_id}, hold_approve_params.HoldApproveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        Cancel an active hold

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
            f"/payments/v1/holds/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def release(
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
        Manually release a hold

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
            f"/payments/v1/holds/{id}/release",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class HoldsResourceWithRawResponse:
    def __init__(self, holds: HoldsResource) -> None:
        self._holds = holds

        self.create = to_raw_response_wrapper(
            holds.create,
        )
        self.retrieve = to_raw_response_wrapper(
            holds.retrieve,
        )
        self.list = to_raw_response_wrapper(
            holds.list,
        )
        self.approve = to_raw_response_wrapper(
            holds.approve,
        )
        self.cancel = to_raw_response_wrapper(
            holds.cancel,
        )
        self.release = to_raw_response_wrapper(
            holds.release,
        )


class AsyncHoldsResourceWithRawResponse:
    def __init__(self, holds: AsyncHoldsResource) -> None:
        self._holds = holds

        self.create = async_to_raw_response_wrapper(
            holds.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            holds.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            holds.list,
        )
        self.approve = async_to_raw_response_wrapper(
            holds.approve,
        )
        self.cancel = async_to_raw_response_wrapper(
            holds.cancel,
        )
        self.release = async_to_raw_response_wrapper(
            holds.release,
        )


class HoldsResourceWithStreamingResponse:
    def __init__(self, holds: HoldsResource) -> None:
        self._holds = holds

        self.create = to_streamed_response_wrapper(
            holds.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            holds.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            holds.list,
        )
        self.approve = to_streamed_response_wrapper(
            holds.approve,
        )
        self.cancel = to_streamed_response_wrapper(
            holds.cancel,
        )
        self.release = to_streamed_response_wrapper(
            holds.release,
        )


class AsyncHoldsResourceWithStreamingResponse:
    def __init__(self, holds: AsyncHoldsResource) -> None:
        self._holds = holds

        self.create = async_to_streamed_response_wrapper(
            holds.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            holds.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            holds.list,
        )
        self.approve = async_to_streamed_response_wrapper(
            holds.approve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            holds.cancel,
        )
        self.release = async_to_streamed_response_wrapper(
            holds.release,
        )
