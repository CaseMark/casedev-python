# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .vaults import (
    VaultsResource,
    AsyncVaultsResource,
    VaultsResourceWithRawResponse,
    AsyncVaultsResourceWithRawResponse,
    VaultsResourceWithStreamingResponse,
    AsyncVaultsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.connectors.v1 import installation_list_params, installation_ensure_params

__all__ = ["InstallationsResource", "AsyncInstallationsResource"]


class InstallationsResource(SyncAPIResource):
    """Import and export between provider folders (Google Drive) and vaults"""

    @cached_property
    def vaults(self) -> VaultsResource:
        """Import and export between provider folders (Google Drive) and vaults"""
        return VaultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> InstallationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return InstallationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstallationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return InstallationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        application: str | Omit = omit,
        external_tenant_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List application installations (tenants) in this organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/connectors/v1/installations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "application": application,
                        "external_tenant_id": external_tenant_id,
                    },
                    installation_list_params.InstallationListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def ensure(
        self,
        *,
        application: str,
        external_tenant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Idempotently create (or return) the installation for (application,
        external_tenant_id) in this organization. Send the returned installation id as
        X-Case-Installation-Id on connector requests to scope them to this tenant.

        Args:
          application: Consuming application key (e.g. "p3").

          external_tenant_id: The application's own tenant identifier (e.g. a P3 organization id).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/connectors/v1/installations",
            body=maybe_transform(
                {
                    "application": application,
                    "external_tenant_id": external_tenant_id,
                },
                installation_ensure_params.InstallationEnsureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncInstallationsResource(AsyncAPIResource):
    """Import and export between provider folders (Google Drive) and vaults"""

    @cached_property
    def vaults(self) -> AsyncVaultsResource:
        """Import and export between provider folders (Google Drive) and vaults"""
        return AsyncVaultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInstallationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstallationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstallationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncInstallationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        application: str | Omit = omit,
        external_tenant_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List application installations (tenants) in this organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/connectors/v1/installations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "application": application,
                        "external_tenant_id": external_tenant_id,
                    },
                    installation_list_params.InstallationListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def ensure(
        self,
        *,
        application: str,
        external_tenant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Idempotently create (or return) the installation for (application,
        external_tenant_id) in this organization. Send the returned installation id as
        X-Case-Installation-Id on connector requests to scope them to this tenant.

        Args:
          application: Consuming application key (e.g. "p3").

          external_tenant_id: The application's own tenant identifier (e.g. a P3 organization id).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/connectors/v1/installations",
            body=await async_maybe_transform(
                {
                    "application": application,
                    "external_tenant_id": external_tenant_id,
                },
                installation_ensure_params.InstallationEnsureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class InstallationsResourceWithRawResponse:
    def __init__(self, installations: InstallationsResource) -> None:
        self._installations = installations

        self.list = to_raw_response_wrapper(
            installations.list,
        )
        self.ensure = to_raw_response_wrapper(
            installations.ensure,
        )

    @cached_property
    def vaults(self) -> VaultsResourceWithRawResponse:
        """Import and export between provider folders (Google Drive) and vaults"""
        return VaultsResourceWithRawResponse(self._installations.vaults)


class AsyncInstallationsResourceWithRawResponse:
    def __init__(self, installations: AsyncInstallationsResource) -> None:
        self._installations = installations

        self.list = async_to_raw_response_wrapper(
            installations.list,
        )
        self.ensure = async_to_raw_response_wrapper(
            installations.ensure,
        )

    @cached_property
    def vaults(self) -> AsyncVaultsResourceWithRawResponse:
        """Import and export between provider folders (Google Drive) and vaults"""
        return AsyncVaultsResourceWithRawResponse(self._installations.vaults)


class InstallationsResourceWithStreamingResponse:
    def __init__(self, installations: InstallationsResource) -> None:
        self._installations = installations

        self.list = to_streamed_response_wrapper(
            installations.list,
        )
        self.ensure = to_streamed_response_wrapper(
            installations.ensure,
        )

    @cached_property
    def vaults(self) -> VaultsResourceWithStreamingResponse:
        """Import and export between provider folders (Google Drive) and vaults"""
        return VaultsResourceWithStreamingResponse(self._installations.vaults)


class AsyncInstallationsResourceWithStreamingResponse:
    def __init__(self, installations: AsyncInstallationsResource) -> None:
        self._installations = installations

        self.list = async_to_streamed_response_wrapper(
            installations.list,
        )
        self.ensure = async_to_streamed_response_wrapper(
            installations.ensure,
        )

    @cached_property
    def vaults(self) -> AsyncVaultsResourceWithStreamingResponse:
        """Import and export between provider folders (Google Drive) and vaults"""
        return AsyncVaultsResourceWithStreamingResponse(self._installations.vaults)
