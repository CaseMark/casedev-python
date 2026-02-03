# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.compute.v1 import instance_create_params
from ....types.compute.v1.instance_list_response import InstanceListResponse
from ....types.compute.v1.instance_create_response import InstanceCreateResponse
from ....types.compute.v1.instance_delete_response import InstanceDeleteResponse
from ....types.compute.v1.instance_retrieve_response import InstanceRetrieveResponse

__all__ = ["InstancesResource", "AsyncInstancesResource"]


class InstancesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return InstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return InstancesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        instance_type: str,
        name: str,
        region: str,
        auto_shutdown_minutes: Optional[int] | Omit = omit,
        vault_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceCreateResponse:
        """Launches a new GPU compute instance with automatic SSH key generation.

        Supports
        mounting Case.dev Vaults as filesystems and configurable auto-shutdown. Instance
        boots in ~2-5 minutes. Perfect for batch OCR processing, AI model training, and
        intensive document analysis workloads.

        Args:
          instance_type: GPU type (e.g., 'gpu_1x_h100_sxm5')

          name: Instance name

          region: Region (e.g., 'us-west-1')

          auto_shutdown_minutes: Auto-shutdown timer (null = never)

          vault_ids: Vault IDs to mount

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/compute/v1/instances",
            body=maybe_transform(
                {
                    "instance_type": instance_type,
                    "name": name,
                    "region": region,
                    "auto_shutdown_minutes": auto_shutdown_minutes,
                    "vault_ids": vault_ids,
                },
                instance_create_params.InstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceCreateResponse,
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
    ) -> InstanceRetrieveResponse:
        """
        Retrieves detailed information about a GPU instance including SSH connection
        details, vault mount scripts, real-time cost tracking, and current status. SSH
        private key included for secure access.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/compute/v1/instances/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceListResponse:
        """
        Retrieves all GPU compute instances for your organization with real-time status
        updates from Lambda Labs. Includes pricing, runtime metrics, and auto-shutdown
        configuration. Perfect for monitoring AI workloads, document processing jobs,
        and cost tracking.
        """
        return self._get(
            "/compute/v1/instances",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceListResponse,
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
    ) -> InstanceDeleteResponse:
        """Terminates a running GPU instance, calculates final cost, and cleans up SSH
        keys.

        This action is permanent and cannot be undone. All data on the instance
        will be lost.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/compute/v1/instances/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceDeleteResponse,
        )


class AsyncInstancesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncInstancesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        instance_type: str,
        name: str,
        region: str,
        auto_shutdown_minutes: Optional[int] | Omit = omit,
        vault_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceCreateResponse:
        """Launches a new GPU compute instance with automatic SSH key generation.

        Supports
        mounting Case.dev Vaults as filesystems and configurable auto-shutdown. Instance
        boots in ~2-5 minutes. Perfect for batch OCR processing, AI model training, and
        intensive document analysis workloads.

        Args:
          instance_type: GPU type (e.g., 'gpu_1x_h100_sxm5')

          name: Instance name

          region: Region (e.g., 'us-west-1')

          auto_shutdown_minutes: Auto-shutdown timer (null = never)

          vault_ids: Vault IDs to mount

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/compute/v1/instances",
            body=await async_maybe_transform(
                {
                    "instance_type": instance_type,
                    "name": name,
                    "region": region,
                    "auto_shutdown_minutes": auto_shutdown_minutes,
                    "vault_ids": vault_ids,
                },
                instance_create_params.InstanceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceCreateResponse,
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
    ) -> InstanceRetrieveResponse:
        """
        Retrieves detailed information about a GPU instance including SSH connection
        details, vault mount scripts, real-time cost tracking, and current status. SSH
        private key included for secure access.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/compute/v1/instances/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceListResponse:
        """
        Retrieves all GPU compute instances for your organization with real-time status
        updates from Lambda Labs. Includes pricing, runtime metrics, and auto-shutdown
        configuration. Perfect for monitoring AI workloads, document processing jobs,
        and cost tracking.
        """
        return await self._get(
            "/compute/v1/instances",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceListResponse,
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
    ) -> InstanceDeleteResponse:
        """Terminates a running GPU instance, calculates final cost, and cleans up SSH
        keys.

        This action is permanent and cannot be undone. All data on the instance
        will be lost.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/compute/v1/instances/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceDeleteResponse,
        )


class InstancesResourceWithRawResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.create = to_raw_response_wrapper(
            instances.create,
        )
        self.retrieve = to_raw_response_wrapper(
            instances.retrieve,
        )
        self.list = to_raw_response_wrapper(
            instances.list,
        )
        self.delete = to_raw_response_wrapper(
            instances.delete,
        )


class AsyncInstancesResourceWithRawResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.create = async_to_raw_response_wrapper(
            instances.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            instances.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            instances.list,
        )
        self.delete = async_to_raw_response_wrapper(
            instances.delete,
        )


class InstancesResourceWithStreamingResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.create = to_streamed_response_wrapper(
            instances.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            instances.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            instances.list,
        )
        self.delete = to_streamed_response_wrapper(
            instances.delete,
        )


class AsyncInstancesResourceWithStreamingResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.create = async_to_streamed_response_wrapper(
            instances.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            instances.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            instances.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            instances.delete,
        )
