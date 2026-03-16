# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .custom import (
    CustomResource,
    AsyncCustomResource,
    CustomResourceWithRawResponse,
    AsyncCustomResourceWithRawResponse,
    CustomResourceWithStreamingResponse,
    AsyncCustomResourceWithStreamingResponse,
)
from ...types import skill_create_params, skill_update_params, skill_resolve_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.skill_read_response import SkillReadResponse
from ...types.skill_create_response import SkillCreateResponse
from ...types.skill_delete_response import SkillDeleteResponse
from ...types.skill_update_response import SkillUpdateResponse
from ...types.skill_resolve_response import SkillResolveResponse

__all__ = ["SkillsResource", "AsyncSkillsResource"]


class SkillsResource(SyncAPIResource):
    """Search and read legal AI skills for agents"""

    @cached_property
    def custom(self) -> CustomResource:
        """Search and read legal AI skills for agents"""
        return CustomResource(self._client)

    @cached_property
    def with_raw_response(self) -> SkillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return SkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return SkillsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content: str,
        name: str,
        metadata: object | Omit = omit,
        slug: str | Omit = omit,
        summary: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillCreateResponse:
        """Create an org-scoped custom skill.

        The skill will be searchable via
        /skills/resolve alongside curated skills.

        Args:
          content: Full skill content in markdown

          name: Skill name

          metadata: Arbitrary metadata (author, license, etc.)

          slug: URL-safe slug. Auto-generated from name if omitted.

          summary: Brief description (1-2 sentences)

          tags: Tags for categorization and search boosting

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/skills",
            body=maybe_transform(
                {
                    "content": content,
                    "name": name,
                    "metadata": metadata,
                    "slug": slug,
                    "summary": summary,
                    "tags": tags,
                },
                skill_create_params.SkillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillCreateResponse,
        )

    def update(
        self,
        path_slug: str,
        *,
        content: str | Omit = omit,
        metadata: object | Omit = omit,
        name: str | Omit = omit,
        body_slug: str | Omit = omit,
        summary: Optional[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillUpdateResponse:
        """Update an org-scoped custom skill by slug.

        Only provided fields are updated.
        Version is auto-incremented.

        Args:
          body_slug: New slug (renames the skill)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_slug:
            raise ValueError(f"Expected a non-empty value for `path_slug` but received {path_slug!r}")
        return self._put(
            f"/skills/{path_slug}",
            body=maybe_transform(
                {
                    "content": content,
                    "metadata": metadata,
                    "name": name,
                    "body_slug": body_slug,
                    "summary": summary,
                    "tags": tags,
                },
                skill_update_params.SkillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillUpdateResponse,
        )

    def delete(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillDeleteResponse:
        """Soft-delete an org-scoped custom skill by slug.

        The skill will no longer appear
        in search results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            f"/skills/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillDeleteResponse,
        )

    def read(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillReadResponse:
        """Read the full content of a legal skill by its slug.

        Returns markdown content,
        tags, and metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            f"/skills/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillReadResponse,
        )

    def resolve(
        self,
        *,
        q: str,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillResolveResponse:
        """
        Search the Legal Skills Store using hybrid search (text + tag + semantic).
        Returns ranked results with relevance scores.

        Args:
          q: Search query string

          limit: Maximum number of results to return (1-20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/skills/resolve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                    },
                    skill_resolve_params.SkillResolveParams,
                ),
            ),
            cast_to=SkillResolveResponse,
        )


class AsyncSkillsResource(AsyncAPIResource):
    """Search and read legal AI skills for agents"""

    @cached_property
    def custom(self) -> AsyncCustomResource:
        """Search and read legal AI skills for agents"""
        return AsyncCustomResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSkillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncSkillsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content: str,
        name: str,
        metadata: object | Omit = omit,
        slug: str | Omit = omit,
        summary: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillCreateResponse:
        """Create an org-scoped custom skill.

        The skill will be searchable via
        /skills/resolve alongside curated skills.

        Args:
          content: Full skill content in markdown

          name: Skill name

          metadata: Arbitrary metadata (author, license, etc.)

          slug: URL-safe slug. Auto-generated from name if omitted.

          summary: Brief description (1-2 sentences)

          tags: Tags for categorization and search boosting

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/skills",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "name": name,
                    "metadata": metadata,
                    "slug": slug,
                    "summary": summary,
                    "tags": tags,
                },
                skill_create_params.SkillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillCreateResponse,
        )

    async def update(
        self,
        path_slug: str,
        *,
        content: str | Omit = omit,
        metadata: object | Omit = omit,
        name: str | Omit = omit,
        body_slug: str | Omit = omit,
        summary: Optional[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillUpdateResponse:
        """Update an org-scoped custom skill by slug.

        Only provided fields are updated.
        Version is auto-incremented.

        Args:
          body_slug: New slug (renames the skill)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_slug:
            raise ValueError(f"Expected a non-empty value for `path_slug` but received {path_slug!r}")
        return await self._put(
            f"/skills/{path_slug}",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "metadata": metadata,
                    "name": name,
                    "body_slug": body_slug,
                    "summary": summary,
                    "tags": tags,
                },
                skill_update_params.SkillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillUpdateResponse,
        )

    async def delete(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillDeleteResponse:
        """Soft-delete an org-scoped custom skill by slug.

        The skill will no longer appear
        in search results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            f"/skills/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillDeleteResponse,
        )

    async def read(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillReadResponse:
        """Read the full content of a legal skill by its slug.

        Returns markdown content,
        tags, and metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            f"/skills/{slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillReadResponse,
        )

    async def resolve(
        self,
        *,
        q: str,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillResolveResponse:
        """
        Search the Legal Skills Store using hybrid search (text + tag + semantic).
        Returns ranked results with relevance scores.

        Args:
          q: Search query string

          limit: Maximum number of results to return (1-20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/skills/resolve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                    },
                    skill_resolve_params.SkillResolveParams,
                ),
            ),
            cast_to=SkillResolveResponse,
        )


class SkillsResourceWithRawResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.create = to_raw_response_wrapper(
            skills.create,
        )
        self.update = to_raw_response_wrapper(
            skills.update,
        )
        self.delete = to_raw_response_wrapper(
            skills.delete,
        )
        self.read = to_raw_response_wrapper(
            skills.read,
        )
        self.resolve = to_raw_response_wrapper(
            skills.resolve,
        )

    @cached_property
    def custom(self) -> CustomResourceWithRawResponse:
        """Search and read legal AI skills for agents"""
        return CustomResourceWithRawResponse(self._skills.custom)


class AsyncSkillsResourceWithRawResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.create = async_to_raw_response_wrapper(
            skills.create,
        )
        self.update = async_to_raw_response_wrapper(
            skills.update,
        )
        self.delete = async_to_raw_response_wrapper(
            skills.delete,
        )
        self.read = async_to_raw_response_wrapper(
            skills.read,
        )
        self.resolve = async_to_raw_response_wrapper(
            skills.resolve,
        )

    @cached_property
    def custom(self) -> AsyncCustomResourceWithRawResponse:
        """Search and read legal AI skills for agents"""
        return AsyncCustomResourceWithRawResponse(self._skills.custom)


class SkillsResourceWithStreamingResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.create = to_streamed_response_wrapper(
            skills.create,
        )
        self.update = to_streamed_response_wrapper(
            skills.update,
        )
        self.delete = to_streamed_response_wrapper(
            skills.delete,
        )
        self.read = to_streamed_response_wrapper(
            skills.read,
        )
        self.resolve = to_streamed_response_wrapper(
            skills.resolve,
        )

    @cached_property
    def custom(self) -> CustomResourceWithStreamingResponse:
        """Search and read legal AI skills for agents"""
        return CustomResourceWithStreamingResponse(self._skills.custom)


class AsyncSkillsResourceWithStreamingResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.create = async_to_streamed_response_wrapper(
            skills.create,
        )
        self.update = async_to_streamed_response_wrapper(
            skills.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            skills.delete,
        )
        self.read = async_to_streamed_response_wrapper(
            skills.read,
        )
        self.resolve = async_to_streamed_response_wrapper(
            skills.resolve,
        )

    @cached_property
    def custom(self) -> AsyncCustomResourceWithStreamingResponse:
        """Search and read legal AI skills for agents"""
        return AsyncCustomResourceWithStreamingResponse(self._skills.custom)
