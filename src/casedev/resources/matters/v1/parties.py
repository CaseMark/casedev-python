# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.matters.v1 import party_list_params, party_create_params

__all__ = ["PartiesResource", "AsyncPartiesResource"]


class PartiesResource(SyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

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
        addresses: Iterable[Dict[str, object]] | Omit = omit,
        custom_fields: Optional[Dict[str, object]] | Omit = omit,
        email: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        phone: str | Omit = omit,
        type: Literal["person", "organization"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a reusable legal party for the authenticated organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/matters/v1/parties",
            body=maybe_transform(
                {
                    "name": name,
                    "addresses": addresses,
                    "custom_fields": custom_fields,
                    "email": email,
                    "metadata": metadata,
                    "notes": notes,
                    "phone": phone,
                    "type": type,
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
        party_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get a reusable legal party by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not party_id:
            raise ValueError(f"Expected a non-empty value for `party_id` but received {party_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/matters/v1/parties/{party_id}", party_id=party_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        party_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a reusable legal party.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not party_id:
            raise ValueError(f"Expected a non-empty value for `party_id` but received {party_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/matters/v1/parties/{party_id}", party_id=party_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        email: str | Omit = omit,
        query: str | Omit = omit,
        type: Literal["person", "organization"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List reusable legal parties for the authenticated organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/matters/v1/parties",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email": email,
                        "query": query,
                        "type": type,
                    },
                    party_list_params.PartyListParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncPartiesResource(AsyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

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
        addresses: Iterable[Dict[str, object]] | Omit = omit,
        custom_fields: Optional[Dict[str, object]] | Omit = omit,
        email: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        phone: str | Omit = omit,
        type: Literal["person", "organization"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a reusable legal party for the authenticated organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/matters/v1/parties",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "addresses": addresses,
                    "custom_fields": custom_fields,
                    "email": email,
                    "metadata": metadata,
                    "notes": notes,
                    "phone": phone,
                    "type": type,
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
        party_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get a reusable legal party by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not party_id:
            raise ValueError(f"Expected a non-empty value for `party_id` but received {party_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/matters/v1/parties/{party_id}", party_id=party_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        party_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a reusable legal party.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not party_id:
            raise ValueError(f"Expected a non-empty value for `party_id` but received {party_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/matters/v1/parties/{party_id}", party_id=party_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        email: str | Omit = omit,
        query: str | Omit = omit,
        type: Literal["person", "organization"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List reusable legal parties for the authenticated organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/matters/v1/parties",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email": email,
                        "query": query,
                        "type": type,
                    },
                    party_list_params.PartyListParams,
                ),
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
