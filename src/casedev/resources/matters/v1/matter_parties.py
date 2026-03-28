# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
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
from ....types.matters.v1 import matter_party_create_params

__all__ = ["MatterPartiesResource", "AsyncMatterPartiesResource"]


class MatterPartiesResource(SyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> MatterPartiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return MatterPartiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MatterPartiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return MatterPartiesResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        party_id: str,
        role: Literal[
            "client",
            "prospect",
            "opposing_party",
            "opposing_counsel",
            "co_counsel",
            "judge",
            "expert",
            "witness",
            "vendor",
            "insurer",
            "other",
        ],
        custom_fields: Optional[Dict[str, object]] | Omit = omit,
        is_primary: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        set_as_client: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Attach a reusable party to a matter with a matter-specific role.

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
            path_template("/matters/v1/{id}/parties", id=id),
            body=maybe_transform(
                {
                    "party_id": party_id,
                    "role": role,
                    "custom_fields": custom_fields,
                    "is_primary": is_primary,
                    "metadata": metadata,
                    "notes": notes,
                    "set_as_client": set_as_client,
                },
                matter_party_create_params.MatterPartyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
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
        List parties attached to a matter.

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
            path_template("/matters/v1/{id}/parties", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMatterPartiesResource(AsyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> AsyncMatterPartiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMatterPartiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMatterPartiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncMatterPartiesResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        party_id: str,
        role: Literal[
            "client",
            "prospect",
            "opposing_party",
            "opposing_counsel",
            "co_counsel",
            "judge",
            "expert",
            "witness",
            "vendor",
            "insurer",
            "other",
        ],
        custom_fields: Optional[Dict[str, object]] | Omit = omit,
        is_primary: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        set_as_client: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Attach a reusable party to a matter with a matter-specific role.

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
            path_template("/matters/v1/{id}/parties", id=id),
            body=await async_maybe_transform(
                {
                    "party_id": party_id,
                    "role": role,
                    "custom_fields": custom_fields,
                    "is_primary": is_primary,
                    "metadata": metadata,
                    "notes": notes,
                    "set_as_client": set_as_client,
                },
                matter_party_create_params.MatterPartyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
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
        List parties attached to a matter.

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
            path_template("/matters/v1/{id}/parties", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MatterPartiesResourceWithRawResponse:
    def __init__(self, matter_parties: MatterPartiesResource) -> None:
        self._matter_parties = matter_parties

        self.create = to_raw_response_wrapper(
            matter_parties.create,
        )
        self.list = to_raw_response_wrapper(
            matter_parties.list,
        )


class AsyncMatterPartiesResourceWithRawResponse:
    def __init__(self, matter_parties: AsyncMatterPartiesResource) -> None:
        self._matter_parties = matter_parties

        self.create = async_to_raw_response_wrapper(
            matter_parties.create,
        )
        self.list = async_to_raw_response_wrapper(
            matter_parties.list,
        )


class MatterPartiesResourceWithStreamingResponse:
    def __init__(self, matter_parties: MatterPartiesResource) -> None:
        self._matter_parties = matter_parties

        self.create = to_streamed_response_wrapper(
            matter_parties.create,
        )
        self.list = to_streamed_response_wrapper(
            matter_parties.list,
        )


class AsyncMatterPartiesResourceWithStreamingResponse:
    def __init__(self, matter_parties: AsyncMatterPartiesResource) -> None:
        self._matter_parties = matter_parties

        self.create = async_to_streamed_response_wrapper(
            matter_parties.create,
        )
        self.list = async_to_streamed_response_wrapper(
            matter_parties.list,
        )
