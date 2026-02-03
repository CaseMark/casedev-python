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
from ....types.payments.v1 import party_list_params, party_create_params, party_update_params

__all__ = ["PartiesResource", "AsyncPartiesResource"]


class PartiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PartiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return PartiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PartiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return PartiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        type: Literal["individual", "organization"],
        address_line1: str | Omit = omit,
        city: str | Omit = omit,
        country: str | Omit = omit,
        email: str | Omit = omit,
        metadata: object | Omit = omit,
        phone: str | Omit = omit,
        postal_code: str | Omit = omit,
        role: Literal["client", "vendor", "counsel", "expert", "lien_holder", "funder", "opposing_party", "other"]
        | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a new payment party (client, vendor, counsel, etc.)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/payments/v1/parties",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "address_line1": address_line1,
                    "city": city,
                    "country": country,
                    "email": email,
                    "metadata": metadata,
                    "phone": phone,
                    "postal_code": postal_code,
                    "role": role,
                    "state": state,
                },
                party_create_params.PartyCreateParams,
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
        Get party details by ID

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
            f"/payments/v1/parties/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        id: str,
        *,
        address_line1: str | Omit = omit,
        address_line2: str | Omit = omit,
        city: str | Omit = omit,
        country: str | Omit = omit,
        email: str | Omit = omit,
        is_active: bool | Omit = omit,
        metadata: object | Omit = omit,
        name: str | Omit = omit,
        notes: str | Omit = omit,
        phone: str | Omit = omit,
        postal_code: str | Omit = omit,
        role: Literal["client", "vendor", "counsel", "expert", "lien_holder", "funder", "opposing_party", "other"]
        | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update party details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/payments/v1/parties/{id}",
            body=maybe_transform(
                {
                    "address_line1": address_line1,
                    "address_line2": address_line2,
                    "city": city,
                    "country": country,
                    "email": email,
                    "is_active": is_active,
                    "metadata": metadata,
                    "name": name,
                    "notes": notes,
                    "phone": phone,
                    "postal_code": postal_code,
                    "role": role,
                    "state": state,
                },
                party_update_params.PartyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        role: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List payment parties with optional filters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/payments/v1/parties",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "role": role,
                        "type": type,
                    },
                    party_list_params.PartyListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def list_payment_methods(
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
        List saved payment methods for a party (from Stripe)

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
            f"/payments/v1/parties/{id}/payment-methods",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPartiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPartiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPartiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPartiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncPartiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        type: Literal["individual", "organization"],
        address_line1: str | Omit = omit,
        city: str | Omit = omit,
        country: str | Omit = omit,
        email: str | Omit = omit,
        metadata: object | Omit = omit,
        phone: str | Omit = omit,
        postal_code: str | Omit = omit,
        role: Literal["client", "vendor", "counsel", "expert", "lien_holder", "funder", "opposing_party", "other"]
        | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a new payment party (client, vendor, counsel, etc.)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/payments/v1/parties",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "address_line1": address_line1,
                    "city": city,
                    "country": country,
                    "email": email,
                    "metadata": metadata,
                    "phone": phone,
                    "postal_code": postal_code,
                    "role": role,
                    "state": state,
                },
                party_create_params.PartyCreateParams,
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
        Get party details by ID

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
            f"/payments/v1/parties/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        id: str,
        *,
        address_line1: str | Omit = omit,
        address_line2: str | Omit = omit,
        city: str | Omit = omit,
        country: str | Omit = omit,
        email: str | Omit = omit,
        is_active: bool | Omit = omit,
        metadata: object | Omit = omit,
        name: str | Omit = omit,
        notes: str | Omit = omit,
        phone: str | Omit = omit,
        postal_code: str | Omit = omit,
        role: Literal["client", "vendor", "counsel", "expert", "lien_holder", "funder", "opposing_party", "other"]
        | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update party details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/payments/v1/parties/{id}",
            body=await async_maybe_transform(
                {
                    "address_line1": address_line1,
                    "address_line2": address_line2,
                    "city": city,
                    "country": country,
                    "email": email,
                    "is_active": is_active,
                    "metadata": metadata,
                    "name": name,
                    "notes": notes,
                    "phone": phone,
                    "postal_code": postal_code,
                    "role": role,
                    "state": state,
                },
                party_update_params.PartyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        role: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List payment parties with optional filters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/payments/v1/parties",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "role": role,
                        "type": type,
                    },
                    party_list_params.PartyListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def list_payment_methods(
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
        List saved payment methods for a party (from Stripe)

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
            f"/payments/v1/parties/{id}/payment-methods",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PartiesResourceWithRawResponse:
    def __init__(self, parties: PartiesResource) -> None:
        self._parties = parties

        self.create = to_raw_response_wrapper(
            parties.create,
        )
        self.retrieve = to_raw_response_wrapper(
            parties.retrieve,
        )
        self.update = to_raw_response_wrapper(
            parties.update,
        )
        self.list = to_raw_response_wrapper(
            parties.list,
        )
        self.list_payment_methods = to_raw_response_wrapper(
            parties.list_payment_methods,
        )


class AsyncPartiesResourceWithRawResponse:
    def __init__(self, parties: AsyncPartiesResource) -> None:
        self._parties = parties

        self.create = async_to_raw_response_wrapper(
            parties.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            parties.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            parties.update,
        )
        self.list = async_to_raw_response_wrapper(
            parties.list,
        )
        self.list_payment_methods = async_to_raw_response_wrapper(
            parties.list_payment_methods,
        )


class PartiesResourceWithStreamingResponse:
    def __init__(self, parties: PartiesResource) -> None:
        self._parties = parties

        self.create = to_streamed_response_wrapper(
            parties.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            parties.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            parties.update,
        )
        self.list = to_streamed_response_wrapper(
            parties.list,
        )
        self.list_payment_methods = to_streamed_response_wrapper(
            parties.list_payment_methods,
        )


class AsyncPartiesResourceWithStreamingResponse:
    def __init__(self, parties: AsyncPartiesResource) -> None:
        self._parties = parties

        self.create = async_to_streamed_response_wrapper(
            parties.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            parties.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            parties.update,
        )
        self.list = async_to_streamed_response_wrapper(
            parties.list,
        )
        self.list_payment_methods = async_to_streamed_response_wrapper(
            parties.list_payment_methods,
        )
