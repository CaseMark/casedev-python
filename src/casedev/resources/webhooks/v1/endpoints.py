# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.webhooks.v1 import (
    endpoint_list_params,
    endpoint_test_params,
    endpoint_create_params,
    endpoint_update_params,
    endpoint_rotate_secret_params,
)

__all__ = ["EndpointsResource", "AsyncEndpointsResource"]


class EndpointsResource(SyncAPIResource):
    """Webhook endpoint management"""

    @cached_property
    def with_raw_response(self) -> EndpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return EndpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EndpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return EndpointsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        event_type_filters: SequenceNotStr[str],
        url: str,
        description: str | Omit = omit,
        resource_scopes: endpoint_create_params.ResourceScopes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Creates a webhook endpoint that receives platform events matching the supplied
        event-type filters. Returns the generated signing secret ONCE — the response is
        the only time it is shown in plaintext.

        Args:
          event_type_filters: Glob patterns of event types to deliver (e.g. "vault._", "ocr.job.completed",
              "_")

          url: HTTPS callback URL that will receive event deliveries

          description: Human-readable label for this endpoint

          resource_scopes: Optional per-resource allowlists. If vaultIds is set, only events for those
              vaults are delivered. Same for matterIds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/webhooks/v1/endpoints",
            body=maybe_transform(
                {
                    "event_type_filters": event_type_filters,
                    "url": url,
                    "description": description,
                    "resource_scopes": resource_scopes,
                },
                endpoint_create_params.EndpointCreateParams,
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
        Get webhook endpoint

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
            path_template("/webhooks/v1/endpoints/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        event_type_filters: SequenceNotStr[str] | Omit = omit,
        resource_scopes: Optional[endpoint_update_params.ResourceScopes] | Omit = omit,
        status: Literal["active", "disabled"] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Partially updates a webhook endpoint.

        Any omitted field is left unchanged.
        Signing secrets are rotated via the separate /rotate_secret endpoint.

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
            path_template("/webhooks/v1/endpoints/{id}", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "event_type_filters": event_type_filters,
                    "resource_scopes": resource_scopes,
                    "status": status,
                    "url": url,
                },
                endpoint_update_params.EndpointUpdateParams,
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
        status: Literal["active", "disabled", "auto_disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Returns the organization's webhook endpoints, newest first.

        Signing secrets are
        never included.

        Args:
          status: Filter by endpoint status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/webhooks/v1/endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "status": status,
                    },
                    endpoint_list_params.EndpointListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def delete(
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
        """Soft-deletes a webhook endpoint.

        Delivery stops immediately and the endpoint no
        longer appears in list results. Delivery history is preserved (and can be
        fetched via GET /deliveries with the endpoint_id filter) so audit trails and
        post-mortem debugging remain possible.

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
            path_template("/webhooks/v1/endpoints/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def rotate_secret(
        self,
        id: str,
        *,
        previous_secret_expires_in_sec: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Generates a new signing secret for the endpoint.

        The previous secret remains
        valid until `previousSecretExpiresInSec` elapses (default 24h, max 30 days).
        During the grace window deliveries are signed with both secrets so receivers can
        migrate without downtime. Returns the new secret — this is the only time it is
        shown in plaintext.

        Args:
          previous_secret_expires_in_sec: How long (seconds) the old secret continues to be accepted. 0 invalidates
              immediately. Default: 86400 (24h).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/webhooks/v1/endpoints/{id}/rotate_secret", id=id),
            body=maybe_transform(
                {"previous_secret_expires_in_sec": previous_secret_expires_in_sec},
                endpoint_rotate_secret_params.EndpointRotateSecretParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def test(
        self,
        id: str,
        *,
        event_type: str | Omit = omit,
        payload: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Synchronously delivers a synthetic `webhook.test` event to the endpoint and
        returns the HTTP result. No retries. Useful for validating that a new endpoint
        is reachable and its signature verifier works. The delivery is not persisted in
        the delivery history.

        Args:
          event_type: Event type to simulate. Defaults to "webhook.test".

          payload: Custom `data` payload. Defaults to a small placeholder.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/webhooks/v1/endpoints/{id}/test", id=id),
            body=maybe_transform(
                {
                    "event_type": event_type,
                    "payload": payload,
                },
                endpoint_test_params.EndpointTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEndpointsResource(AsyncAPIResource):
    """Webhook endpoint management"""

    @cached_property
    def with_raw_response(self) -> AsyncEndpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEndpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEndpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncEndpointsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        event_type_filters: SequenceNotStr[str],
        url: str,
        description: str | Omit = omit,
        resource_scopes: endpoint_create_params.ResourceScopes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Creates a webhook endpoint that receives platform events matching the supplied
        event-type filters. Returns the generated signing secret ONCE — the response is
        the only time it is shown in plaintext.

        Args:
          event_type_filters: Glob patterns of event types to deliver (e.g. "vault._", "ocr.job.completed",
              "_")

          url: HTTPS callback URL that will receive event deliveries

          description: Human-readable label for this endpoint

          resource_scopes: Optional per-resource allowlists. If vaultIds is set, only events for those
              vaults are delivered. Same for matterIds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/webhooks/v1/endpoints",
            body=await async_maybe_transform(
                {
                    "event_type_filters": event_type_filters,
                    "url": url,
                    "description": description,
                    "resource_scopes": resource_scopes,
                },
                endpoint_create_params.EndpointCreateParams,
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
        Get webhook endpoint

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
            path_template("/webhooks/v1/endpoints/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        event_type_filters: SequenceNotStr[str] | Omit = omit,
        resource_scopes: Optional[endpoint_update_params.ResourceScopes] | Omit = omit,
        status: Literal["active", "disabled"] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Partially updates a webhook endpoint.

        Any omitted field is left unchanged.
        Signing secrets are rotated via the separate /rotate_secret endpoint.

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
            path_template("/webhooks/v1/endpoints/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "event_type_filters": event_type_filters,
                    "resource_scopes": resource_scopes,
                    "status": status,
                    "url": url,
                },
                endpoint_update_params.EndpointUpdateParams,
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
        status: Literal["active", "disabled", "auto_disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Returns the organization's webhook endpoints, newest first.

        Signing secrets are
        never included.

        Args:
          status: Filter by endpoint status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/webhooks/v1/endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "status": status,
                    },
                    endpoint_list_params.EndpointListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def delete(
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
        """Soft-deletes a webhook endpoint.

        Delivery stops immediately and the endpoint no
        longer appears in list results. Delivery history is preserved (and can be
        fetched via GET /deliveries with the endpoint_id filter) so audit trails and
        post-mortem debugging remain possible.

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
            path_template("/webhooks/v1/endpoints/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def rotate_secret(
        self,
        id: str,
        *,
        previous_secret_expires_in_sec: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Generates a new signing secret for the endpoint.

        The previous secret remains
        valid until `previousSecretExpiresInSec` elapses (default 24h, max 30 days).
        During the grace window deliveries are signed with both secrets so receivers can
        migrate without downtime. Returns the new secret — this is the only time it is
        shown in plaintext.

        Args:
          previous_secret_expires_in_sec: How long (seconds) the old secret continues to be accepted. 0 invalidates
              immediately. Default: 86400 (24h).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/webhooks/v1/endpoints/{id}/rotate_secret", id=id),
            body=await async_maybe_transform(
                {"previous_secret_expires_in_sec": previous_secret_expires_in_sec},
                endpoint_rotate_secret_params.EndpointRotateSecretParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def test(
        self,
        id: str,
        *,
        event_type: str | Omit = omit,
        payload: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Synchronously delivers a synthetic `webhook.test` event to the endpoint and
        returns the HTTP result. No retries. Useful for validating that a new endpoint
        is reachable and its signature verifier works. The delivery is not persisted in
        the delivery history.

        Args:
          event_type: Event type to simulate. Defaults to "webhook.test".

          payload: Custom `data` payload. Defaults to a small placeholder.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/webhooks/v1/endpoints/{id}/test", id=id),
            body=await async_maybe_transform(
                {
                    "event_type": event_type,
                    "payload": payload,
                },
                endpoint_test_params.EndpointTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EndpointsResourceWithRawResponse:
    def __init__(self, endpoints: EndpointsResource) -> None:
        self._endpoints = endpoints

        self.create = to_raw_response_wrapper(
            endpoints.create,
        )
        self.retrieve = to_raw_response_wrapper(
            endpoints.retrieve,
        )
        self.update = to_raw_response_wrapper(
            endpoints.update,
        )
        self.list = to_raw_response_wrapper(
            endpoints.list,
        )
        self.delete = to_raw_response_wrapper(
            endpoints.delete,
        )
        self.rotate_secret = to_raw_response_wrapper(
            endpoints.rotate_secret,
        )
        self.test = to_raw_response_wrapper(
            endpoints.test,
        )


class AsyncEndpointsResourceWithRawResponse:
    def __init__(self, endpoints: AsyncEndpointsResource) -> None:
        self._endpoints = endpoints

        self.create = async_to_raw_response_wrapper(
            endpoints.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            endpoints.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            endpoints.update,
        )
        self.list = async_to_raw_response_wrapper(
            endpoints.list,
        )
        self.delete = async_to_raw_response_wrapper(
            endpoints.delete,
        )
        self.rotate_secret = async_to_raw_response_wrapper(
            endpoints.rotate_secret,
        )
        self.test = async_to_raw_response_wrapper(
            endpoints.test,
        )


class EndpointsResourceWithStreamingResponse:
    def __init__(self, endpoints: EndpointsResource) -> None:
        self._endpoints = endpoints

        self.create = to_streamed_response_wrapper(
            endpoints.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            endpoints.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            endpoints.update,
        )
        self.list = to_streamed_response_wrapper(
            endpoints.list,
        )
        self.delete = to_streamed_response_wrapper(
            endpoints.delete,
        )
        self.rotate_secret = to_streamed_response_wrapper(
            endpoints.rotate_secret,
        )
        self.test = to_streamed_response_wrapper(
            endpoints.test,
        )


class AsyncEndpointsResourceWithStreamingResponse:
    def __init__(self, endpoints: AsyncEndpointsResource) -> None:
        self._endpoints = endpoints

        self.create = async_to_streamed_response_wrapper(
            endpoints.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            endpoints.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            endpoints.update,
        )
        self.list = async_to_streamed_response_wrapper(
            endpoints.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            endpoints.delete,
        )
        self.rotate_secret = async_to_streamed_response_wrapper(
            endpoints.rotate_secret,
        )
        self.test = async_to_streamed_response_wrapper(
            endpoints.test,
        )
