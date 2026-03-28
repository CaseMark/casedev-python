# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.matters.v1 import agent_type_list_params, agent_type_create_params

__all__ = ["AgentTypesResource", "AsyncAgentTypesResource"]


class AgentTypesResource(SyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> AgentTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AgentTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AgentTypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        instructions: str,
        name: str,
        description: str | Omit = omit,
        disabled_tools: SequenceNotStr[str] | Omit = omit,
        enabled_tools: SequenceNotStr[str] | Omit = omit,
        is_active: bool | Omit = omit,
        is_default: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        model: str | Omit = omit,
        skill_refs: SequenceNotStr[str] | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a reusable agent role for legal matter orchestration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/matters/v1/agent-types",
            body=maybe_transform(
                {
                    "instructions": instructions,
                    "name": name,
                    "description": description,
                    "disabled_tools": disabled_tools,
                    "enabled_tools": enabled_tools,
                    "is_active": is_active,
                    "is_default": is_default,
                    "metadata": metadata,
                    "model": model,
                    "skill_refs": skill_refs,
                    "slug": slug,
                },
                agent_type_create_params.AgentTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List reusable agent roles for the authenticated organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/matters/v1/agent-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"active": active}, agent_type_list_params.AgentTypeListParams),
            ),
            cast_to=NoneType,
        )


class AsyncAgentTypesResource(AsyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> AsyncAgentTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncAgentTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        instructions: str,
        name: str,
        description: str | Omit = omit,
        disabled_tools: SequenceNotStr[str] | Omit = omit,
        enabled_tools: SequenceNotStr[str] | Omit = omit,
        is_active: bool | Omit = omit,
        is_default: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        model: str | Omit = omit,
        skill_refs: SequenceNotStr[str] | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a reusable agent role for legal matter orchestration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/matters/v1/agent-types",
            body=await async_maybe_transform(
                {
                    "instructions": instructions,
                    "name": name,
                    "description": description,
                    "disabled_tools": disabled_tools,
                    "enabled_tools": enabled_tools,
                    "is_active": is_active,
                    "is_default": is_default,
                    "metadata": metadata,
                    "model": model,
                    "skill_refs": skill_refs,
                    "slug": slug,
                },
                agent_type_create_params.AgentTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List reusable agent roles for the authenticated organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/matters/v1/agent-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"active": active}, agent_type_list_params.AgentTypeListParams),
            ),
            cast_to=NoneType,
        )


class AgentTypesResourceWithRawResponse:
    def __init__(self, agent_types: AgentTypesResource) -> None:
        self._agent_types = agent_types

        self.create = to_raw_response_wrapper(
            agent_types.create,
        )
        self.list = to_raw_response_wrapper(
            agent_types.list,
        )


class AsyncAgentTypesResourceWithRawResponse:
    def __init__(self, agent_types: AsyncAgentTypesResource) -> None:
        self._agent_types = agent_types

        self.create = async_to_raw_response_wrapper(
            agent_types.create,
        )
        self.list = async_to_raw_response_wrapper(
            agent_types.list,
        )


class AgentTypesResourceWithStreamingResponse:
    def __init__(self, agent_types: AgentTypesResource) -> None:
        self._agent_types = agent_types

        self.create = to_streamed_response_wrapper(
            agent_types.create,
        )
        self.list = to_streamed_response_wrapper(
            agent_types.list,
        )


class AsyncAgentTypesResourceWithStreamingResponse:
    def __init__(self, agent_types: AsyncAgentTypesResource) -> None:
        self._agent_types = agent_types

        self.create = async_to_streamed_response_wrapper(
            agent_types.create,
        )
        self.list = async_to_streamed_response_wrapper(
            agent_types.list,
        )
