# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["FromVaultObjectResource", "AsyncFromVaultObjectResource"]


class FromVaultObjectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FromVaultObjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return FromVaultObjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FromVaultObjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return FromVaultObjectResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Promote vault object to document template"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/document-templates/from-vault-object",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFromVaultObjectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFromVaultObjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFromVaultObjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFromVaultObjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncFromVaultObjectResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Promote vault object to document template"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/document-templates/from-vault-object",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FromVaultObjectResourceWithRawResponse:
    def __init__(self, from_vault_object: FromVaultObjectResource) -> None:
        self._from_vault_object = from_vault_object

        self.create = to_raw_response_wrapper(
            from_vault_object.create,
        )


class AsyncFromVaultObjectResourceWithRawResponse:
    def __init__(self, from_vault_object: AsyncFromVaultObjectResource) -> None:
        self._from_vault_object = from_vault_object

        self.create = async_to_raw_response_wrapper(
            from_vault_object.create,
        )


class FromVaultObjectResourceWithStreamingResponse:
    def __init__(self, from_vault_object: FromVaultObjectResource) -> None:
        self._from_vault_object = from_vault_object

        self.create = to_streamed_response_wrapper(
            from_vault_object.create,
        )


class AsyncFromVaultObjectResourceWithStreamingResponse:
    def __init__(self, from_vault_object: AsyncFromVaultObjectResource) -> None:
        self._from_vault_object = from_vault_object

        self.create = async_to_streamed_response_wrapper(
            from_vault_object.create,
        )
