# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .log import (
    LogResource,
    AsyncLogResource,
    LogResourceWithRawResponse,
    AsyncLogResourceWithRawResponse,
    LogResourceWithStreamingResponse,
    AsyncLogResourceWithStreamingResponse,
)
from .types import (
    TypesResource,
    AsyncTypesResource,
    TypesResourceWithRawResponse,
    AsyncTypesResourceWithRawResponse,
    TypesResourceWithStreamingResponse,
    AsyncTypesResourceWithStreamingResponse,
)
from .shares import (
    SharesResource,
    AsyncSharesResource,
    SharesResourceWithRawResponse,
    AsyncSharesResourceWithRawResponse,
    SharesResourceWithStreamingResponse,
    AsyncSharesResourceWithStreamingResponse,
)
from .parties import (
    PartiesResource,
    AsyncPartiesResource,
    PartiesResourceWithRawResponse,
    AsyncPartiesResourceWithRawResponse,
    PartiesResourceWithStreamingResponse,
    AsyncPartiesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .work_items import (
    WorkItemsResource,
    AsyncWorkItemsResource,
    WorkItemsResourceWithRawResponse,
    AsyncWorkItemsResourceWithRawResponse,
    WorkItemsResourceWithStreamingResponse,
    AsyncWorkItemsResourceWithStreamingResponse,
)
from .agent_types import (
    AgentTypesResource,
    AsyncAgentTypesResource,
    AgentTypesResourceWithRawResponse,
    AsyncAgentTypesResourceWithRawResponse,
    AgentTypesResourceWithStreamingResponse,
    AsyncAgentTypesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .events.events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .matter_parties import (
    MatterPartiesResource,
    AsyncMatterPartiesResource,
    MatterPartiesResourceWithRawResponse,
    AsyncMatterPartiesResourceWithRawResponse,
    MatterPartiesResourceWithStreamingResponse,
    AsyncMatterPartiesResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.matters import v1_list_params, v1_create_params, v1_update_params

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def agent_types(self) -> AgentTypesResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return AgentTypesResource(self._client)

    @cached_property
    def parties(self) -> PartiesResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return PartiesResource(self._client)

    @cached_property
    def types(self) -> TypesResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return TypesResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def log(self) -> LogResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return LogResource(self._client)

    @cached_property
    def matter_parties(self) -> MatterPartiesResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return MatterPartiesResource(self._client)

    @cached_property
    def shares(self) -> SharesResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return SharesResource(self._client)

    @cached_property
    def work_items(self) -> WorkItemsResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return WorkItemsResource(self._client)

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
        title: str,
        billing: Dict[str, object] | Omit = omit,
        client_name: str | Omit = omit,
        client_party_id: Optional[str] | Omit = omit,
        custom_fields: Dict[str, object] | Omit = omit,
        description: str | Omit = omit,
        display_id: str | Omit = omit,
        important_dates: Dict[str, object] | Omit = omit,
        jurisdiction: Dict[str, object] | Omit = omit,
        matter_type: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        practice_area: str | Omit = omit,
        responsible_attorney_id: str | Omit = omit,
        status: Literal["intake", "open", "pending", "closed", "archived"] | Omit = omit,
        subtype: str | Omit = omit,
        vault: v1_create_params.Vault | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a new legal matter and provision its primary vault.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/matters/v1",
            body=maybe_transform(
                {
                    "title": title,
                    "billing": billing,
                    "client_name": client_name,
                    "client_party_id": client_party_id,
                    "custom_fields": custom_fields,
                    "description": description,
                    "display_id": display_id,
                    "important_dates": important_dates,
                    "jurisdiction": jurisdiction,
                    "matter_type": matter_type,
                    "metadata": metadata,
                    "practice_area": practice_area,
                    "responsible_attorney_id": responsible_attorney_id,
                    "status": status,
                    "subtype": subtype,
                    "vault": vault,
                },
                v1_create_params.V1CreateParams,
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
        Get a single matter by ID.

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
            path_template("/matters/v1/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        id: str,
        *,
        archived_at: Union[str, datetime, None] | Omit = omit,
        billing: Dict[str, object] | Omit = omit,
        client_name: str | Omit = omit,
        client_party_id: Optional[str] | Omit = omit,
        custom_fields: Dict[str, object] | Omit = omit,
        description: str | Omit = omit,
        display_id: str | Omit = omit,
        important_dates: Dict[str, object] | Omit = omit,
        jurisdiction: Dict[str, object] | Omit = omit,
        matter_type: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        practice_area: str | Omit = omit,
        responsible_attorney_id: str | Omit = omit,
        status: Literal["intake", "open", "pending", "closed", "archived"] | Omit = omit,
        subtype: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update mutable matter fields.

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
            path_template("/matters/v1/{id}", id=id),
            body=maybe_transform(
                {
                    "archived_at": archived_at,
                    "billing": billing,
                    "client_name": client_name,
                    "client_party_id": client_party_id,
                    "custom_fields": custom_fields,
                    "description": description,
                    "display_id": display_id,
                    "important_dates": important_dates,
                    "jurisdiction": jurisdiction,
                    "matter_type": matter_type,
                    "metadata": metadata,
                    "practice_area": practice_area,
                    "responsible_attorney_id": responsible_attorney_id,
                    "status": status,
                    "subtype": subtype,
                    "title": title,
                },
                v1_update_params.V1UpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        matter_type: str | Omit = omit,
        practice_area: str | Omit = omit,
        query: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List matters for the authenticated organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/matters/v1",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "matter_type": matter_type,
                        "practice_area": practice_area,
                        "query": query,
                        "status": status,
                    },
                    v1_list_params.V1ListParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncV1Resource(AsyncAPIResource):
    """Matter-native legal workspaces and orchestration primitives"""

    @cached_property
    def agent_types(self) -> AsyncAgentTypesResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncAgentTypesResource(self._client)

    @cached_property
    def parties(self) -> AsyncPartiesResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncPartiesResource(self._client)

    @cached_property
    def types(self) -> AsyncTypesResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncTypesResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def log(self) -> AsyncLogResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncLogResource(self._client)

    @cached_property
    def matter_parties(self) -> AsyncMatterPartiesResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncMatterPartiesResource(self._client)

    @cached_property
    def shares(self) -> AsyncSharesResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncSharesResource(self._client)

    @cached_property
    def work_items(self) -> AsyncWorkItemsResource:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncWorkItemsResource(self._client)

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
        title: str,
        billing: Dict[str, object] | Omit = omit,
        client_name: str | Omit = omit,
        client_party_id: Optional[str] | Omit = omit,
        custom_fields: Dict[str, object] | Omit = omit,
        description: str | Omit = omit,
        display_id: str | Omit = omit,
        important_dates: Dict[str, object] | Omit = omit,
        jurisdiction: Dict[str, object] | Omit = omit,
        matter_type: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        practice_area: str | Omit = omit,
        responsible_attorney_id: str | Omit = omit,
        status: Literal["intake", "open", "pending", "closed", "archived"] | Omit = omit,
        subtype: str | Omit = omit,
        vault: v1_create_params.Vault | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a new legal matter and provision its primary vault.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/matters/v1",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "billing": billing,
                    "client_name": client_name,
                    "client_party_id": client_party_id,
                    "custom_fields": custom_fields,
                    "description": description,
                    "display_id": display_id,
                    "important_dates": important_dates,
                    "jurisdiction": jurisdiction,
                    "matter_type": matter_type,
                    "metadata": metadata,
                    "practice_area": practice_area,
                    "responsible_attorney_id": responsible_attorney_id,
                    "status": status,
                    "subtype": subtype,
                    "vault": vault,
                },
                v1_create_params.V1CreateParams,
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
        Get a single matter by ID.

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
            path_template("/matters/v1/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        id: str,
        *,
        archived_at: Union[str, datetime, None] | Omit = omit,
        billing: Dict[str, object] | Omit = omit,
        client_name: str | Omit = omit,
        client_party_id: Optional[str] | Omit = omit,
        custom_fields: Dict[str, object] | Omit = omit,
        description: str | Omit = omit,
        display_id: str | Omit = omit,
        important_dates: Dict[str, object] | Omit = omit,
        jurisdiction: Dict[str, object] | Omit = omit,
        matter_type: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        practice_area: str | Omit = omit,
        responsible_attorney_id: str | Omit = omit,
        status: Literal["intake", "open", "pending", "closed", "archived"] | Omit = omit,
        subtype: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update mutable matter fields.

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
            path_template("/matters/v1/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "archived_at": archived_at,
                    "billing": billing,
                    "client_name": client_name,
                    "client_party_id": client_party_id,
                    "custom_fields": custom_fields,
                    "description": description,
                    "display_id": display_id,
                    "important_dates": important_dates,
                    "jurisdiction": jurisdiction,
                    "matter_type": matter_type,
                    "metadata": metadata,
                    "practice_area": practice_area,
                    "responsible_attorney_id": responsible_attorney_id,
                    "status": status,
                    "subtype": subtype,
                    "title": title,
                },
                v1_update_params.V1UpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        matter_type: str | Omit = omit,
        practice_area: str | Omit = omit,
        query: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List matters for the authenticated organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/matters/v1",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "matter_type": matter_type,
                        "practice_area": practice_area,
                        "query": query,
                        "status": status,
                    },
                    v1_list_params.V1ListParams,
                ),
            ),
            cast_to=NoneType,
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
        self.update = to_raw_response_wrapper(
            v1.update,
        )
        self.list = to_raw_response_wrapper(
            v1.list,
        )

    @cached_property
    def agent_types(self) -> AgentTypesResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AgentTypesResourceWithRawResponse(self._v1.agent_types)

    @cached_property
    def parties(self) -> PartiesResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return PartiesResourceWithRawResponse(self._v1.parties)

    @cached_property
    def types(self) -> TypesResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return TypesResourceWithRawResponse(self._v1.types)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._v1.events)

    @cached_property
    def log(self) -> LogResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return LogResourceWithRawResponse(self._v1.log)

    @cached_property
    def matter_parties(self) -> MatterPartiesResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return MatterPartiesResourceWithRawResponse(self._v1.matter_parties)

    @cached_property
    def shares(self) -> SharesResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return SharesResourceWithRawResponse(self._v1.shares)

    @cached_property
    def work_items(self) -> WorkItemsResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return WorkItemsResourceWithRawResponse(self._v1.work_items)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.create = async_to_raw_response_wrapper(
            v1.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            v1.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            v1.update,
        )
        self.list = async_to_raw_response_wrapper(
            v1.list,
        )

    @cached_property
    def agent_types(self) -> AsyncAgentTypesResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncAgentTypesResourceWithRawResponse(self._v1.agent_types)

    @cached_property
    def parties(self) -> AsyncPartiesResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncPartiesResourceWithRawResponse(self._v1.parties)

    @cached_property
    def types(self) -> AsyncTypesResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncTypesResourceWithRawResponse(self._v1.types)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._v1.events)

    @cached_property
    def log(self) -> AsyncLogResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncLogResourceWithRawResponse(self._v1.log)

    @cached_property
    def matter_parties(self) -> AsyncMatterPartiesResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncMatterPartiesResourceWithRawResponse(self._v1.matter_parties)

    @cached_property
    def shares(self) -> AsyncSharesResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncSharesResourceWithRawResponse(self._v1.shares)

    @cached_property
    def work_items(self) -> AsyncWorkItemsResourceWithRawResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncWorkItemsResourceWithRawResponse(self._v1.work_items)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.create = to_streamed_response_wrapper(
            v1.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            v1.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            v1.update,
        )
        self.list = to_streamed_response_wrapper(
            v1.list,
        )

    @cached_property
    def agent_types(self) -> AgentTypesResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AgentTypesResourceWithStreamingResponse(self._v1.agent_types)

    @cached_property
    def parties(self) -> PartiesResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return PartiesResourceWithStreamingResponse(self._v1.parties)

    @cached_property
    def types(self) -> TypesResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return TypesResourceWithStreamingResponse(self._v1.types)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._v1.events)

    @cached_property
    def log(self) -> LogResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return LogResourceWithStreamingResponse(self._v1.log)

    @cached_property
    def matter_parties(self) -> MatterPartiesResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return MatterPartiesResourceWithStreamingResponse(self._v1.matter_parties)

    @cached_property
    def shares(self) -> SharesResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return SharesResourceWithStreamingResponse(self._v1.shares)

    @cached_property
    def work_items(self) -> WorkItemsResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return WorkItemsResourceWithStreamingResponse(self._v1.work_items)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.create = async_to_streamed_response_wrapper(
            v1.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            v1.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            v1.update,
        )
        self.list = async_to_streamed_response_wrapper(
            v1.list,
        )

    @cached_property
    def agent_types(self) -> AsyncAgentTypesResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncAgentTypesResourceWithStreamingResponse(self._v1.agent_types)

    @cached_property
    def parties(self) -> AsyncPartiesResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncPartiesResourceWithStreamingResponse(self._v1.parties)

    @cached_property
    def types(self) -> AsyncTypesResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncTypesResourceWithStreamingResponse(self._v1.types)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._v1.events)

    @cached_property
    def log(self) -> AsyncLogResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncLogResourceWithStreamingResponse(self._v1.log)

    @cached_property
    def matter_parties(self) -> AsyncMatterPartiesResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncMatterPartiesResourceWithStreamingResponse(self._v1.matter_parties)

    @cached_property
    def shares(self) -> AsyncSharesResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncSharesResourceWithStreamingResponse(self._v1.shares)

    @cached_property
    def work_items(self) -> AsyncWorkItemsResourceWithStreamingResponse:
        """Matter-native legal workspaces and orchestration primitives"""
        return AsyncWorkItemsResourceWithStreamingResponse(self._v1.work_items)
