# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...._base_client import make_request_options
from ....types.matters.v1 import content_purge_create_params
from ....types.matters.v1.content_purge_create_response import ContentPurgeCreateResponse
from ....types.matters.v1.content_purge_retrieve_response import ContentPurgeRetrieveResponse

__all__ = ["ContentPurgesResource", "AsyncContentPurgesResource"]


class ContentPurgesResource(SyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> ContentPurgesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return ContentPurgesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentPurgesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return ContentPurgesResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        request_id: str,
        object_ids: SequenceNotStr[str] | Omit = omit,
        session_ids: SequenceNotStr[str] | Omit = omit,
        transcription_ids: SequenceNotStr[str] | Omit = omit,
        work_item_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentPurgeCreateResponse:
        """
        Queues an idempotent hard deletion of explicitly owned content while preserving
        the Matter, Vault, and unrelated content. Use unified matter.content_purge
        webhooks for completion, not polling.

        Args:
          request_id: Stable caller idempotency ID; cannot be reused with different targets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/matters/v1/{id}/content-purges", id=id),
            body=maybe_transform(
                {
                    "request_id": request_id,
                    "object_ids": object_ids,
                    "session_ids": session_ids,
                    "transcription_ids": transcription_ids,
                    "work_item_ids": work_item_ids,
                },
                content_purge_create_params.ContentPurgeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentPurgeCreateResponse,
        )

    def retrieve(
        self,
        purge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentPurgeRetrieveResponse:
        """Owner-only receipt for operator diagnostics.

        Integrations must use unified
        content-purge webhooks rather than polling.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not purge_id:
            raise ValueError(f"Expected a non-empty value for `purge_id` but received {purge_id!r}")
        return self._get(
            path_template("/matters/v1/content-purges/{purge_id}", purge_id=purge_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentPurgeRetrieveResponse,
        )


class AsyncContentPurgesResource(AsyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> AsyncContentPurgesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContentPurgesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentPurgesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncContentPurgesResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        request_id: str,
        object_ids: SequenceNotStr[str] | Omit = omit,
        session_ids: SequenceNotStr[str] | Omit = omit,
        transcription_ids: SequenceNotStr[str] | Omit = omit,
        work_item_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentPurgeCreateResponse:
        """
        Queues an idempotent hard deletion of explicitly owned content while preserving
        the Matter, Vault, and unrelated content. Use unified matter.content_purge
        webhooks for completion, not polling.

        Args:
          request_id: Stable caller idempotency ID; cannot be reused with different targets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/matters/v1/{id}/content-purges", id=id),
            body=await async_maybe_transform(
                {
                    "request_id": request_id,
                    "object_ids": object_ids,
                    "session_ids": session_ids,
                    "transcription_ids": transcription_ids,
                    "work_item_ids": work_item_ids,
                },
                content_purge_create_params.ContentPurgeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentPurgeCreateResponse,
        )

    async def retrieve(
        self,
        purge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentPurgeRetrieveResponse:
        """Owner-only receipt for operator diagnostics.

        Integrations must use unified
        content-purge webhooks rather than polling.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not purge_id:
            raise ValueError(f"Expected a non-empty value for `purge_id` but received {purge_id!r}")
        return await self._get(
            path_template("/matters/v1/content-purges/{purge_id}", purge_id=purge_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentPurgeRetrieveResponse,
        )


class ContentPurgesResourceWithRawResponse:
    def __init__(self, content_purges: ContentPurgesResource) -> None:
        self._content_purges = content_purges

        self.create = to_raw_response_wrapper(
            content_purges.create,
        )
        self.retrieve = to_raw_response_wrapper(
            content_purges.retrieve,
        )


class AsyncContentPurgesResourceWithRawResponse:
    def __init__(self, content_purges: AsyncContentPurgesResource) -> None:
        self._content_purges = content_purges

        self.create = async_to_raw_response_wrapper(
            content_purges.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            content_purges.retrieve,
        )


class ContentPurgesResourceWithStreamingResponse:
    def __init__(self, content_purges: ContentPurgesResource) -> None:
        self._content_purges = content_purges

        self.create = to_streamed_response_wrapper(
            content_purges.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            content_purges.retrieve,
        )


class AsyncContentPurgesResourceWithStreamingResponse:
    def __init__(self, content_purges: AsyncContentPurgesResource) -> None:
        self._content_purges = content_purges

        self.create = async_to_streamed_response_wrapper(
            content_purges.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            content_purges.retrieve,
        )
