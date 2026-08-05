# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
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
from ....types.linc.v1 import (
    session_cancel_params,
    session_create_params,
    session_send_rpc_params,
    session_ingest_events_params,
    session_retrieve_events_params,
    session_retrieve_messages_params,
)

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    """Durable, stateful legal agent sessions with sandboxed tools and files"""

    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        document_template_slugs: Optional[SequenceNotStr[str]] | Omit = omit,
        idle_timeout_ms: Optional[int] | Omit = omit,
        include_document_templates: Optional[bool] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        model: Optional[str] | Omit = omit,
        scoped_api_key: Optional[str] | Omit = omit,
        service_tier: Literal["default", "priority"] | Omit = omit,
        skill_slugs: Optional[SequenceNotStr[str]] | Omit = omit,
        title: str | Omit = omit,
        vault_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Creates a Daytona-backed native Linc session with scoped Case.dev credentials.
        This endpoint starts the sandbox actor only; messages and event replay use
        separate endpoints.

        Args:
          document_template_slugs: Specific document template slugs to inject into the using-document-templates
              skill.

          include_document_templates: When true, inject all active org document templates into the
              using-document-templates skill.

          instructions: Privileged C3-only hidden app instructions to append to the sandbox AGENTS.md.

          scoped_api_key: Optional caller-provided scoped Case.dev API key for the runtime.

          service_tier: Processing tier for eligible OpenAI GPT models. Priority provides lower latency
              at premium cost.

          skill_slugs: Skills API slugs to install into the runtime sandbox before the native session
              starts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/linc/v1/sessions",
            body=maybe_transform(
                {
                    "document_template_slugs": document_template_slugs,
                    "idle_timeout_ms": idle_timeout_ms,
                    "include_document_templates": include_document_templates,
                    "instructions": instructions,
                    "model": model,
                    "scoped_api_key": scoped_api_key,
                    "service_tier": service_tier,
                    "skill_slugs": skill_slugs,
                    "title": title,
                    "vault_ids": vault_ids,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        """
        End native Linc session

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
            path_template("/linc/v1/sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def cancel(
        self,
        id: str,
        *,
        clear_queue: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Sends an abort RPC to the session runtime, ending the current turn while keeping
        the session alive. Body handling is intentionally lenient — cancel is a stop
        control, so unknown fields are ignored and an invalid or missing body is treated
        as empty rather than rejected.

        Args:
          clear_queue: Also clear queued steering/follow-up messages so the abort leaves the agent
              fully idle. Cleared texts are returned in the `response.data.clearedQueue` field
              of the response body. Without it, messages still queued when the abort settles
              are auto-continued as a new run. Runtimes older than the Linc release that
              supports this flag ignore it: the abort still happens but the queue is left
              untouched.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/linc/v1/sessions/{id}/cancel", id=id),
            body=maybe_transform({"clear_queue": clear_queue}, session_cancel_params.SessionCancelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def ingest_events(
        self,
        id: str,
        *,
        frames: Iterable[session_ingest_events_params.Frame],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Runtime ingest endpoint for sandbox runtimes.

        Frames are persisted for replay;
        terminal frames emit the durable Linc session ended webhook.

        Args:
          frames: Native Linc event frames to persist for replay.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/linc/v1/sessions/{id}/events/ingest", id=id),
            body=maybe_transform({"frames": frames}, session_ingest_events_params.SessionIngestEventsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_events(
        self,
        id: str,
        *,
        after_seq: int | Omit = omit,
        cursor: int | Omit = omit,
        exclude_event_types: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns persisted native Pi/Linc event envelopes after the requested cursor.
        Live delivery is handled by the Linc stream service.

        Args:
          after_seq: Alias for cursor. Ignored when cursor is also provided.

          cursor: Replay events with a sequence number greater than this cursor.

          exclude_event_types: Comma-separated Linc event types to omit from replay.

          limit: Maximum number of events to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/linc/v1/sessions/{id}/events", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_seq": after_seq,
                        "cursor": cursor,
                        "exclude_event_types": exclude_event_types,
                        "limit": limit,
                    },
                    session_retrieve_events_params.SessionRetrieveEventsParams,
                ),
            ),
            cast_to=NoneType,
        )

    def retrieve_messages(
        self,
        id: str,
        *,
        after_seq: int | Omit = omit,
        cursor: int | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns completed Pi/Linc message entries derived from durable native Linc
        events. This is the stable session-message read model for callers that need to
        persist or recover chat history without depending on a live SSE stream.

        Args:
          after_seq: Alias for cursor. Ignored when cursor is also provided.

          cursor: Replay messages with a source event sequence number greater than this cursor.

          limit: Maximum number of source events to scan for completed messages.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/linc/v1/sessions/{id}/messages", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_seq": after_seq,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    session_retrieve_messages_params.SessionRetrieveMessagesParams,
                ),
            ),
            cast_to=NoneType,
        )

    def retrieve_state(
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
        Get native Linc session state

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
            path_template("/linc/v1/sessions/{id}/state", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send_rpc(
        self,
        path_id: str,
        *,
        type: str,
        body_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Forwards a native Pi/Linc RPC command object to the sandbox-local Linc bridge
        unchanged. The route returns after Pi accepts or rejects the command; native
        events are read through the events endpoint.

        Args:
          type: Native Pi/Linc RPC command type. Prompt commands also require a string id for
              idempotency.

          body_id: Command idempotency key. Required when type is prompt.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/linc/v1/sessions/{path_id}/rpc", path_id=path_id),
            body=maybe_transform(
                {
                    "type": type,
                    "body_id": body_id,
                },
                session_send_rpc_params.SessionSendRpcParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSessionsResource(AsyncAPIResource):
    """Durable, stateful legal agent sessions with sandboxed tools and files"""

    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        document_template_slugs: Optional[SequenceNotStr[str]] | Omit = omit,
        idle_timeout_ms: Optional[int] | Omit = omit,
        include_document_templates: Optional[bool] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        model: Optional[str] | Omit = omit,
        scoped_api_key: Optional[str] | Omit = omit,
        service_tier: Literal["default", "priority"] | Omit = omit,
        skill_slugs: Optional[SequenceNotStr[str]] | Omit = omit,
        title: str | Omit = omit,
        vault_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Creates a Daytona-backed native Linc session with scoped Case.dev credentials.
        This endpoint starts the sandbox actor only; messages and event replay use
        separate endpoints.

        Args:
          document_template_slugs: Specific document template slugs to inject into the using-document-templates
              skill.

          include_document_templates: When true, inject all active org document templates into the
              using-document-templates skill.

          instructions: Privileged C3-only hidden app instructions to append to the sandbox AGENTS.md.

          scoped_api_key: Optional caller-provided scoped Case.dev API key for the runtime.

          service_tier: Processing tier for eligible OpenAI GPT models. Priority provides lower latency
              at premium cost.

          skill_slugs: Skills API slugs to install into the runtime sandbox before the native session
              starts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/linc/v1/sessions",
            body=await async_maybe_transform(
                {
                    "document_template_slugs": document_template_slugs,
                    "idle_timeout_ms": idle_timeout_ms,
                    "include_document_templates": include_document_templates,
                    "instructions": instructions,
                    "model": model,
                    "scoped_api_key": scoped_api_key,
                    "service_tier": service_tier,
                    "skill_slugs": skill_slugs,
                    "title": title,
                    "vault_ids": vault_ids,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        """
        End native Linc session

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
            path_template("/linc/v1/sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def cancel(
        self,
        id: str,
        *,
        clear_queue: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Sends an abort RPC to the session runtime, ending the current turn while keeping
        the session alive. Body handling is intentionally lenient — cancel is a stop
        control, so unknown fields are ignored and an invalid or missing body is treated
        as empty rather than rejected.

        Args:
          clear_queue: Also clear queued steering/follow-up messages so the abort leaves the agent
              fully idle. Cleared texts are returned in the `response.data.clearedQueue` field
              of the response body. Without it, messages still queued when the abort settles
              are auto-continued as a new run. Runtimes older than the Linc release that
              supports this flag ignore it: the abort still happens but the queue is left
              untouched.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/linc/v1/sessions/{id}/cancel", id=id),
            body=await async_maybe_transform({"clear_queue": clear_queue}, session_cancel_params.SessionCancelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def ingest_events(
        self,
        id: str,
        *,
        frames: Iterable[session_ingest_events_params.Frame],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Runtime ingest endpoint for sandbox runtimes.

        Frames are persisted for replay;
        terminal frames emit the durable Linc session ended webhook.

        Args:
          frames: Native Linc event frames to persist for replay.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/linc/v1/sessions/{id}/events/ingest", id=id),
            body=await async_maybe_transform(
                {"frames": frames}, session_ingest_events_params.SessionIngestEventsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_events(
        self,
        id: str,
        *,
        after_seq: int | Omit = omit,
        cursor: int | Omit = omit,
        exclude_event_types: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns persisted native Pi/Linc event envelopes after the requested cursor.
        Live delivery is handled by the Linc stream service.

        Args:
          after_seq: Alias for cursor. Ignored when cursor is also provided.

          cursor: Replay events with a sequence number greater than this cursor.

          exclude_event_types: Comma-separated Linc event types to omit from replay.

          limit: Maximum number of events to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/linc/v1/sessions/{id}/events", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after_seq": after_seq,
                        "cursor": cursor,
                        "exclude_event_types": exclude_event_types,
                        "limit": limit,
                    },
                    session_retrieve_events_params.SessionRetrieveEventsParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def retrieve_messages(
        self,
        id: str,
        *,
        after_seq: int | Omit = omit,
        cursor: int | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns completed Pi/Linc message entries derived from durable native Linc
        events. This is the stable session-message read model for callers that need to
        persist or recover chat history without depending on a live SSE stream.

        Args:
          after_seq: Alias for cursor. Ignored when cursor is also provided.

          cursor: Replay messages with a source event sequence number greater than this cursor.

          limit: Maximum number of source events to scan for completed messages.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/linc/v1/sessions/{id}/messages", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after_seq": after_seq,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    session_retrieve_messages_params.SessionRetrieveMessagesParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def retrieve_state(
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
        Get native Linc session state

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
            path_template("/linc/v1/sessions/{id}/state", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send_rpc(
        self,
        path_id: str,
        *,
        type: str,
        body_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Forwards a native Pi/Linc RPC command object to the sandbox-local Linc bridge
        unchanged. The route returns after Pi accepts or rejects the command; native
        events are read through the events endpoint.

        Args:
          type: Native Pi/Linc RPC command type. Prompt commands also require a string id for
              idempotency.

          body_id: Command idempotency key. Required when type is prompt.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/linc/v1/sessions/{path_id}/rpc", path_id=path_id),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "body_id": body_id,
                },
                session_send_rpc_params.SessionSendRpcParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_raw_response_wrapper(
            sessions.create,
        )
        self.delete = to_raw_response_wrapper(
            sessions.delete,
        )
        self.cancel = to_raw_response_wrapper(
            sessions.cancel,
        )
        self.ingest_events = to_raw_response_wrapper(
            sessions.ingest_events,
        )
        self.retrieve_events = to_raw_response_wrapper(
            sessions.retrieve_events,
        )
        self.retrieve_messages = to_raw_response_wrapper(
            sessions.retrieve_messages,
        )
        self.retrieve_state = to_raw_response_wrapper(
            sessions.retrieve_state,
        )
        self.send_rpc = to_raw_response_wrapper(
            sessions.send_rpc,
        )


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_raw_response_wrapper(
            sessions.create,
        )
        self.delete = async_to_raw_response_wrapper(
            sessions.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            sessions.cancel,
        )
        self.ingest_events = async_to_raw_response_wrapper(
            sessions.ingest_events,
        )
        self.retrieve_events = async_to_raw_response_wrapper(
            sessions.retrieve_events,
        )
        self.retrieve_messages = async_to_raw_response_wrapper(
            sessions.retrieve_messages,
        )
        self.retrieve_state = async_to_raw_response_wrapper(
            sessions.retrieve_state,
        )
        self.send_rpc = async_to_raw_response_wrapper(
            sessions.send_rpc,
        )


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_streamed_response_wrapper(
            sessions.create,
        )
        self.delete = to_streamed_response_wrapper(
            sessions.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            sessions.cancel,
        )
        self.ingest_events = to_streamed_response_wrapper(
            sessions.ingest_events,
        )
        self.retrieve_events = to_streamed_response_wrapper(
            sessions.retrieve_events,
        )
        self.retrieve_messages = to_streamed_response_wrapper(
            sessions.retrieve_messages,
        )
        self.retrieve_state = to_streamed_response_wrapper(
            sessions.retrieve_state,
        )
        self.send_rpc = to_streamed_response_wrapper(
            sessions.send_rpc,
        )


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_streamed_response_wrapper(
            sessions.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            sessions.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            sessions.cancel,
        )
        self.ingest_events = async_to_streamed_response_wrapper(
            sessions.ingest_events,
        )
        self.retrieve_events = async_to_streamed_response_wrapper(
            sessions.retrieve_events,
        )
        self.retrieve_messages = async_to_streamed_response_wrapper(
            sessions.retrieve_messages,
        )
        self.retrieve_state = async_to_streamed_response_wrapper(
            sessions.retrieve_state,
        )
        self.send_rpc = async_to_streamed_response_wrapper(
            sessions.send_rpc,
        )
