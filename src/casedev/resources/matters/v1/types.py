# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
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
from ....types.matters.v1 import type_list_params, type_create_params, type_update_params

__all__ = ["TypesResource", "AsyncTypesResource"]


class TypesResource(SyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> TypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return TypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return TypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        default_agent_type_id: str | Omit = omit,
        default_metadata: Dict[str, object] | Omit = omit,
        default_work_items: Iterable[Dict[str, object]] | Omit = omit,
        description: str | Omit = omit,
        exit_criteria: SequenceNotStr[str] | Omit = omit,
        instructions: str | Omit = omit,
        intake_requirements: SequenceNotStr[str] | Omit = omit,
        is_active: bool | Omit = omit,
        orchestration_mode: Literal["auto", "human"] | Omit = omit,
        review_agent_type_id: str | Omit = omit,
        review_criteria: SequenceNotStr[str] | Omit = omit,
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
        Create a matter type with plain-English operating instructions and seeded work.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/matters/v1/types",
            body=maybe_transform(
                {
                    "name": name,
                    "default_agent_type_id": default_agent_type_id,
                    "default_metadata": default_metadata,
                    "default_work_items": default_work_items,
                    "description": description,
                    "exit_criteria": exit_criteria,
                    "instructions": instructions,
                    "intake_requirements": intake_requirements,
                    "is_active": is_active,
                    "orchestration_mode": orchestration_mode,
                    "review_agent_type_id": review_agent_type_id,
                    "review_criteria": review_criteria,
                    "skill_refs": skill_refs,
                    "slug": slug,
                },
                type_create_params.TypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> None:
        """
        Get a single matter type.

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
            path_template("/matters/v1/types/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        id: str,
        *,
        default_agent_type_id: Optional[str] | Omit = omit,
        default_metadata: Dict[str, object] | Omit = omit,
        default_work_items: Iterable[Dict[str, object]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        exit_criteria: SequenceNotStr[str] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        intake_requirements: SequenceNotStr[str] | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        orchestration_mode: Literal["auto", "human"] | Omit = omit,
        review_agent_type_id: Optional[str] | Omit = omit,
        review_criteria: SequenceNotStr[str] | Omit = omit,
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
        Update a matter type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/matters/v1/types/{id}", id=id),
            body=maybe_transform(
                {
                    "default_agent_type_id": default_agent_type_id,
                    "default_metadata": default_metadata,
                    "default_work_items": default_work_items,
                    "description": description,
                    "exit_criteria": exit_criteria,
                    "instructions": instructions,
                    "intake_requirements": intake_requirements,
                    "is_active": is_active,
                    "name": name,
                    "orchestration_mode": orchestration_mode,
                    "review_agent_type_id": review_agent_type_id,
                    "review_criteria": review_criteria,
                    "skill_refs": skill_refs,
                    "slug": slug,
                },
                type_update_params.TypeUpdateParams,
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
        List matter types for the authenticated organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/matters/v1/types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"active": active}, type_list_params.TypeListParams),
            ),
            cast_to=NoneType,
        )


class AsyncTypesResource(AsyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def with_raw_response(self) -> AsyncTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        default_agent_type_id: str | Omit = omit,
        default_metadata: Dict[str, object] | Omit = omit,
        default_work_items: Iterable[Dict[str, object]] | Omit = omit,
        description: str | Omit = omit,
        exit_criteria: SequenceNotStr[str] | Omit = omit,
        instructions: str | Omit = omit,
        intake_requirements: SequenceNotStr[str] | Omit = omit,
        is_active: bool | Omit = omit,
        orchestration_mode: Literal["auto", "human"] | Omit = omit,
        review_agent_type_id: str | Omit = omit,
        review_criteria: SequenceNotStr[str] | Omit = omit,
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
        Create a matter type with plain-English operating instructions and seeded work.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/matters/v1/types",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "default_agent_type_id": default_agent_type_id,
                    "default_metadata": default_metadata,
                    "default_work_items": default_work_items,
                    "description": description,
                    "exit_criteria": exit_criteria,
                    "instructions": instructions,
                    "intake_requirements": intake_requirements,
                    "is_active": is_active,
                    "orchestration_mode": orchestration_mode,
                    "review_agent_type_id": review_agent_type_id,
                    "review_criteria": review_criteria,
                    "skill_refs": skill_refs,
                    "slug": slug,
                },
                type_create_params.TypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> None:
        """
        Get a single matter type.

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
            path_template("/matters/v1/types/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        id: str,
        *,
        default_agent_type_id: Optional[str] | Omit = omit,
        default_metadata: Dict[str, object] | Omit = omit,
        default_work_items: Iterable[Dict[str, object]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        exit_criteria: SequenceNotStr[str] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        intake_requirements: SequenceNotStr[str] | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        orchestration_mode: Literal["auto", "human"] | Omit = omit,
        review_agent_type_id: Optional[str] | Omit = omit,
        review_criteria: SequenceNotStr[str] | Omit = omit,
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
        Update a matter type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/matters/v1/types/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "default_agent_type_id": default_agent_type_id,
                    "default_metadata": default_metadata,
                    "default_work_items": default_work_items,
                    "description": description,
                    "exit_criteria": exit_criteria,
                    "instructions": instructions,
                    "intake_requirements": intake_requirements,
                    "is_active": is_active,
                    "name": name,
                    "orchestration_mode": orchestration_mode,
                    "review_agent_type_id": review_agent_type_id,
                    "review_criteria": review_criteria,
                    "skill_refs": skill_refs,
                    "slug": slug,
                },
                type_update_params.TypeUpdateParams,
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
        List matter types for the authenticated organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/matters/v1/types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"active": active}, type_list_params.TypeListParams),
            ),
            cast_to=NoneType,
        )


class TypesResourceWithRawResponse:
    def __init__(self, types: TypesResource) -> None:
        self._types = types

        self.create = to_raw_response_wrapper(
            types.create,
        )
        self.retrieve = to_raw_response_wrapper(
            types.retrieve,
        )
        self.update = to_raw_response_wrapper(
            types.update,
        )
        self.list = to_raw_response_wrapper(
            types.list,
        )


class AsyncTypesResourceWithRawResponse:
    def __init__(self, types: AsyncTypesResource) -> None:
        self._types = types

        self.create = async_to_raw_response_wrapper(
            types.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            types.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            types.update,
        )
        self.list = async_to_raw_response_wrapper(
            types.list,
        )


class TypesResourceWithStreamingResponse:
    def __init__(self, types: TypesResource) -> None:
        self._types = types

        self.create = to_streamed_response_wrapper(
            types.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            types.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            types.update,
        )
        self.list = to_streamed_response_wrapper(
            types.list,
        )


class AsyncTypesResourceWithStreamingResponse:
    def __init__(self, types: AsyncTypesResource) -> None:
        self._types = types

        self.create = async_to_streamed_response_wrapper(
            types.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            types.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            types.update,
        )
        self.list = async_to_streamed_response_wrapper(
            types.list,
        )
