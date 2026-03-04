# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .projects import (
    ProjectsResource,
    AsyncProjectsResource,
    ProjectsResourceWithRawResponse,
    AsyncProjectsResourceWithRawResponse,
    ProjectsResourceWithStreamingResponse,
    AsyncProjectsResourceWithStreamingResponse,
)
from .workflows import (
    WorkflowsResource,
    AsyncWorkflowsResource,
    WorkflowsResourceWithRawResponse,
    AsyncWorkflowsResourceWithRawResponse,
    WorkflowsResourceWithStreamingResponse,
    AsyncWorkflowsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .deployments import (
    DeploymentsResource,
    AsyncDeploymentsResource,
    DeploymentsResourceWithRawResponse,
    AsyncDeploymentsResourceWithRawResponse,
    DeploymentsResourceWithStreamingResponse,
    AsyncDeploymentsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def deployments(self) -> DeploymentsResource:
        """Web application deployment management"""
        return DeploymentsResource(self._client)

    @cached_property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self._client)

    @cached_property
    def workflows(self) -> WorkflowsResource:
        """Web application deployment management"""
        return WorkflowsResource(self._client)

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


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def deployments(self) -> AsyncDeploymentsResource:
        """Web application deployment management"""
        return AsyncDeploymentsResource(self._client)

    @cached_property
    def projects(self) -> AsyncProjectsResource:
        return AsyncProjectsResource(self._client)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResource:
        """Web application deployment management"""
        return AsyncWorkflowsResource(self._client)

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


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def deployments(self) -> DeploymentsResourceWithRawResponse:
        """Web application deployment management"""
        return DeploymentsResourceWithRawResponse(self._v1.deployments)

    @cached_property
    def projects(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self._v1.projects)

    @cached_property
    def workflows(self) -> WorkflowsResourceWithRawResponse:
        """Web application deployment management"""
        return WorkflowsResourceWithRawResponse(self._v1.workflows)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithRawResponse:
        """Web application deployment management"""
        return AsyncDeploymentsResourceWithRawResponse(self._v1.deployments)

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self._v1.projects)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResourceWithRawResponse:
        """Web application deployment management"""
        return AsyncWorkflowsResourceWithRawResponse(self._v1.workflows)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def deployments(self) -> DeploymentsResourceWithStreamingResponse:
        """Web application deployment management"""
        return DeploymentsResourceWithStreamingResponse(self._v1.deployments)

    @cached_property
    def projects(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self._v1.projects)

    @cached_property
    def workflows(self) -> WorkflowsResourceWithStreamingResponse:
        """Web application deployment management"""
        return WorkflowsResourceWithStreamingResponse(self._v1.workflows)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        """Web application deployment management"""
        return AsyncDeploymentsResourceWithStreamingResponse(self._v1.deployments)

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self._v1.projects)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        """Web application deployment management"""
        return AsyncWorkflowsResourceWithStreamingResponse(self._v1.workflows)
