# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .namespaces import (
    NamespacesResource,
    AsyncNamespacesResource,
    NamespacesResourceWithRawResponse,
    AsyncNamespacesResourceWithRawResponse,
    NamespacesResourceWithStreamingResponse,
    AsyncNamespacesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SkillsResource", "AsyncSkillsResource"]


class SkillsResource(SyncAPIResource):
    @cached_property
    def namespaces(self) -> NamespacesResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return NamespacesResource(self._client)

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


class AsyncSkillsResource(AsyncAPIResource):
    @cached_property
    def namespaces(self) -> AsyncNamespacesResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncNamespacesResource(self._client)

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


class SkillsResourceWithRawResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

    @cached_property
    def namespaces(self) -> NamespacesResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return NamespacesResourceWithRawResponse(self._skills.namespaces)


class AsyncSkillsResourceWithRawResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncNamespacesResourceWithRawResponse(self._skills.namespaces)


class SkillsResourceWithStreamingResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

    @cached_property
    def namespaces(self) -> NamespacesResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return NamespacesResourceWithStreamingResponse(self._skills.namespaces)


class AsyncSkillsResourceWithStreamingResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncNamespacesResourceWithStreamingResponse(self._skills.namespaces)
