# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
from ....types.payments.v1 import ledger_get_params, ledger_list_transactions_params

__all__ = ["LedgerResource", "AsyncLedgerResource"]


class LedgerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return LedgerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return LedgerResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        transaction_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List ledger entries with optional filters by account, transaction, or date range

        Args:
          account_id: Filter by account

          transaction_id: Filter by transaction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/payments/v1/ledger",
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
                        "transaction_id": transaction_id,
                    },
                    ledger_get_params.LedgerGetParams,
                ),
            ),
            cast_to=NoneType,
        )

    def list_transactions(
        self,
        *,
        end_date: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        reference_id: str | Omit = omit,
        reference_type: str | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Query ledger transactions with optional filters

        Args:
          reference_id: Filter by reference ID

          reference_type: Filter by reference type (transfer, charge, payout, etc.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/payments/v1/ledger/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "offset": offset,
                        "reference_id": reference_id,
                        "reference_type": reference_type,
                        "start_date": start_date,
                    },
                    ledger_list_transactions_params.LedgerListTransactionsParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncLedgerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLedgerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncLedgerResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        transaction_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List ledger entries with optional filters by account, transaction, or date range

        Args:
          account_id: Filter by account

          transaction_id: Filter by transaction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/payments/v1/ledger",
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
                        "transaction_id": transaction_id,
                    },
                    ledger_get_params.LedgerGetParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def list_transactions(
        self,
        *,
        end_date: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        reference_id: str | Omit = omit,
        reference_type: str | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Query ledger transactions with optional filters

        Args:
          reference_id: Filter by reference ID

          reference_type: Filter by reference type (transfer, charge, payout, etc.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/payments/v1/ledger/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "offset": offset,
                        "reference_id": reference_id,
                        "reference_type": reference_type,
                        "start_date": start_date,
                    },
                    ledger_list_transactions_params.LedgerListTransactionsParams,
                ),
            ),
            cast_to=NoneType,
        )


class LedgerResourceWithRawResponse:
    def __init__(self, ledger: LedgerResource) -> None:
        self._ledger = ledger

        self.get = to_raw_response_wrapper(
            ledger.get,
        )
        self.list_transactions = to_raw_response_wrapper(
            ledger.list_transactions,
        )


class AsyncLedgerResourceWithRawResponse:
    def __init__(self, ledger: AsyncLedgerResource) -> None:
        self._ledger = ledger

        self.get = async_to_raw_response_wrapper(
            ledger.get,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            ledger.list_transactions,
        )


class LedgerResourceWithStreamingResponse:
    def __init__(self, ledger: LedgerResource) -> None:
        self._ledger = ledger

        self.get = to_streamed_response_wrapper(
            ledger.get,
        )
        self.list_transactions = to_streamed_response_wrapper(
            ledger.list_transactions,
        )


class AsyncLedgerResourceWithStreamingResponse:
    def __init__(self, ledger: AsyncLedgerResource) -> None:
        self._ledger = ledger

        self.get = async_to_streamed_response_wrapper(
            ledger.get,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            ledger.list_transactions,
        )
