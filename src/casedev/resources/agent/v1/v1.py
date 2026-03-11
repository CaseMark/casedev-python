# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .run import (
    RunResource,
    AsyncRunResource,
    RunResourceWithRawResponse,
    AsyncRunResourceWithRawResponse,
    RunResourceWithStreamingResponse,
    AsyncRunResourceWithStreamingResponse,
)
from .chat import (
    ChatResource,
    AsyncChatResource,
    ChatResourceWithRawResponse,
    AsyncChatResourceWithRawResponse,
    ChatResourceWithStreamingResponse,
    AsyncChatResourceWithStreamingResponse,
)
from .agents import (
    AgentsResource,
    AsyncAgentsResource,
    AgentsResourceWithRawResponse,
    AsyncAgentsResourceWithRawResponse,
    AgentsResourceWithStreamingResponse,
    AsyncAgentsResourceWithStreamingResponse,
)
from .execute import (
    ExecuteResource,
    AsyncExecuteResource,
    ExecuteResourceWithRawResponse,
    AsyncExecuteResourceWithRawResponse,
    ExecuteResourceWithStreamingResponse,
    AsyncExecuteResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def agents(self) -> AgentsResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AgentsResource(self._client)

    @cached_property
    def run(self) -> RunResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return RunResource(self._client)

    @cached_property
    def execute(self) -> ExecuteResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return ExecuteResource(self._client)

    @cached_property
    def chat(self) -> ChatResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return ChatResource(self._client)

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
    def agents(self) -> AsyncAgentsResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncAgentsResource(self._client)

    @cached_property
    def run(self) -> AsyncRunResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncRunResource(self._client)

    @cached_property
    def execute(self) -> AsyncExecuteResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncExecuteResource(self._client)

    @cached_property
    def chat(self) -> AsyncChatResource:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncChatResource(self._client)

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
    def agents(self) -> AgentsResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AgentsResourceWithRawResponse(self._v1.agents)

    @cached_property
    def run(self) -> RunResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return RunResourceWithRawResponse(self._v1.run)

    @cached_property
    def execute(self) -> ExecuteResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return ExecuteResourceWithRawResponse(self._v1.execute)

    @cached_property
    def chat(self) -> ChatResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return ChatResourceWithRawResponse(self._v1.chat)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncAgentsResourceWithRawResponse(self._v1.agents)

    @cached_property
    def run(self) -> AsyncRunResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncRunResourceWithRawResponse(self._v1.run)

    @cached_property
    def execute(self) -> AsyncExecuteResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncExecuteResourceWithRawResponse(self._v1.execute)

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncChatResourceWithRawResponse(self._v1.chat)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def agents(self) -> AgentsResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AgentsResourceWithStreamingResponse(self._v1.agents)

    @cached_property
    def run(self) -> RunResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return RunResourceWithStreamingResponse(self._v1.run)

    @cached_property
    def execute(self) -> ExecuteResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return ExecuteResourceWithStreamingResponse(self._v1.execute)

    @cached_property
    def chat(self) -> ChatResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return ChatResourceWithStreamingResponse(self._v1.chat)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncAgentsResourceWithStreamingResponse(self._v1.agents)

    @cached_property
    def run(self) -> AsyncRunResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncRunResourceWithStreamingResponse(self._v1.run)

    @cached_property
    def execute(self) -> AsyncExecuteResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncExecuteResourceWithStreamingResponse(self._v1.execute)

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        """
        Create, manage, and execute AI agents with tool access, sandbox environments, and async run workflows
        """
        return AsyncChatResourceWithStreamingResponse(self._v1.chat)
