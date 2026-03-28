# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
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
from ....types.matters.v1 import (
    work_item_list_params,
    work_item_create_params,
    work_item_decide_params,
    work_item_update_params,
)

__all__ = ["WorkItemsResource", "AsyncWorkItemsResource"]


class WorkItemsResource(SyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> WorkItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return WorkItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return WorkItemsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        title: str,
        assignee_id: str | Omit = omit,
        description: str | Omit = omit,
        due_at: Union[str, datetime] | Omit = omit,
        exit_criteria: SequenceNotStr[str] | Omit = omit,
        instructions: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        priority: Literal["low", "normal", "high", "urgent"] | Omit = omit,
        type: Literal[
            "task", "deadline", "review", "filing", "communication", "research", "drafting", "collection", "intake"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create an active work item on a matter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/matters/v1/{id}/work-items", id=id),
            body=maybe_transform(
                {
                    "title": title,
                    "assignee_id": assignee_id,
                    "description": description,
                    "due_at": due_at,
                    "exit_criteria": exit_criteria,
                    "instructions": instructions,
                    "metadata": metadata,
                    "priority": priority,
                    "type": type,
                },
                work_item_create_params.WorkItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        work_item_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get a single work item for a matter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not work_item_id:
            raise ValueError(f"Expected a non-empty value for `work_item_id` but received {work_item_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/matters/v1/{id}/work-items/{work_item_id}", id=id, work_item_id=work_item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        work_item_id: str,
        *,
        id: str,
        assignee_id: Optional[str] | Omit = omit,
        completed_at: Union[str, datetime, None] | Omit = omit,
        description: str | Omit = omit,
        due_at: Union[str, datetime, None] | Omit = omit,
        exit_criteria: SequenceNotStr[str] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        priority: Literal["low", "normal", "high", "urgent"] | Omit = omit,
        started_at: Union[str, datetime, None] | Omit = omit,
        status: Literal["draft", "queued", "in_progress", "blocked", "in_review", "awaiting_human", "done", "canceled"]
        | Omit = omit,
        title: str | Omit = omit,
        type: Literal[
            "task", "deadline", "review", "filing", "communication", "research", "drafting", "collection", "intake"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a matter work item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not work_item_id:
            raise ValueError(f"Expected a non-empty value for `work_item_id` but received {work_item_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/matters/v1/{id}/work-items/{work_item_id}", id=id, work_item_id=work_item_id),
            body=maybe_transform(
                {
                    "assignee_id": assignee_id,
                    "completed_at": completed_at,
                    "description": description,
                    "due_at": due_at,
                    "exit_criteria": exit_criteria,
                    "instructions": instructions,
                    "metadata": metadata,
                    "priority": priority,
                    "started_at": started_at,
                    "status": status,
                    "title": title,
                    "type": type,
                },
                work_item_update_params.WorkItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        id: str,
        *,
        assignee_id: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List active work items for a matter.

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
            path_template("/matters/v1/{id}/work-items", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "assignee_id": assignee_id,
                        "status": status,
                    },
                    work_item_list_params.WorkItemListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def decide(
        self,
        work_item_id: str,
        *,
        id: str,
        decision: Literal["approve", "revise", "block", "reassign"],
        agent_type_id: Optional[str] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Allow a human to act as the orchestrator for a work item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not work_item_id:
            raise ValueError(f"Expected a non-empty value for `work_item_id` but received {work_item_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/matters/v1/{id}/work-items/{work_item_id}/decision", id=id, work_item_id=work_item_id),
            body=maybe_transform(
                {
                    "decision": decision,
                    "agent_type_id": agent_type_id,
                    "metadata": metadata,
                    "reason": reason,
                },
                work_item_decide_params.WorkItemDecideParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_executions(
        self,
        work_item_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List execution attempts for a work item, including agent and run linkage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not work_item_id:
            raise ValueError(f"Expected a non-empty value for `work_item_id` but received {work_item_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/matters/v1/{id}/work-items/{work_item_id}/executions", id=id, work_item_id=work_item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWorkItemsResource(AsyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> AsyncWorkItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncWorkItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        title: str,
        assignee_id: str | Omit = omit,
        description: str | Omit = omit,
        due_at: Union[str, datetime] | Omit = omit,
        exit_criteria: SequenceNotStr[str] | Omit = omit,
        instructions: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        priority: Literal["low", "normal", "high", "urgent"] | Omit = omit,
        type: Literal[
            "task", "deadline", "review", "filing", "communication", "research", "drafting", "collection", "intake"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create an active work item on a matter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/matters/v1/{id}/work-items", id=id),
            body=await async_maybe_transform(
                {
                    "title": title,
                    "assignee_id": assignee_id,
                    "description": description,
                    "due_at": due_at,
                    "exit_criteria": exit_criteria,
                    "instructions": instructions,
                    "metadata": metadata,
                    "priority": priority,
                    "type": type,
                },
                work_item_create_params.WorkItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        work_item_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get a single work item for a matter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not work_item_id:
            raise ValueError(f"Expected a non-empty value for `work_item_id` but received {work_item_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/matters/v1/{id}/work-items/{work_item_id}", id=id, work_item_id=work_item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        work_item_id: str,
        *,
        id: str,
        assignee_id: Optional[str] | Omit = omit,
        completed_at: Union[str, datetime, None] | Omit = omit,
        description: str | Omit = omit,
        due_at: Union[str, datetime, None] | Omit = omit,
        exit_criteria: SequenceNotStr[str] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        priority: Literal["low", "normal", "high", "urgent"] | Omit = omit,
        started_at: Union[str, datetime, None] | Omit = omit,
        status: Literal["draft", "queued", "in_progress", "blocked", "in_review", "awaiting_human", "done", "canceled"]
        | Omit = omit,
        title: str | Omit = omit,
        type: Literal[
            "task", "deadline", "review", "filing", "communication", "research", "drafting", "collection", "intake"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a matter work item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not work_item_id:
            raise ValueError(f"Expected a non-empty value for `work_item_id` but received {work_item_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/matters/v1/{id}/work-items/{work_item_id}", id=id, work_item_id=work_item_id),
            body=await async_maybe_transform(
                {
                    "assignee_id": assignee_id,
                    "completed_at": completed_at,
                    "description": description,
                    "due_at": due_at,
                    "exit_criteria": exit_criteria,
                    "instructions": instructions,
                    "metadata": metadata,
                    "priority": priority,
                    "started_at": started_at,
                    "status": status,
                    "title": title,
                    "type": type,
                },
                work_item_update_params.WorkItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        id: str,
        *,
        assignee_id: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List active work items for a matter.

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
            path_template("/matters/v1/{id}/work-items", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "assignee_id": assignee_id,
                        "status": status,
                    },
                    work_item_list_params.WorkItemListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def decide(
        self,
        work_item_id: str,
        *,
        id: str,
        decision: Literal["approve", "revise", "block", "reassign"],
        agent_type_id: Optional[str] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Allow a human to act as the orchestrator for a work item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not work_item_id:
            raise ValueError(f"Expected a non-empty value for `work_item_id` but received {work_item_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/matters/v1/{id}/work-items/{work_item_id}/decision", id=id, work_item_id=work_item_id),
            body=await async_maybe_transform(
                {
                    "decision": decision,
                    "agent_type_id": agent_type_id,
                    "metadata": metadata,
                    "reason": reason,
                },
                work_item_decide_params.WorkItemDecideParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_executions(
        self,
        work_item_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List execution attempts for a work item, including agent and run linkage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not work_item_id:
            raise ValueError(f"Expected a non-empty value for `work_item_id` but received {work_item_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/matters/v1/{id}/work-items/{work_item_id}/executions", id=id, work_item_id=work_item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WorkItemsResourceWithRawResponse:
    def __init__(self, work_items: WorkItemsResource) -> None:
        self._work_items = work_items

        self.create = to_raw_response_wrapper(
            work_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            work_items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            work_items.update,
        )
        self.list = to_raw_response_wrapper(
            work_items.list,
        )
        self.decide = to_raw_response_wrapper(
            work_items.decide,
        )
        self.list_executions = to_raw_response_wrapper(
            work_items.list_executions,
        )


class AsyncWorkItemsResourceWithRawResponse:
    def __init__(self, work_items: AsyncWorkItemsResource) -> None:
        self._work_items = work_items

        self.create = async_to_raw_response_wrapper(
            work_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            work_items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            work_items.update,
        )
        self.list = async_to_raw_response_wrapper(
            work_items.list,
        )
        self.decide = async_to_raw_response_wrapper(
            work_items.decide,
        )
        self.list_executions = async_to_raw_response_wrapper(
            work_items.list_executions,
        )


class WorkItemsResourceWithStreamingResponse:
    def __init__(self, work_items: WorkItemsResource) -> None:
        self._work_items = work_items

        self.create = to_streamed_response_wrapper(
            work_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            work_items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            work_items.update,
        )
        self.list = to_streamed_response_wrapper(
            work_items.list,
        )
        self.decide = to_streamed_response_wrapper(
            work_items.decide,
        )
        self.list_executions = to_streamed_response_wrapper(
            work_items.list_executions,
        )


class AsyncWorkItemsResourceWithStreamingResponse:
    def __init__(self, work_items: AsyncWorkItemsResource) -> None:
        self._work_items = work_items

        self.create = async_to_streamed_response_wrapper(
            work_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            work_items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            work_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            work_items.list,
        )
        self.decide = async_to_streamed_response_wrapper(
            work_items.decide,
        )
        self.list_executions = async_to_streamed_response_wrapper(
            work_items.list_executions,
        )
