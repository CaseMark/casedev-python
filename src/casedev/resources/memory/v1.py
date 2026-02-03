# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.memory import v1_list_params, v1_create_params, v1_search_params, v1_delete_all_params
from ...types.memory.v1_list_response import V1ListResponse
from ...types.memory.v1_create_response import V1CreateResponse
from ...types.memory.v1_delete_response import V1DeleteResponse
from ...types.memory.v1_search_response import V1SearchResponse
from ...types.memory.v1_retrieve_response import V1RetrieveResponse
from ...types.memory.v1_delete_all_response import V1DeleteAllResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        messages: Iterable[v1_create_params.Message],
        category: str | Omit = omit,
        extraction_prompt: str | Omit = omit,
        infer: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        tag_1: str | Omit = omit,
        tag_10: str | Omit = omit,
        tag_11: str | Omit = omit,
        tag_12: str | Omit = omit,
        tag_2: str | Omit = omit,
        tag_3: str | Omit = omit,
        tag_4: str | Omit = omit,
        tag_5: str | Omit = omit,
        tag_6: str | Omit = omit,
        tag_7: str | Omit = omit,
        tag_8: str | Omit = omit,
        tag_9: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1CreateResponse:
        """Store memories from conversation messages.

        Automatically extracts facts and
        handles deduplication.

        Use tag_1 through tag_12 for filtering - these are generic indexed fields you
        can use for any purpose:

        - Legal app: tag_1=client_id, tag_2=matter_id
        - Healthcare: tag_1=patient_id, tag_2=encounter_id
        - E-commerce: tag_1=customer_id, tag_2=order_id

        Args:
          messages: Conversation messages to extract memories from

          category: Custom category (e.g., "fact", "preference", "deadline")

          extraction_prompt: Optional custom prompt for fact extraction

          infer: Whether to extract facts from messages (default: true)

          metadata: Additional metadata (not indexed)

          tag_1: Generic indexed filter field 1 (you decide what it means)

          tag_10: Generic indexed filter field 10

          tag_11: Generic indexed filter field 11

          tag_12: Generic indexed filter field 12

          tag_2: Generic indexed filter field 2

          tag_3: Generic indexed filter field 3

          tag_4: Generic indexed filter field 4

          tag_5: Generic indexed filter field 5

          tag_6: Generic indexed filter field 6

          tag_7: Generic indexed filter field 7

          tag_8: Generic indexed filter field 8

          tag_9: Generic indexed filter field 9

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/memory/v1",
            body=maybe_transform(
                {
                    "messages": messages,
                    "category": category,
                    "extraction_prompt": extraction_prompt,
                    "infer": infer,
                    "metadata": metadata,
                    "tag_1": tag_1,
                    "tag_10": tag_10,
                    "tag_11": tag_11,
                    "tag_12": tag_12,
                    "tag_2": tag_2,
                    "tag_3": tag_3,
                    "tag_4": tag_4,
                    "tag_5": tag_5,
                    "tag_6": tag_6,
                    "tag_7": tag_7,
                    "tag_8": tag_8,
                    "tag_9": tag_9,
                },
                v1_create_params.V1CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1CreateResponse,
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
    ) -> V1RetrieveResponse:
        """
        Retrieve a single memory by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/memory/v1/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1RetrieveResponse,
        )

    def list(
        self,
        *,
        category: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        tag_1: str | Omit = omit,
        tag_10: str | Omit = omit,
        tag_11: str | Omit = omit,
        tag_12: str | Omit = omit,
        tag_2: str | Omit = omit,
        tag_3: str | Omit = omit,
        tag_4: str | Omit = omit,
        tag_5: str | Omit = omit,
        tag_6: str | Omit = omit,
        tag_7: str | Omit = omit,
        tag_8: str | Omit = omit,
        tag_9: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ListResponse:
        """
        List all memories with optional filtering by tags and category.

        Args:
          category: Filter by category

          limit: Number of results

          offset: Pagination offset

          tag_1: Filter by tag_1

          tag_10: Filter by tag_10

          tag_11: Filter by tag_11

          tag_12: Filter by tag_12

          tag_2: Filter by tag_2

          tag_3: Filter by tag_3

          tag_4: Filter by tag_4

          tag_5: Filter by tag_5

          tag_6: Filter by tag_6

          tag_7: Filter by tag_7

          tag_8: Filter by tag_8

          tag_9: Filter by tag_9

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/memory/v1",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "limit": limit,
                        "offset": offset,
                        "tag_1": tag_1,
                        "tag_10": tag_10,
                        "tag_11": tag_11,
                        "tag_12": tag_12,
                        "tag_2": tag_2,
                        "tag_3": tag_3,
                        "tag_4": tag_4,
                        "tag_5": tag_5,
                        "tag_6": tag_6,
                        "tag_7": tag_7,
                        "tag_8": tag_8,
                        "tag_9": tag_9,
                    },
                    v1_list_params.V1ListParams,
                ),
            ),
            cast_to=V1ListResponse,
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
    ) -> V1DeleteResponse:
        """
        Delete a single memory by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/memory/v1/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1DeleteResponse,
        )

    def delete_all(
        self,
        *,
        tag_1: str | Omit = omit,
        tag_10: str | Omit = omit,
        tag_11: str | Omit = omit,
        tag_12: str | Omit = omit,
        tag_2: str | Omit = omit,
        tag_3: str | Omit = omit,
        tag_4: str | Omit = omit,
        tag_5: str | Omit = omit,
        tag_6: str | Omit = omit,
        tag_7: str | Omit = omit,
        tag_8: str | Omit = omit,
        tag_9: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1DeleteAllResponse:
        """Delete multiple memories matching tag filter criteria.

        CAUTION: This will delete
        all matching memories for your organization.

        Args:
          tag_1: Filter by tag_1

          tag_10: Filter by tag_10

          tag_11: Filter by tag_11

          tag_12: Filter by tag_12

          tag_2: Filter by tag_2

          tag_3: Filter by tag_3

          tag_4: Filter by tag_4

          tag_5: Filter by tag_5

          tag_6: Filter by tag_6

          tag_7: Filter by tag_7

          tag_8: Filter by tag_8

          tag_9: Filter by tag_9

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/memory/v1",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tag_1": tag_1,
                        "tag_10": tag_10,
                        "tag_11": tag_11,
                        "tag_12": tag_12,
                        "tag_2": tag_2,
                        "tag_3": tag_3,
                        "tag_4": tag_4,
                        "tag_5": tag_5,
                        "tag_6": tag_6,
                        "tag_7": tag_7,
                        "tag_8": tag_8,
                        "tag_9": tag_9,
                    },
                    v1_delete_all_params.V1DeleteAllParams,
                ),
            ),
            cast_to=V1DeleteAllResponse,
        )

    def search(
        self,
        *,
        query: str,
        category: str | Omit = omit,
        tag_1: str | Omit = omit,
        tag_10: str | Omit = omit,
        tag_11: str | Omit = omit,
        tag_12: str | Omit = omit,
        tag_2: str | Omit = omit,
        tag_3: str | Omit = omit,
        tag_4: str | Omit = omit,
        tag_5: str | Omit = omit,
        tag_6: str | Omit = omit,
        tag_7: str | Omit = omit,
        tag_8: str | Omit = omit,
        tag_9: str | Omit = omit,
        top_k: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1SearchResponse:
        """Search memories using semantic similarity.

        Filter by tag fields to narrow
        results.

        Use tag_1 through tag_12 for filtering - these are generic indexed fields you
        define:

        - Legal app: tag_1=client_id, tag_2=matter_id
        - Healthcare: tag_1=patient_id, tag_2=encounter_id

        Args:
          query: Search query for semantic matching

          category: Filter by category

          tag_1: Filter by tag_1

          tag_10: Filter by tag_10

          tag_11: Filter by tag_11

          tag_12: Filter by tag_12

          tag_2: Filter by tag_2

          tag_3: Filter by tag_3

          tag_4: Filter by tag_4

          tag_5: Filter by tag_5

          tag_6: Filter by tag_6

          tag_7: Filter by tag_7

          tag_8: Filter by tag_8

          tag_9: Filter by tag_9

          top_k: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/memory/v1/search",
            body=maybe_transform(
                {
                    "query": query,
                    "category": category,
                    "tag_1": tag_1,
                    "tag_10": tag_10,
                    "tag_11": tag_11,
                    "tag_12": tag_12,
                    "tag_2": tag_2,
                    "tag_3": tag_3,
                    "tag_4": tag_4,
                    "tag_5": tag_5,
                    "tag_6": tag_6,
                    "tag_7": tag_7,
                    "tag_8": tag_8,
                    "tag_9": tag_9,
                    "top_k": top_k,
                },
                v1_search_params.V1SearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1SearchResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        messages: Iterable[v1_create_params.Message],
        category: str | Omit = omit,
        extraction_prompt: str | Omit = omit,
        infer: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        tag_1: str | Omit = omit,
        tag_10: str | Omit = omit,
        tag_11: str | Omit = omit,
        tag_12: str | Omit = omit,
        tag_2: str | Omit = omit,
        tag_3: str | Omit = omit,
        tag_4: str | Omit = omit,
        tag_5: str | Omit = omit,
        tag_6: str | Omit = omit,
        tag_7: str | Omit = omit,
        tag_8: str | Omit = omit,
        tag_9: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1CreateResponse:
        """Store memories from conversation messages.

        Automatically extracts facts and
        handles deduplication.

        Use tag_1 through tag_12 for filtering - these are generic indexed fields you
        can use for any purpose:

        - Legal app: tag_1=client_id, tag_2=matter_id
        - Healthcare: tag_1=patient_id, tag_2=encounter_id
        - E-commerce: tag_1=customer_id, tag_2=order_id

        Args:
          messages: Conversation messages to extract memories from

          category: Custom category (e.g., "fact", "preference", "deadline")

          extraction_prompt: Optional custom prompt for fact extraction

          infer: Whether to extract facts from messages (default: true)

          metadata: Additional metadata (not indexed)

          tag_1: Generic indexed filter field 1 (you decide what it means)

          tag_10: Generic indexed filter field 10

          tag_11: Generic indexed filter field 11

          tag_12: Generic indexed filter field 12

          tag_2: Generic indexed filter field 2

          tag_3: Generic indexed filter field 3

          tag_4: Generic indexed filter field 4

          tag_5: Generic indexed filter field 5

          tag_6: Generic indexed filter field 6

          tag_7: Generic indexed filter field 7

          tag_8: Generic indexed filter field 8

          tag_9: Generic indexed filter field 9

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/memory/v1",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "category": category,
                    "extraction_prompt": extraction_prompt,
                    "infer": infer,
                    "metadata": metadata,
                    "tag_1": tag_1,
                    "tag_10": tag_10,
                    "tag_11": tag_11,
                    "tag_12": tag_12,
                    "tag_2": tag_2,
                    "tag_3": tag_3,
                    "tag_4": tag_4,
                    "tag_5": tag_5,
                    "tag_6": tag_6,
                    "tag_7": tag_7,
                    "tag_8": tag_8,
                    "tag_9": tag_9,
                },
                v1_create_params.V1CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1CreateResponse,
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
    ) -> V1RetrieveResponse:
        """
        Retrieve a single memory by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/memory/v1/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1RetrieveResponse,
        )

    async def list(
        self,
        *,
        category: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        tag_1: str | Omit = omit,
        tag_10: str | Omit = omit,
        tag_11: str | Omit = omit,
        tag_12: str | Omit = omit,
        tag_2: str | Omit = omit,
        tag_3: str | Omit = omit,
        tag_4: str | Omit = omit,
        tag_5: str | Omit = omit,
        tag_6: str | Omit = omit,
        tag_7: str | Omit = omit,
        tag_8: str | Omit = omit,
        tag_9: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ListResponse:
        """
        List all memories with optional filtering by tags and category.

        Args:
          category: Filter by category

          limit: Number of results

          offset: Pagination offset

          tag_1: Filter by tag_1

          tag_10: Filter by tag_10

          tag_11: Filter by tag_11

          tag_12: Filter by tag_12

          tag_2: Filter by tag_2

          tag_3: Filter by tag_3

          tag_4: Filter by tag_4

          tag_5: Filter by tag_5

          tag_6: Filter by tag_6

          tag_7: Filter by tag_7

          tag_8: Filter by tag_8

          tag_9: Filter by tag_9

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/memory/v1",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "limit": limit,
                        "offset": offset,
                        "tag_1": tag_1,
                        "tag_10": tag_10,
                        "tag_11": tag_11,
                        "tag_12": tag_12,
                        "tag_2": tag_2,
                        "tag_3": tag_3,
                        "tag_4": tag_4,
                        "tag_5": tag_5,
                        "tag_6": tag_6,
                        "tag_7": tag_7,
                        "tag_8": tag_8,
                        "tag_9": tag_9,
                    },
                    v1_list_params.V1ListParams,
                ),
            ),
            cast_to=V1ListResponse,
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
    ) -> V1DeleteResponse:
        """
        Delete a single memory by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/memory/v1/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1DeleteResponse,
        )

    async def delete_all(
        self,
        *,
        tag_1: str | Omit = omit,
        tag_10: str | Omit = omit,
        tag_11: str | Omit = omit,
        tag_12: str | Omit = omit,
        tag_2: str | Omit = omit,
        tag_3: str | Omit = omit,
        tag_4: str | Omit = omit,
        tag_5: str | Omit = omit,
        tag_6: str | Omit = omit,
        tag_7: str | Omit = omit,
        tag_8: str | Omit = omit,
        tag_9: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1DeleteAllResponse:
        """Delete multiple memories matching tag filter criteria.

        CAUTION: This will delete
        all matching memories for your organization.

        Args:
          tag_1: Filter by tag_1

          tag_10: Filter by tag_10

          tag_11: Filter by tag_11

          tag_12: Filter by tag_12

          tag_2: Filter by tag_2

          tag_3: Filter by tag_3

          tag_4: Filter by tag_4

          tag_5: Filter by tag_5

          tag_6: Filter by tag_6

          tag_7: Filter by tag_7

          tag_8: Filter by tag_8

          tag_9: Filter by tag_9

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/memory/v1",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tag_1": tag_1,
                        "tag_10": tag_10,
                        "tag_11": tag_11,
                        "tag_12": tag_12,
                        "tag_2": tag_2,
                        "tag_3": tag_3,
                        "tag_4": tag_4,
                        "tag_5": tag_5,
                        "tag_6": tag_6,
                        "tag_7": tag_7,
                        "tag_8": tag_8,
                        "tag_9": tag_9,
                    },
                    v1_delete_all_params.V1DeleteAllParams,
                ),
            ),
            cast_to=V1DeleteAllResponse,
        )

    async def search(
        self,
        *,
        query: str,
        category: str | Omit = omit,
        tag_1: str | Omit = omit,
        tag_10: str | Omit = omit,
        tag_11: str | Omit = omit,
        tag_12: str | Omit = omit,
        tag_2: str | Omit = omit,
        tag_3: str | Omit = omit,
        tag_4: str | Omit = omit,
        tag_5: str | Omit = omit,
        tag_6: str | Omit = omit,
        tag_7: str | Omit = omit,
        tag_8: str | Omit = omit,
        tag_9: str | Omit = omit,
        top_k: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1SearchResponse:
        """Search memories using semantic similarity.

        Filter by tag fields to narrow
        results.

        Use tag_1 through tag_12 for filtering - these are generic indexed fields you
        define:

        - Legal app: tag_1=client_id, tag_2=matter_id
        - Healthcare: tag_1=patient_id, tag_2=encounter_id

        Args:
          query: Search query for semantic matching

          category: Filter by category

          tag_1: Filter by tag_1

          tag_10: Filter by tag_10

          tag_11: Filter by tag_11

          tag_12: Filter by tag_12

          tag_2: Filter by tag_2

          tag_3: Filter by tag_3

          tag_4: Filter by tag_4

          tag_5: Filter by tag_5

          tag_6: Filter by tag_6

          tag_7: Filter by tag_7

          tag_8: Filter by tag_8

          tag_9: Filter by tag_9

          top_k: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/memory/v1/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "category": category,
                    "tag_1": tag_1,
                    "tag_10": tag_10,
                    "tag_11": tag_11,
                    "tag_12": tag_12,
                    "tag_2": tag_2,
                    "tag_3": tag_3,
                    "tag_4": tag_4,
                    "tag_5": tag_5,
                    "tag_6": tag_6,
                    "tag_7": tag_7,
                    "tag_8": tag_8,
                    "tag_9": tag_9,
                    "top_k": top_k,
                },
                v1_search_params.V1SearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1SearchResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.create = to_raw_response_wrapper(
            v1.create,
        )
        self.retrieve = to_raw_response_wrapper(
            v1.retrieve,
        )
        self.list = to_raw_response_wrapper(
            v1.list,
        )
        self.delete = to_raw_response_wrapper(
            v1.delete,
        )
        self.delete_all = to_raw_response_wrapper(
            v1.delete_all,
        )
        self.search = to_raw_response_wrapper(
            v1.search,
        )


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.create = async_to_raw_response_wrapper(
            v1.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            v1.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            v1.list,
        )
        self.delete = async_to_raw_response_wrapper(
            v1.delete,
        )
        self.delete_all = async_to_raw_response_wrapper(
            v1.delete_all,
        )
        self.search = async_to_raw_response_wrapper(
            v1.search,
        )


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.create = to_streamed_response_wrapper(
            v1.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            v1.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            v1.list,
        )
        self.delete = to_streamed_response_wrapper(
            v1.delete,
        )
        self.delete_all = to_streamed_response_wrapper(
            v1.delete_all,
        )
        self.search = to_streamed_response_wrapper(
            v1.search,
        )


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.create = async_to_streamed_response_wrapper(
            v1.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            v1.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            v1.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            v1.delete,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            v1.delete_all,
        )
        self.search = async_to_streamed_response_wrapper(
            v1.search,
        )
