# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.compute.v1.instance_type_list_response import InstanceTypeListResponse

__all__ = ["InstanceTypesResource", "AsyncInstanceTypesResource"]


class InstanceTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstanceTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return InstanceTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstanceTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return InstanceTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceTypeListResponse:
        """
        Retrieves all available GPU instance types with pricing, specifications, and
        regional availability. Includes T4, A10, A100, H100, and H200 GPUs powered by
        Lambda Labs. Perfect for AI model training, inference workloads, and legal
        document OCR processing at scale.
        """
        return self._get(
            "/compute/v1/instance-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceTypeListResponse,
        )


class AsyncInstanceTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstanceTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstanceTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstanceTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncInstanceTypesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceTypeListResponse:
        """
        Retrieves all available GPU instance types with pricing, specifications, and
        regional availability. Includes T4, A10, A100, H100, and H200 GPUs powered by
        Lambda Labs. Perfect for AI model training, inference workloads, and legal
        document OCR processing at scale.
        """
        return await self._get(
            "/compute/v1/instance-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstanceTypeListResponse,
        )


class InstanceTypesResourceWithRawResponse:
    def __init__(self, instance_types: InstanceTypesResource) -> None:
        self._instance_types = instance_types

        self.list = to_raw_response_wrapper(
            instance_types.list,
        )


class AsyncInstanceTypesResourceWithRawResponse:
    def __init__(self, instance_types: AsyncInstanceTypesResource) -> None:
        self._instance_types = instance_types

        self.list = async_to_raw_response_wrapper(
            instance_types.list,
        )


class InstanceTypesResourceWithStreamingResponse:
    def __init__(self, instance_types: InstanceTypesResource) -> None:
        self._instance_types = instance_types

        self.list = to_streamed_response_wrapper(
            instance_types.list,
        )


class AsyncInstanceTypesResourceWithStreamingResponse:
    def __init__(self, instance_types: AsyncInstanceTypesResource) -> None:
        self._instance_types = instance_types

        self.list = async_to_streamed_response_wrapper(
            instance_types.list,
        )
