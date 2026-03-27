# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._streaming import Stream, AsyncStream
from ...._base_client import make_request_options
from ....types.agent.v2 import run_create_params, run_events_params
from ....types.agent.v2.run_exec_response import RunExecResponse
from ....types.agent.v2.run_create_response import RunCreateResponse
from ....types.agent.v2.run_events_response import RunEventsResponse
from ....types.agent.v2.run_get_status_response import RunGetStatusResponse

__all__ = ["RunResource", "AsyncRunResource"]


class RunResource(SyncAPIResource):
    """
    Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
    """

    @cached_property
    def with_raw_response(self) -> RunResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return RunResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return RunResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_id: str,
        prompt: str,
        callback_url: Optional[str] | Omit = omit,
        guidance: Optional[str] | Omit = omit,
        model: Optional[str] | Omit = omit,
        object_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCreateResponse:
        """Creates a v2 run in queued state.

        Call POST /agent/v2/run/:id/exec to start
        execution on the Daytona runtime.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agent/v2/run",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "prompt": prompt,
                    "callback_url": callback_url,
                    "guidance": guidance,
                    "model": model,
                    "object_ids": object_ids,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCreateResponse,
        )

    def events(
        self,
        id: str,
        *,
        last_event_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[RunEventsResponse]:
        """
        Streams real-time v2 run events over SSE with replay support.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            path_template("/agent/v2/run/{id}/events", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"last_event_id": last_event_id}, run_events_params.RunEventsParams),
            ),
            cast_to=str,
            stream=True,
            stream_cls=Stream[RunEventsResponse],
        )

    def exec(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunExecResponse:
        """Starts execution of a queued v2 run.

        The agent runs in a durable workflow on a
        Daytona runtime.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/agent/v2/run/{id}/exec", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunExecResponse,
        )

    def get_details(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Full audit trail for a v2 run, with provider-neutral runtime metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/agent/v2/run/{id}/details", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunGetStatusResponse:
        """
        Lightweight status poll for a v2 run including neutral runtime metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/agent/v2/run/{id}/status", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunGetStatusResponse,
        )


class AsyncRunResource(AsyncAPIResource):
    """
    Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
    """

    @cached_property
    def with_raw_response(self) -> AsyncRunResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncRunResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_id: str,
        prompt: str,
        callback_url: Optional[str] | Omit = omit,
        guidance: Optional[str] | Omit = omit,
        model: Optional[str] | Omit = omit,
        object_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCreateResponse:
        """Creates a v2 run in queued state.

        Call POST /agent/v2/run/:id/exec to start
        execution on the Daytona runtime.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agent/v2/run",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "prompt": prompt,
                    "callback_url": callback_url,
                    "guidance": guidance,
                    "model": model,
                    "object_ids": object_ids,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCreateResponse,
        )

    async def events(
        self,
        id: str,
        *,
        last_event_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[RunEventsResponse]:
        """
        Streams real-time v2 run events over SSE with replay support.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/agent/v2/run/{id}/events", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"last_event_id": last_event_id}, run_events_params.RunEventsParams),
            ),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[RunEventsResponse],
        )

    async def exec(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunExecResponse:
        """Starts execution of a queued v2 run.

        The agent runs in a durable workflow on a
        Daytona runtime.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/agent/v2/run/{id}/exec", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunExecResponse,
        )

    async def get_details(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Full audit trail for a v2 run, with provider-neutral runtime metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/agent/v2/run/{id}/details", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunGetStatusResponse:
        """
        Lightweight status poll for a v2 run including neutral runtime metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/agent/v2/run/{id}/status", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunGetStatusResponse,
        )


class RunResourceWithRawResponse:
    def __init__(self, run: RunResource) -> None:
        self._run = run

        self.create = to_raw_response_wrapper(
            run.create,
        )
        self.events = to_raw_response_wrapper(
            run.events,
        )
        self.exec = to_raw_response_wrapper(
            run.exec,
        )
        self.get_details = to_raw_response_wrapper(
            run.get_details,
        )
        self.get_status = to_raw_response_wrapper(
            run.get_status,
        )


class AsyncRunResourceWithRawResponse:
    def __init__(self, run: AsyncRunResource) -> None:
        self._run = run

        self.create = async_to_raw_response_wrapper(
            run.create,
        )
        self.events = async_to_raw_response_wrapper(
            run.events,
        )
        self.exec = async_to_raw_response_wrapper(
            run.exec,
        )
        self.get_details = async_to_raw_response_wrapper(
            run.get_details,
        )
        self.get_status = async_to_raw_response_wrapper(
            run.get_status,
        )


class RunResourceWithStreamingResponse:
    def __init__(self, run: RunResource) -> None:
        self._run = run

        self.create = to_streamed_response_wrapper(
            run.create,
        )
        self.events = to_streamed_response_wrapper(
            run.events,
        )
        self.exec = to_streamed_response_wrapper(
            run.exec,
        )
        self.get_details = to_streamed_response_wrapper(
            run.get_details,
        )
        self.get_status = to_streamed_response_wrapper(
            run.get_status,
        )


class AsyncRunResourceWithStreamingResponse:
    def __init__(self, run: AsyncRunResource) -> None:
        self._run = run

        self.create = async_to_streamed_response_wrapper(
            run.create,
        )
        self.events = async_to_streamed_response_wrapper(
            run.events,
        )
        self.exec = async_to_streamed_response_wrapper(
            run.exec,
        )
        self.get_details = async_to_streamed_response_wrapper(
            run.get_details,
        )
        self.get_status = async_to_streamed_response_wrapper(
            run.get_status,
        )
