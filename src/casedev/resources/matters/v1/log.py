# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
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
from ....types.matters.v1 import log_list_params, log_create_params, log_export_params
from ....types.matters.v1.log_export_response import LogExportResponse

__all__ = ["LogResource", "AsyncLogResource"]


class LogResource(SyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> LogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return LogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return LogResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        summary: str,
        details: Dict[str, object] | Omit = omit,
        event_type: str | Omit = omit,
        work_item_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Append a manual operational note or event to a matter log.

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
            path_template("/matters/v1/{id}/log", id=id),
            body=maybe_transform(
                {
                    "summary": summary,
                    "details": details,
                    "event_type": event_type,
                    "work_item_id": work_item_id,
                },
                log_create_params.LogCreateParams,
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
        actor_id: str | Omit = omit,
        actor_type: str | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        event_type: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        scope: Union[str, SequenceNotStr[str]] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        work_item_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List the operational history for a matter.

        Args:
          actor_id: Filter by actor ID

          actor_type: Filter by actor type

          end_time: End of time range (ISO 8601)

          event_type: Filter by exact event type

          limit: Maximum number of log entries to return (max 200)

          offset: Number of log entries to skip for pagination

          scope: Filter by scope: matter, work_item, execution, sharing, all

          start_time: Start of time range (ISO 8601)

          work_item_id: Filter by work item ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/matters/v1/{id}/log", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "actor_id": actor_id,
                        "actor_type": actor_type,
                        "end_time": end_time,
                        "event_type": event_type,
                        "limit": limit,
                        "offset": offset,
                        "scope": scope,
                        "start_time": start_time,
                        "work_item_id": work_item_id,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def export(
        self,
        id: str,
        *,
        actor_id: str | Omit = omit,
        actor_type: str | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        event_type: str | Omit = omit,
        format: Literal["json", "jsonl", "csv", "tsv"] | Omit = omit,
        scope: Union[str, SequenceNotStr[str]] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        work_item_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogExportResponse:
        """
        Bulk export matter log entries for audits, visibility, and eval pipelines.
        Supports json, csv, tsv, and jsonl. Limited to 10,000 entries per request.

        Args:
          actor_id: Filter by actor ID

          actor_type: Filter by actor type

          end_time: End of time range (ISO 8601)

          event_type: Filter by exact event type

          format: Export format. Defaults to jsonl.

          scope: Filter by scope: matter, work_item, execution, sharing, all

          start_time: Start of time range (ISO 8601)

          work_item_id: Filter by work item ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/matters/v1/{id}/log/export", id=id),
            body=maybe_transform(
                {
                    "actor_id": actor_id,
                    "actor_type": actor_type,
                    "end_time": end_time,
                    "event_type": event_type,
                    "format": format,
                    "scope": scope,
                    "start_time": start_time,
                    "work_item_id": work_item_id,
                },
                log_export_params.LogExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogExportResponse,
        )


class AsyncLogResource(AsyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> AsyncLogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncLogResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        summary: str,
        details: Dict[str, object] | Omit = omit,
        event_type: str | Omit = omit,
        work_item_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Append a manual operational note or event to a matter log.

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
            path_template("/matters/v1/{id}/log", id=id),
            body=await async_maybe_transform(
                {
                    "summary": summary,
                    "details": details,
                    "event_type": event_type,
                    "work_item_id": work_item_id,
                },
                log_create_params.LogCreateParams,
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
        actor_id: str | Omit = omit,
        actor_type: str | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        event_type: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        scope: Union[str, SequenceNotStr[str]] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        work_item_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List the operational history for a matter.

        Args:
          actor_id: Filter by actor ID

          actor_type: Filter by actor type

          end_time: End of time range (ISO 8601)

          event_type: Filter by exact event type

          limit: Maximum number of log entries to return (max 200)

          offset: Number of log entries to skip for pagination

          scope: Filter by scope: matter, work_item, execution, sharing, all

          start_time: Start of time range (ISO 8601)

          work_item_id: Filter by work item ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/matters/v1/{id}/log", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "actor_id": actor_id,
                        "actor_type": actor_type,
                        "end_time": end_time,
                        "event_type": event_type,
                        "limit": limit,
                        "offset": offset,
                        "scope": scope,
                        "start_time": start_time,
                        "work_item_id": work_item_id,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def export(
        self,
        id: str,
        *,
        actor_id: str | Omit = omit,
        actor_type: str | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        event_type: str | Omit = omit,
        format: Literal["json", "jsonl", "csv", "tsv"] | Omit = omit,
        scope: Union[str, SequenceNotStr[str]] | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        work_item_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogExportResponse:
        """
        Bulk export matter log entries for audits, visibility, and eval pipelines.
        Supports json, csv, tsv, and jsonl. Limited to 10,000 entries per request.

        Args:
          actor_id: Filter by actor ID

          actor_type: Filter by actor type

          end_time: End of time range (ISO 8601)

          event_type: Filter by exact event type

          format: Export format. Defaults to jsonl.

          scope: Filter by scope: matter, work_item, execution, sharing, all

          start_time: Start of time range (ISO 8601)

          work_item_id: Filter by work item ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/matters/v1/{id}/log/export", id=id),
            body=await async_maybe_transform(
                {
                    "actor_id": actor_id,
                    "actor_type": actor_type,
                    "end_time": end_time,
                    "event_type": event_type,
                    "format": format,
                    "scope": scope,
                    "start_time": start_time,
                    "work_item_id": work_item_id,
                },
                log_export_params.LogExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogExportResponse,
        )


class LogResourceWithRawResponse:
    def __init__(self, log: LogResource) -> None:
        self._log = log

        self.create = to_raw_response_wrapper(
            log.create,
        )
        self.list = to_raw_response_wrapper(
            log.list,
        )
        self.export = to_raw_response_wrapper(
            log.export,
        )


class AsyncLogResourceWithRawResponse:
    def __init__(self, log: AsyncLogResource) -> None:
        self._log = log

        self.create = async_to_raw_response_wrapper(
            log.create,
        )
        self.list = async_to_raw_response_wrapper(
            log.list,
        )
        self.export = async_to_raw_response_wrapper(
            log.export,
        )


class LogResourceWithStreamingResponse:
    def __init__(self, log: LogResource) -> None:
        self._log = log

        self.create = to_streamed_response_wrapper(
            log.create,
        )
        self.list = to_streamed_response_wrapper(
            log.list,
        )
        self.export = to_streamed_response_wrapper(
            log.export,
        )


class AsyncLogResourceWithStreamingResponse:
    def __init__(self, log: AsyncLogResource) -> None:
        self._log = log

        self.create = async_to_streamed_response_wrapper(
            log.create,
        )
        self.list = async_to_streamed_response_wrapper(
            log.list,
        )
        self.export = async_to_streamed_response_wrapper(
            log.export,
        )
