# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.payments.v1 import transfer_list_params, transfer_create_params

__all__ = ["TransfersResource", "AsyncTransfersResource"]


class TransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return TransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return TransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        from_account_id: str,
        to_account_id: str,
        memo: str | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a transfer between payment accounts

        Args:
          amount: Amount in cents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/payments/v1/transfers",
            body=maybe_transform(
                {
                    "amount": amount,
                    "from_account_id": from_account_id,
                    "to_account_id": to_account_id,
                    "memo": memo,
                    "metadata": metadata,
                },
                transfer_create_params.TransferCreateParams,
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
        Get transfer details by ID

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
            f"/payments/v1/transfers/{id}",
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
        status: str | Omit = omit,
        to_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List transfers with optional filters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/payments/v1/transfers",
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
                        "status": status,
                        "to_account_id": to_account_id,
                    },
                    transfer_list_params.TransferListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def approve(
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
        Approve and execute a pending transfer

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
            f"/payments/v1/transfers/{id}/approve",
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
        Cancel a pending transfer

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
            f"/payments/v1/transfers/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        from_account_id: str,
        to_account_id: str,
        memo: str | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a transfer between payment accounts

        Args:
          amount: Amount in cents

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/payments/v1/transfers",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "from_account_id": from_account_id,
                    "to_account_id": to_account_id,
                    "memo": memo,
                    "metadata": metadata,
                },
                transfer_create_params.TransferCreateParams,
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
        Get transfer details by ID

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
            f"/payments/v1/transfers/{id}",
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
        status: str | Omit = omit,
        to_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List transfers with optional filters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/payments/v1/transfers",
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
                        "status": status,
                        "to_account_id": to_account_id,
                    },
                    transfer_list_params.TransferListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def approve(
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
        Approve and execute a pending transfer

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
            f"/payments/v1/transfers/{id}/approve",
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
        Cancel a pending transfer

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
            f"/payments/v1/transfers/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TransfersResourceWithRawResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.create = to_raw_response_wrapper(
            transfers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            transfers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            transfers.list,
        )
        self.approve = to_raw_response_wrapper(
            transfers.approve,
        )
        self.cancel = to_raw_response_wrapper(
            transfers.cancel,
        )


class AsyncTransfersResourceWithRawResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.create = async_to_raw_response_wrapper(
            transfers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            transfers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            transfers.list,
        )
        self.approve = async_to_raw_response_wrapper(
            transfers.approve,
        )
        self.cancel = async_to_raw_response_wrapper(
            transfers.cancel,
        )


class TransfersResourceWithStreamingResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.create = to_streamed_response_wrapper(
            transfers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            transfers.list,
        )
        self.approve = to_streamed_response_wrapper(
            transfers.approve,
        )
        self.cancel = to_streamed_response_wrapper(
            transfers.cancel,
        )


class AsyncTransfersResourceWithStreamingResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.create = async_to_streamed_response_wrapper(
            transfers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            transfers.list,
        )
        self.approve = async_to_streamed_response_wrapper(
            transfers.approve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            transfers.cancel,
        )
