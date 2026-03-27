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
from ....types.agent.v2 import execute_create_params
from ....types.agent.v2.execute_create_response import ExecuteCreateResponse

__all__ = ["ExecuteResource", "AsyncExecuteResource"]


class ExecuteResource(SyncAPIResource):
    """
    Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
    """

    @cached_property
    def with_raw_response(self) -> ExecuteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return ExecuteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecuteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return ExecuteResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        prompt: str,
        disabled_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        enabled_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        guidance: Optional[str] | Omit = omit,
        instructions: str | Omit = omit,
        model: str | Omit = omit,
        object_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        sandbox: Optional[execute_create_params.Sandbox] | Omit = omit,
        vault_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecuteCreateResponse:
        """
        Creates an ephemeral agent and immediately executes a v2 run on the Daytona
        runtime.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agent/v2/execute",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "disabled_tools": disabled_tools,
                    "enabled_tools": enabled_tools,
                    "guidance": guidance,
                    "instructions": instructions,
                    "model": model,
                    "object_ids": object_ids,
                    "sandbox": sandbox,
                    "vault_ids": vault_ids,
                },
                execute_create_params.ExecuteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecuteCreateResponse,
        )


class AsyncExecuteResource(AsyncAPIResource):
    """
    Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
    """

    @cached_property
    def with_raw_response(self) -> AsyncExecuteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExecuteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecuteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncExecuteResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        prompt: str,
        disabled_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        enabled_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        guidance: Optional[str] | Omit = omit,
        instructions: str | Omit = omit,
        model: str | Omit = omit,
        object_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        sandbox: Optional[execute_create_params.Sandbox] | Omit = omit,
        vault_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecuteCreateResponse:
        """
        Creates an ephemeral agent and immediately executes a v2 run on the Daytona
        runtime.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agent/v2/execute",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "disabled_tools": disabled_tools,
                    "enabled_tools": enabled_tools,
                    "guidance": guidance,
                    "instructions": instructions,
                    "model": model,
                    "object_ids": object_ids,
                    "sandbox": sandbox,
                    "vault_ids": vault_ids,
                },
                execute_create_params.ExecuteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecuteCreateResponse,
        )


class ExecuteResourceWithRawResponse:
    def __init__(self, execute: ExecuteResource) -> None:
        self._execute = execute

        self.create = to_raw_response_wrapper(
            execute.create,
        )


class AsyncExecuteResourceWithRawResponse:
    def __init__(self, execute: AsyncExecuteResource) -> None:
        self._execute = execute

        self.create = async_to_raw_response_wrapper(
            execute.create,
        )


class ExecuteResourceWithStreamingResponse:
    def __init__(self, execute: ExecuteResource) -> None:
        self._execute = execute

        self.create = to_streamed_response_wrapper(
            execute.create,
        )


class AsyncExecuteResourceWithStreamingResponse:
    def __init__(self, execute: AsyncExecuteResource) -> None:
        self._execute = execute

        self.create = async_to_streamed_response_wrapper(
            execute.create,
        )
