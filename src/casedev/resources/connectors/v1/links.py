# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.connectors.v1 import link_list_params, link_delete_params, link_update_params, link_list_objects_params

__all__ = ["LinksResource", "AsyncLinksResource"]


class LinksResource(SyncAPIResource):
    """Import and export between provider folders (Google Drive) and vaults"""

    @cached_property
    def with_raw_response(self) -> LinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return LinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return LinksResourceWithStreamingResponse(self)

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
        """Retrieve one link: state, counts, and embedded active_run/last_run.

        Poll this
        after POST /transfer.

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
            path_template("/connectors/v1/links/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        id: str,
        *,
        mode: Literal["once", "synced"] | Omit = omit,
        policy: object | Omit = omit,
        state: Literal["paused", "ready"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Pause/resume a link (state "paused" | "ready"), change its mode (synced -> once
        is the sync downgrade), or edit its policy in place.

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
            path_template("/connectors/v1/links/{id}", id=id),
            body=maybe_transform(
                {
                    "mode": mode,
                    "policy": policy,
                    "state": state,
                },
                link_update_params.LinkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        connection_id: str | Omit = omit,
        direction: Literal["import", "export"] | Omit = omit,
        mode: Literal["once", "synced"] | Omit = omit,
        pair_id: str | Omit = omit,
        state: Literal["ready", "running", "active", "paused", "orphaned", "error"] | Omit = omit,
        vault_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List transfer links, filterable by vault, connection, direction, mode, and
        state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/connectors/v1/links",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connection_id": connection_id,
                        "direction": direction,
                        "mode": mode,
                        "pair_id": pair_id,
                        "state": state,
                        "vault_id": vault_id,
                    },
                    link_list_params.LinkListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        id: str,
        *,
        vault_docs: Literal["keep", "delete"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a link and its ledger.

        vault_docs=delete additionally removes the vault
        documents an import link brought in (default: keep).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/connectors/v1/links/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"vault_docs": vault_docs}, link_delete_params.LinkDeleteParams),
            ),
            cast_to=NoneType,
        )

    def list_objects(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        state: Literal["pending", "transferring", "ingesting", "synced", "skipped", "failed", "tombstoned"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Per-file transfer ledger for a link: provider item, vault object, path, content
        version, state, and error.

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
            path_template("/connectors/v1/links/{id}/objects", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "state": state,
                    },
                    link_list_objects_params.LinkListObjectsParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncLinksResource(AsyncAPIResource):
    """Import and export between provider folders (Google Drive) and vaults"""

    @cached_property
    def with_raw_response(self) -> AsyncLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncLinksResourceWithStreamingResponse(self)

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
        """Retrieve one link: state, counts, and embedded active_run/last_run.

        Poll this
        after POST /transfer.

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
            path_template("/connectors/v1/links/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        id: str,
        *,
        mode: Literal["once", "synced"] | Omit = omit,
        policy: object | Omit = omit,
        state: Literal["paused", "ready"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Pause/resume a link (state "paused" | "ready"), change its mode (synced -> once
        is the sync downgrade), or edit its policy in place.

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
            path_template("/connectors/v1/links/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "mode": mode,
                    "policy": policy,
                    "state": state,
                },
                link_update_params.LinkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        connection_id: str | Omit = omit,
        direction: Literal["import", "export"] | Omit = omit,
        mode: Literal["once", "synced"] | Omit = omit,
        pair_id: str | Omit = omit,
        state: Literal["ready", "running", "active", "paused", "orphaned", "error"] | Omit = omit,
        vault_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List transfer links, filterable by vault, connection, direction, mode, and
        state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/connectors/v1/links",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connection_id": connection_id,
                        "direction": direction,
                        "mode": mode,
                        "pair_id": pair_id,
                        "state": state,
                        "vault_id": vault_id,
                    },
                    link_list_params.LinkListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        id: str,
        *,
        vault_docs: Literal["keep", "delete"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a link and its ledger.

        vault_docs=delete additionally removes the vault
        documents an import link brought in (default: keep).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/connectors/v1/links/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"vault_docs": vault_docs}, link_delete_params.LinkDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def list_objects(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        state: Literal["pending", "transferring", "ingesting", "synced", "skipped", "failed", "tombstoned"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Per-file transfer ledger for a link: provider item, vault object, path, content
        version, state, and error.

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
            path_template("/connectors/v1/links/{id}/objects", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "state": state,
                    },
                    link_list_objects_params.LinkListObjectsParams,
                ),
            ),
            cast_to=NoneType,
        )


class LinksResourceWithRawResponse:
    def __init__(self, links: LinksResource) -> None:
        self._links = links

        self.retrieve = to_raw_response_wrapper(
            links.retrieve,
        )
        self.update = to_raw_response_wrapper(
            links.update,
        )
        self.list = to_raw_response_wrapper(
            links.list,
        )
        self.delete = to_raw_response_wrapper(
            links.delete,
        )
        self.list_objects = to_raw_response_wrapper(
            links.list_objects,
        )


class AsyncLinksResourceWithRawResponse:
    def __init__(self, links: AsyncLinksResource) -> None:
        self._links = links

        self.retrieve = async_to_raw_response_wrapper(
            links.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            links.update,
        )
        self.list = async_to_raw_response_wrapper(
            links.list,
        )
        self.delete = async_to_raw_response_wrapper(
            links.delete,
        )
        self.list_objects = async_to_raw_response_wrapper(
            links.list_objects,
        )


class LinksResourceWithStreamingResponse:
    def __init__(self, links: LinksResource) -> None:
        self._links = links

        self.retrieve = to_streamed_response_wrapper(
            links.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            links.update,
        )
        self.list = to_streamed_response_wrapper(
            links.list,
        )
        self.delete = to_streamed_response_wrapper(
            links.delete,
        )
        self.list_objects = to_streamed_response_wrapper(
            links.list_objects,
        )


class AsyncLinksResourceWithStreamingResponse:
    def __init__(self, links: AsyncLinksResource) -> None:
        self._links = links

        self.retrieve = async_to_streamed_response_wrapper(
            links.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            links.update,
        )
        self.list = async_to_streamed_response_wrapper(
            links.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            links.delete,
        )
        self.list_objects = async_to_streamed_response_wrapper(
            links.list_objects,
        )
