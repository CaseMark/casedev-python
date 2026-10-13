# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.connectors.v1 import (
    connection_list_params,
    connection_browse_params,
    connection_create_params,
    connection_delete_params,
    connection_update_all_params,
)
from ....types.connectors.v1.connection_list_response import ConnectionListResponse
from ....types.connectors.v1.connection_browse_response import ConnectionBrowseResponse
from ....types.connectors.v1.connection_create_response import ConnectionCreateResponse

__all__ = ["ConnectionsResource", "AsyncConnectionsResource"]


class ConnectionsResource(SyncAPIResource):
    """Import and export between provider folders and vaults"""

    @cached_property
    def with_raw_response(self) -> ConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return ConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return ConnectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        provider: Literal["box", "clio", "dropbox", "gdrive", "microsoft", "smokeball"],
        return_url: str,
        scope_tier: Literal[
            "box.readwrite",
            "box.readwrite.webhooks",
            "clio.us",
            "dropbox.readwrite",
            "drive",
            "microsoft.read",
            "microsoft.personal.read",
            "microsoft.write",
            "microsoft.personal.write",
            "smokeball.us",
            "smokeball.us.staging",
        ]
        | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionCreateResponse:
        """
        Create a pending provider connection and return a one-time connect_url for the
        hosted OAuth flow. The user completes provider consent at connect_url and is
        redirected to return_url with ?connection_id=.

        Args:
          return_url: HTTPS URL the user is sent back to after consent.

          scope_tier: Provider-specific OAuth permission tier. Omit to use the provider's default.
              Microsoft defaults to organizational OneDrive/SharePoint; use
              microsoft.personal.read for a personal Microsoft account's own OneDrive.
              Microsoft write tiers are a separately gated private pilot; exports and paired
              sync are not yet available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return self._post(
            "/connectors/v1/connections",
            body=maybe_transform(
                {
                    "provider": provider,
                    "return_url": return_url,
                    "scope_tier": scope_tier,
                },
                connection_create_params.ConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieve one provider connection, including account identity and health.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/connectors/v1/connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        provider: str | Omit = omit,
        status: Literal["pending", "healthy", "reauth_required", "revoked", "throttled"] | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionListResponse:
        """List provider connections for the organization, with health status.

        Returns at
        most `limit` connections (default 200, maximum 200). When `pagination.has_more`
        is true, replay `pagination.next_cursor` as `?cursor=` to fetch the following
        page. Cursors are opaque and are only valid for the exact filter set and
        installation/subject scope they were issued under.

        Args:
          cursor: Opaque continuation cursor from `pagination.next_cursor` of the previous page.
              Must be replayed with the same filters and scope that produced it.

          limit: Connections per page (1-200). Defaults to 200.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return self._get(
            "/connectors/v1/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "provider": provider,
                        "status": status,
                    },
                    connection_list_params.ConnectionListParams,
                ),
            ),
            cast_to=ConnectionListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        purge: bool | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unlink a provider account: revoke tokens at the provider and delete them.
        purge=true additionally deletes the vault documents its import links brought in.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return self._delete(
            path_template("/connectors/v1/connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"purge": purge}, connection_delete_params.ConnectionDeleteParams),
            ),
            cast_to=NoneType,
        )

    def browse(
        self,
        id: str,
        *,
        container: str | Omit = omit,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        parent: str | Omit = omit,
        query: str | Omit = omit,
        site: str | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionBrowseResponse:
        """Browse the provider one level at a time.

        Without a site, container, or parent,
        returns top-level resources. Pass the stable browse_ref fields returned by one
        response to navigate into the next level. Returns 403
        provider_scope_insufficient when the connection scope cannot browse server-side.
        Clio browsing shares request capacity with background runs; throttled responses
        include Retry-After when a retry deadline is known.

        Args:
          container: Container id to list, or the container containing parent

          parent: Folder id to list

          query: Optional provider-supported search text

          site: Site id to list

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/connectors/v1/connections/{id}/browse", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "container": container,
                        "cursor": cursor,
                        "page_size": page_size,
                        "parent": parent,
                        "query": query,
                        "site": site,
                    },
                    connection_browse_params.ConnectionBrowseParams,
                ),
            ),
            cast_to=ConnectionBrowseResponse,
        )

    def update_all(
        self,
        *,
        confirm_organization_wide: Literal[True],
        enabled: bool,
        provider: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Enable or disable new runs and scheduled syncs for one provider across the
        authenticated organization or installation. This organization-wide operation
        requires explicit confirmation. Existing credentials, links, and imported files
        are preserved; active runs are not interrupted.

        Args:
          confirm_organization_wide: Confirms that this change applies to every user connection in scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            "/connectors/v1/connections",
            body=maybe_transform(
                {
                    "confirm_organization_wide": confirm_organization_wide,
                    "enabled": enabled,
                    "provider": provider,
                },
                connection_update_all_params.ConnectionUpdateAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncConnectionsResource(AsyncAPIResource):
    """Import and export between provider folders and vaults"""

    @cached_property
    def with_raw_response(self) -> AsyncConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncConnectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        provider: Literal["box", "clio", "dropbox", "gdrive", "microsoft", "smokeball"],
        return_url: str,
        scope_tier: Literal[
            "box.readwrite",
            "box.readwrite.webhooks",
            "clio.us",
            "dropbox.readwrite",
            "drive",
            "microsoft.read",
            "microsoft.personal.read",
            "microsoft.write",
            "microsoft.personal.write",
            "smokeball.us",
            "smokeball.us.staging",
        ]
        | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionCreateResponse:
        """
        Create a pending provider connection and return a one-time connect_url for the
        hosted OAuth flow. The user completes provider consent at connect_url and is
        redirected to return_url with ?connection_id=.

        Args:
          return_url: HTTPS URL the user is sent back to after consent.

          scope_tier: Provider-specific OAuth permission tier. Omit to use the provider's default.
              Microsoft defaults to organizational OneDrive/SharePoint; use
              microsoft.personal.read for a personal Microsoft account's own OneDrive.
              Microsoft write tiers are a separately gated private pilot; exports and paired
              sync are not yet available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/connectors/v1/connections",
            body=await async_maybe_transform(
                {
                    "provider": provider,
                    "return_url": return_url,
                    "scope_tier": scope_tier,
                },
                connection_create_params.ConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieve one provider connection, including account identity and health.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/connectors/v1/connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        provider: str | Omit = omit,
        status: Literal["pending", "healthy", "reauth_required", "revoked", "throttled"] | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionListResponse:
        """List provider connections for the organization, with health status.

        Returns at
        most `limit` connections (default 200, maximum 200). When `pagination.has_more`
        is true, replay `pagination.next_cursor` as `?cursor=` to fetch the following
        page. Cursors are opaque and are only valid for the exact filter set and
        installation/subject scope they were issued under.

        Args:
          cursor: Opaque continuation cursor from `pagination.next_cursor` of the previous page.
              Must be replayed with the same filters and scope that produced it.

          limit: Connections per page (1-200). Defaults to 200.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return await self._get(
            "/connectors/v1/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "provider": provider,
                        "status": status,
                    },
                    connection_list_params.ConnectionListParams,
                ),
            ),
            cast_to=ConnectionListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        purge: bool | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unlink a provider account: revoke tokens at the provider and delete them.
        purge=true additionally deletes the vault documents its import links brought in.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return await self._delete(
            path_template("/connectors/v1/connections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"purge": purge}, connection_delete_params.ConnectionDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def browse(
        self,
        id: str,
        *,
        container: str | Omit = omit,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        parent: str | Omit = omit,
        query: str | Omit = omit,
        site: str | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionBrowseResponse:
        """Browse the provider one level at a time.

        Without a site, container, or parent,
        returns top-level resources. Pass the stable browse_ref fields returned by one
        response to navigate into the next level. Returns 403
        provider_scope_insufficient when the connection scope cannot browse server-side.
        Clio browsing shares request capacity with background runs; throttled responses
        include Retry-After when a retry deadline is known.

        Args:
          container: Container id to list, or the container containing parent

          parent: Folder id to list

          query: Optional provider-supported search text

          site: Site id to list

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/connectors/v1/connections/{id}/browse", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "container": container,
                        "cursor": cursor,
                        "page_size": page_size,
                        "parent": parent,
                        "query": query,
                        "site": site,
                    },
                    connection_browse_params.ConnectionBrowseParams,
                ),
            ),
            cast_to=ConnectionBrowseResponse,
        )

    async def update_all(
        self,
        *,
        confirm_organization_wide: Literal[True],
        enabled: bool,
        provider: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Enable or disable new runs and scheduled syncs for one provider across the
        authenticated organization or installation. This organization-wide operation
        requires explicit confirmation. Existing credentials, links, and imported files
        are preserved; active runs are not interrupted.

        Args:
          confirm_organization_wide: Confirms that this change applies to every user connection in scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            "/connectors/v1/connections",
            body=await async_maybe_transform(
                {
                    "confirm_organization_wide": confirm_organization_wide,
                    "enabled": enabled,
                    "provider": provider,
                },
                connection_update_all_params.ConnectionUpdateAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ConnectionsResourceWithRawResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.create = to_raw_response_wrapper(
            connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            connections.retrieve,
        )
        self.list = to_raw_response_wrapper(
            connections.list,
        )
        self.delete = to_raw_response_wrapper(
            connections.delete,
        )
        self.browse = to_raw_response_wrapper(
            connections.browse,
        )
        self.update_all = to_raw_response_wrapper(
            connections.update_all,
        )


class AsyncConnectionsResourceWithRawResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.create = async_to_raw_response_wrapper(
            connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            connections.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            connections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connections.delete,
        )
        self.browse = async_to_raw_response_wrapper(
            connections.browse,
        )
        self.update_all = async_to_raw_response_wrapper(
            connections.update_all,
        )


class ConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.create = to_streamed_response_wrapper(
            connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            connections.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            connections.delete,
        )
        self.browse = to_streamed_response_wrapper(
            connections.browse,
        )
        self.update_all = to_streamed_response_wrapper(
            connections.update_all,
        )


class AsyncConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.create = async_to_streamed_response_wrapper(
            connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            connections.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connections.delete,
        )
        self.browse = async_to_streamed_response_wrapper(
            connections.browse,
        )
        self.update_all = async_to_streamed_response_wrapper(
            connections.update_all,
        )
