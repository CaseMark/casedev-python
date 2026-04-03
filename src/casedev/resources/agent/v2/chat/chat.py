# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._streaming import Stream, AsyncStream
from ....._base_client import make_request_options
from .....types.agent.v2 import (
    chat_create_params,
    chat_stream_params,
    chat_respond_params,
    chat_send_message_params,
    chat_reply_to_question_params,
)
from .....types.agent.v2.chat_cancel_response import ChatCancelResponse
from .....types.agent.v2.chat_create_response import ChatCreateResponse
from .....types.agent.v2.chat_delete_response import ChatDeleteResponse
from .....types.agent.v2.chat_stream_response import ChatStreamResponse
from .....types.agent.v2.chat_respond_response import ChatRespondResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    """
    Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
    """

    @cached_property
    def files(self) -> FilesResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        idle_timeout_ms: Optional[int] | Omit = omit,
        model: Optional[str] | Omit = omit,
        title: str | Omit = omit,
        vault_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCreateResponse:
        """Creates a persistent OpenCode chat session backed by a Daytona runtime.

        Session
        state is retained and can be resumed or recovered across requests.

        Args:
          idle_timeout_ms: Idle timeout before the runtime is eligible to stop. Defaults to 15 minutes.

          model: Optional model override for the OpenCode session

          title: Optional human-readable session title

          vault_ids: Restrict the chat session to specific vault IDs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agent/v2/chat",
            body=maybe_transform(
                {
                    "idle_timeout_ms": idle_timeout_ms,
                    "model": model,
                    "title": title,
                    "vault_ids": vault_ids,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateResponse,
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
    ) -> ChatDeleteResponse:
        """
        Terminates the active Daytona runtime (if any), then marks the chat as ended.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/agent/v2/chat/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatDeleteResponse,
        )

    def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCancelResponse:
        """
        Aborts the active OpenCode generation for this Daytona-backed chat session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/agent/v2/chat/{id}/cancel", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCancelResponse,
        )

    def reply_to_question(
        self,
        request_id: str,
        *,
        id: str,
        answers: Iterable[SequenceNotStr[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Answers a pending OpenCode question for the Daytona-backed chat session and
        resumes or recovers the runtime if needed.

        Args:
          answers: Answer selections for each prompt element in the pending question

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/agent/v2/chat/{id}/question/{request_id}/reply", id=id, request_id=request_id),
            body=maybe_transform({"answers": answers}, chat_reply_to_question_params.ChatReplyToQuestionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def respond(
        self,
        id: str,
        *,
        model: Optional[str] | Omit = omit,
        parts: Iterable[chat_respond_params.Part] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ChatRespondResponse]:
        """
        Streams a single assistant turn from a Daytona-backed chat runtime as normalized
        SSE events with stable turn, message, and part IDs. Emits events:
        `turn.started`, `turn.status`, `message.created`, `message.part.updated`,
        `message.completed`, `session.usage`, `turn.completed`.

        **When to use this endpoint:** Recommended for building custom chat UIs that
        need real-time streaming progress. This is the primary streaming endpoint for
        new integrations.

        **Alternatives:**

        - `POST /chat/:id/message` — synchronous, returns complete response as JSON
          (best for server-to-server)

        Args:
          model: Optional model override. When provided, the runtime bootstrap config is updated
              so subsequent turns use this model. Conversation history is preserved.

          parts: Message content parts. Currently only "text" type is supported. Additional types
              (e.g. file, image) may be added in future versions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            path_template("/agent/v2/chat/{id}/respond", id=id),
            body=maybe_transform(
                {
                    "model": model,
                    "parts": parts,
                },
                chat_respond_params.ChatRespondParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=Stream[ChatRespondResponse],
        )

    def send_message(
        self,
        id: str,
        *,
        model: Optional[str] | Omit = omit,
        parts: Iterable[chat_send_message_params.Part] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Sends a message to a Daytona-backed chat runtime and returns the complete
        response as a single JSON body. Blocks until the assistant turn completes.

        **When to use this endpoint:** Best for server-to-server integrations,
        background processing, or any context where you want the full response in one
        call without managing an SSE stream.

        **Alternatives:**

        - `POST /chat/:id/respond` — streaming SSE with normalized events (recommended
          for custom chat UIs)

        Args:
          model: Optional model override. When provided, the runtime bootstrap config is updated
              so subsequent turns use this model. Conversation history is preserved.

          parts: Message content parts. Currently only "text" type is supported. Additional types
              (e.g. file, image) may be added in future versions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/agent/v2/chat/{id}/message", id=id),
            body=maybe_transform(
                {
                    "model": model,
                    "parts": parts,
                },
                chat_send_message_params.ChatSendMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def stream(
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
    ) -> Stream[ChatStreamResponse]:
        """Relays OpenCode SSE events for this Daytona-backed chat runtime.

        Supports replay
        from buffered events using Last-Event-ID and transparently reconnects stopped or
        archived runtimes.

        Args:
          last_event_id: Replay events after this sequence number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            path_template("/agent/v2/chat/{id}/stream", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"last_event_id": last_event_id}, chat_stream_params.ChatStreamParams),
            ),
            cast_to=str,
            stream=True,
            stream_cls=Stream[ChatStreamResponse],
        )


class AsyncChatResource(AsyncAPIResource):
    """
    Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
    """

    @cached_property
    def files(self) -> AsyncFilesResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        idle_timeout_ms: Optional[int] | Omit = omit,
        model: Optional[str] | Omit = omit,
        title: str | Omit = omit,
        vault_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCreateResponse:
        """Creates a persistent OpenCode chat session backed by a Daytona runtime.

        Session
        state is retained and can be resumed or recovered across requests.

        Args:
          idle_timeout_ms: Idle timeout before the runtime is eligible to stop. Defaults to 15 minutes.

          model: Optional model override for the OpenCode session

          title: Optional human-readable session title

          vault_ids: Restrict the chat session to specific vault IDs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agent/v2/chat",
            body=await async_maybe_transform(
                {
                    "idle_timeout_ms": idle_timeout_ms,
                    "model": model,
                    "title": title,
                    "vault_ids": vault_ids,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateResponse,
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
    ) -> ChatDeleteResponse:
        """
        Terminates the active Daytona runtime (if any), then marks the chat as ended.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/agent/v2/chat/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatDeleteResponse,
        )

    async def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCancelResponse:
        """
        Aborts the active OpenCode generation for this Daytona-backed chat session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/agent/v2/chat/{id}/cancel", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCancelResponse,
        )

    async def reply_to_question(
        self,
        request_id: str,
        *,
        id: str,
        answers: Iterable[SequenceNotStr[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Answers a pending OpenCode question for the Daytona-backed chat session and
        resumes or recovers the runtime if needed.

        Args:
          answers: Answer selections for each prompt element in the pending question

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/agent/v2/chat/{id}/question/{request_id}/reply", id=id, request_id=request_id),
            body=await async_maybe_transform(
                {"answers": answers}, chat_reply_to_question_params.ChatReplyToQuestionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def respond(
        self,
        id: str,
        *,
        model: Optional[str] | Omit = omit,
        parts: Iterable[chat_respond_params.Part] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ChatRespondResponse]:
        """
        Streams a single assistant turn from a Daytona-backed chat runtime as normalized
        SSE events with stable turn, message, and part IDs. Emits events:
        `turn.started`, `turn.status`, `message.created`, `message.part.updated`,
        `message.completed`, `session.usage`, `turn.completed`.

        **When to use this endpoint:** Recommended for building custom chat UIs that
        need real-time streaming progress. This is the primary streaming endpoint for
        new integrations.

        **Alternatives:**

        - `POST /chat/:id/message` — synchronous, returns complete response as JSON
          (best for server-to-server)

        Args:
          model: Optional model override. When provided, the runtime bootstrap config is updated
              so subsequent turns use this model. Conversation history is preserved.

          parts: Message content parts. Currently only "text" type is supported. Additional types
              (e.g. file, image) may be added in future versions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            path_template("/agent/v2/chat/{id}/respond", id=id),
            body=await async_maybe_transform(
                {
                    "model": model,
                    "parts": parts,
                },
                chat_respond_params.ChatRespondParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[ChatRespondResponse],
        )

    async def send_message(
        self,
        id: str,
        *,
        model: Optional[str] | Omit = omit,
        parts: Iterable[chat_send_message_params.Part] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Sends a message to a Daytona-backed chat runtime and returns the complete
        response as a single JSON body. Blocks until the assistant turn completes.

        **When to use this endpoint:** Best for server-to-server integrations,
        background processing, or any context where you want the full response in one
        call without managing an SSE stream.

        **Alternatives:**

        - `POST /chat/:id/respond` — streaming SSE with normalized events (recommended
          for custom chat UIs)

        Args:
          model: Optional model override. When provided, the runtime bootstrap config is updated
              so subsequent turns use this model. Conversation history is preserved.

          parts: Message content parts. Currently only "text" type is supported. Additional types
              (e.g. file, image) may be added in future versions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/agent/v2/chat/{id}/message", id=id),
            body=await async_maybe_transform(
                {
                    "model": model,
                    "parts": parts,
                },
                chat_send_message_params.ChatSendMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def stream(
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
    ) -> AsyncStream[ChatStreamResponse]:
        """Relays OpenCode SSE events for this Daytona-backed chat runtime.

        Supports replay
        from buffered events using Last-Event-ID and transparently reconnects stopped or
        archived runtimes.

        Args:
          last_event_id: Replay events after this sequence number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/agent/v2/chat/{id}/stream", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"last_event_id": last_event_id}, chat_stream_params.ChatStreamParams
                ),
            ),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[ChatStreamResponse],
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create = to_raw_response_wrapper(
            chat.create,
        )
        self.delete = to_raw_response_wrapper(
            chat.delete,
        )
        self.cancel = to_raw_response_wrapper(
            chat.cancel,
        )
        self.reply_to_question = to_raw_response_wrapper(
            chat.reply_to_question,
        )
        self.respond = to_raw_response_wrapper(
            chat.respond,
        )
        self.send_message = to_raw_response_wrapper(
            chat.send_message,
        )
        self.stream = to_raw_response_wrapper(
            chat.stream,
        )

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return FilesResourceWithRawResponse(self._chat.files)


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create = async_to_raw_response_wrapper(
            chat.create,
        )
        self.delete = async_to_raw_response_wrapper(
            chat.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            chat.cancel,
        )
        self.reply_to_question = async_to_raw_response_wrapper(
            chat.reply_to_question,
        )
        self.respond = async_to_raw_response_wrapper(
            chat.respond,
        )
        self.send_message = async_to_raw_response_wrapper(
            chat.send_message,
        )
        self.stream = async_to_raw_response_wrapper(
            chat.stream,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncFilesResourceWithRawResponse(self._chat.files)


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create = to_streamed_response_wrapper(
            chat.create,
        )
        self.delete = to_streamed_response_wrapper(
            chat.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            chat.cancel,
        )
        self.reply_to_question = to_streamed_response_wrapper(
            chat.reply_to_question,
        )
        self.respond = to_streamed_response_wrapper(
            chat.respond,
        )
        self.send_message = to_streamed_response_wrapper(
            chat.send_message,
        )
        self.stream = to_streamed_response_wrapper(
            chat.stream,
        )

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return FilesResourceWithStreamingResponse(self._chat.files)


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create = async_to_streamed_response_wrapper(
            chat.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            chat.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            chat.cancel,
        )
        self.reply_to_question = async_to_streamed_response_wrapper(
            chat.reply_to_question,
        )
        self.respond = async_to_streamed_response_wrapper(
            chat.respond,
        )
        self.send_message = async_to_streamed_response_wrapper(
            chat.send_message,
        )
        self.stream = async_to_streamed_response_wrapper(
            chat.stream,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncFilesResourceWithStreamingResponse(self._chat.files)
