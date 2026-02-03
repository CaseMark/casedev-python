# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.applications.v1 import (
    project_create_params,
    project_delete_params,
    project_list_env_params,
    project_create_env_params,
    project_create_domain_params,
    project_get_runtime_logs_params,
    project_list_deployments_params,
    project_create_deployment_params,
)
from ....types.applications.v1.project_list_response import ProjectListResponse

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return ProjectsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        git_repo: str,
        name: str,
        build_command: str | Omit = omit,
        environment_variables: Iterable[project_create_params.EnvironmentVariable] | Omit = omit,
        framework: str | Omit = omit,
        git_branch: str | Omit = omit,
        install_command: str | Omit = omit,
        output_directory: str | Omit = omit,
        root_directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a new web application project

        Args:
          git_repo: GitHub repository URL or "owner/repo"

          name: Project name

          build_command: Custom build command

          environment_variables: Environment variables to set on the project

          framework: Framework (e.g., "nextjs", "remix", "astro")

          git_branch: Git branch to deploy

          install_command: Custom install command

          output_directory: Build output directory

          root_directory: Root directory of the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/applications/v1/projects",
            body=maybe_transform(
                {
                    "git_repo": git_repo,
                    "name": name,
                    "build_command": build_command,
                    "environment_variables": environment_variables,
                    "framework": framework,
                    "git_branch": git_branch,
                    "install_command": install_command,
                    "output_directory": output_directory,
                    "root_directory": root_directory,
                },
                project_create_params.ProjectCreateParams,
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
        Get details of a specific web application project

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
            f"/applications/v1/projects/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectListResponse:
        """List all web application projects"""
        return self._get(
            "/applications/v1/projects",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        delete_from_hosting: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a web application project

        Args:
          delete_from_hosting: Also delete the project from hosting (default: true)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/applications/v1/projects/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"delete_from_hosting": delete_from_hosting}, project_delete_params.ProjectDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    def create_deployment(
        self,
        id: str,
        *,
        environment_variables: Iterable[project_create_deployment_params.EnvironmentVariable] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Trigger a new deployment for a project.

        Args:
          environment_variables: Additional environment variables to set or update before deployment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/applications/v1/projects/{id}/deployments",
            body=maybe_transform(
                {"environment_variables": environment_variables},
                project_create_deployment_params.ProjectCreateDeploymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_domain(
        self,
        id: str,
        *,
        domain: str,
        git_branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add a custom domain to a project

        Args:
          domain: Domain name to add

          git_branch: Git branch to associate with this domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/applications/v1/projects/{id}/domains",
            body=maybe_transform(
                {
                    "domain": domain,
                    "git_branch": git_branch,
                },
                project_create_domain_params.ProjectCreateDomainParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_env(
        self,
        id: str,
        *,
        key: str,
        target: List[Literal["production", "preview", "development"]],
        value: str,
        git_branch: str | Omit = omit,
        type: Literal["plain", "encrypted", "secret"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a new environment variable for a project

        Args:
          key: Environment variable name

          target: Deployment targets for this variable

          value: Environment variable value

          git_branch: Specific git branch (for preview deployments)

          type: Variable type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/applications/v1/projects/{id}/env",
            body=maybe_transform(
                {
                    "key": key,
                    "target": target,
                    "value": value,
                    "git_branch": git_branch,
                    "type": type,
                },
                project_create_env_params.ProjectCreateEnvParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_domain(
        self,
        domain: str,
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
        Remove a domain from a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/applications/v1/projects/{id}/domains/{domain}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_env(
        self,
        env_id: str,
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
        Delete an environment variable from a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not env_id:
            raise ValueError(f"Expected a non-empty value for `env_id` but received {env_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/applications/v1/projects/{id}/env/{env_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_runtime_logs(
        self,
        id: str,
        *,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get runtime/function logs for a project

        Args:
          limit: Maximum number of logs to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/applications/v1/projects/{id}/runtime-logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, project_get_runtime_logs_params.ProjectGetRuntimeLogsParams),
            ),
            cast_to=NoneType,
        )

    def list_deployments(
        self,
        id: str,
        *,
        limit: float | Omit = omit,
        state: str | Omit = omit,
        target: Literal["production", "staging"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List deployments for a specific project

        Args:
          limit: Maximum number of deployments to return

          state: Filter by deployment state

          target: Filter by deployment target

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/applications/v1/projects/{id}/deployments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "state": state,
                        "target": target,
                    },
                    project_list_deployments_params.ProjectListDeploymentsParams,
                ),
            ),
            cast_to=NoneType,
        )

    def list_domains(
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
        List all domains configured for a project

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
            f"/applications/v1/projects/{id}/domains",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_env(
        self,
        id: str,
        *,
        decrypt: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List all environment variables for a project (values are hidden unless
        decrypt=true)

        Args:
          decrypt: Whether to decrypt and return values (requires appropriate permissions)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/applications/v1/projects/{id}/env",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"decrypt": decrypt}, project_list_env_params.ProjectListEnvParams),
            ),
            cast_to=NoneType,
        )


class AsyncProjectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncProjectsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        git_repo: str,
        name: str,
        build_command: str | Omit = omit,
        environment_variables: Iterable[project_create_params.EnvironmentVariable] | Omit = omit,
        framework: str | Omit = omit,
        git_branch: str | Omit = omit,
        install_command: str | Omit = omit,
        output_directory: str | Omit = omit,
        root_directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a new web application project

        Args:
          git_repo: GitHub repository URL or "owner/repo"

          name: Project name

          build_command: Custom build command

          environment_variables: Environment variables to set on the project

          framework: Framework (e.g., "nextjs", "remix", "astro")

          git_branch: Git branch to deploy

          install_command: Custom install command

          output_directory: Build output directory

          root_directory: Root directory of the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/applications/v1/projects",
            body=await async_maybe_transform(
                {
                    "git_repo": git_repo,
                    "name": name,
                    "build_command": build_command,
                    "environment_variables": environment_variables,
                    "framework": framework,
                    "git_branch": git_branch,
                    "install_command": install_command,
                    "output_directory": output_directory,
                    "root_directory": root_directory,
                },
                project_create_params.ProjectCreateParams,
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
        Get details of a specific web application project

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
            f"/applications/v1/projects/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectListResponse:
        """List all web application projects"""
        return await self._get(
            "/applications/v1/projects",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        delete_from_hosting: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a web application project

        Args:
          delete_from_hosting: Also delete the project from hosting (default: true)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/applications/v1/projects/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"delete_from_hosting": delete_from_hosting}, project_delete_params.ProjectDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def create_deployment(
        self,
        id: str,
        *,
        environment_variables: Iterable[project_create_deployment_params.EnvironmentVariable] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Trigger a new deployment for a project.

        Args:
          environment_variables: Additional environment variables to set or update before deployment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/applications/v1/projects/{id}/deployments",
            body=await async_maybe_transform(
                {"environment_variables": environment_variables},
                project_create_deployment_params.ProjectCreateDeploymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_domain(
        self,
        id: str,
        *,
        domain: str,
        git_branch: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add a custom domain to a project

        Args:
          domain: Domain name to add

          git_branch: Git branch to associate with this domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/applications/v1/projects/{id}/domains",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "git_branch": git_branch,
                },
                project_create_domain_params.ProjectCreateDomainParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_env(
        self,
        id: str,
        *,
        key: str,
        target: List[Literal["production", "preview", "development"]],
        value: str,
        git_branch: str | Omit = omit,
        type: Literal["plain", "encrypted", "secret"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a new environment variable for a project

        Args:
          key: Environment variable name

          target: Deployment targets for this variable

          value: Environment variable value

          git_branch: Specific git branch (for preview deployments)

          type: Variable type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/applications/v1/projects/{id}/env",
            body=await async_maybe_transform(
                {
                    "key": key,
                    "target": target,
                    "value": value,
                    "git_branch": git_branch,
                    "type": type,
                },
                project_create_env_params.ProjectCreateEnvParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_domain(
        self,
        domain: str,
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
        Remove a domain from a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/applications/v1/projects/{id}/domains/{domain}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_env(
        self,
        env_id: str,
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
        Delete an environment variable from a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not env_id:
            raise ValueError(f"Expected a non-empty value for `env_id` but received {env_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/applications/v1/projects/{id}/env/{env_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_runtime_logs(
        self,
        id: str,
        *,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get runtime/function logs for a project

        Args:
          limit: Maximum number of logs to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/applications/v1/projects/{id}/runtime-logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit}, project_get_runtime_logs_params.ProjectGetRuntimeLogsParams
                ),
            ),
            cast_to=NoneType,
        )

    async def list_deployments(
        self,
        id: str,
        *,
        limit: float | Omit = omit,
        state: str | Omit = omit,
        target: Literal["production", "staging"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List deployments for a specific project

        Args:
          limit: Maximum number of deployments to return

          state: Filter by deployment state

          target: Filter by deployment target

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/applications/v1/projects/{id}/deployments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "state": state,
                        "target": target,
                    },
                    project_list_deployments_params.ProjectListDeploymentsParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def list_domains(
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
        List all domains configured for a project

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
            f"/applications/v1/projects/{id}/domains",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_env(
        self,
        id: str,
        *,
        decrypt: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List all environment variables for a project (values are hidden unless
        decrypt=true)

        Args:
          decrypt: Whether to decrypt and return values (requires appropriate permissions)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/applications/v1/projects/{id}/env",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"decrypt": decrypt}, project_list_env_params.ProjectListEnvParams),
            ),
            cast_to=NoneType,
        )


class ProjectsResourceWithRawResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.create = to_raw_response_wrapper(
            projects.create,
        )
        self.retrieve = to_raw_response_wrapper(
            projects.retrieve,
        )
        self.list = to_raw_response_wrapper(
            projects.list,
        )
        self.delete = to_raw_response_wrapper(
            projects.delete,
        )
        self.create_deployment = to_raw_response_wrapper(
            projects.create_deployment,
        )
        self.create_domain = to_raw_response_wrapper(
            projects.create_domain,
        )
        self.create_env = to_raw_response_wrapper(
            projects.create_env,
        )
        self.delete_domain = to_raw_response_wrapper(
            projects.delete_domain,
        )
        self.delete_env = to_raw_response_wrapper(
            projects.delete_env,
        )
        self.get_runtime_logs = to_raw_response_wrapper(
            projects.get_runtime_logs,
        )
        self.list_deployments = to_raw_response_wrapper(
            projects.list_deployments,
        )
        self.list_domains = to_raw_response_wrapper(
            projects.list_domains,
        )
        self.list_env = to_raw_response_wrapper(
            projects.list_env,
        )


class AsyncProjectsResourceWithRawResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create = async_to_raw_response_wrapper(
            projects.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            projects.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            projects.list,
        )
        self.delete = async_to_raw_response_wrapper(
            projects.delete,
        )
        self.create_deployment = async_to_raw_response_wrapper(
            projects.create_deployment,
        )
        self.create_domain = async_to_raw_response_wrapper(
            projects.create_domain,
        )
        self.create_env = async_to_raw_response_wrapper(
            projects.create_env,
        )
        self.delete_domain = async_to_raw_response_wrapper(
            projects.delete_domain,
        )
        self.delete_env = async_to_raw_response_wrapper(
            projects.delete_env,
        )
        self.get_runtime_logs = async_to_raw_response_wrapper(
            projects.get_runtime_logs,
        )
        self.list_deployments = async_to_raw_response_wrapper(
            projects.list_deployments,
        )
        self.list_domains = async_to_raw_response_wrapper(
            projects.list_domains,
        )
        self.list_env = async_to_raw_response_wrapper(
            projects.list_env,
        )


class ProjectsResourceWithStreamingResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.create = to_streamed_response_wrapper(
            projects.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            projects.list,
        )
        self.delete = to_streamed_response_wrapper(
            projects.delete,
        )
        self.create_deployment = to_streamed_response_wrapper(
            projects.create_deployment,
        )
        self.create_domain = to_streamed_response_wrapper(
            projects.create_domain,
        )
        self.create_env = to_streamed_response_wrapper(
            projects.create_env,
        )
        self.delete_domain = to_streamed_response_wrapper(
            projects.delete_domain,
        )
        self.delete_env = to_streamed_response_wrapper(
            projects.delete_env,
        )
        self.get_runtime_logs = to_streamed_response_wrapper(
            projects.get_runtime_logs,
        )
        self.list_deployments = to_streamed_response_wrapper(
            projects.list_deployments,
        )
        self.list_domains = to_streamed_response_wrapper(
            projects.list_domains,
        )
        self.list_env = to_streamed_response_wrapper(
            projects.list_env,
        )


class AsyncProjectsResourceWithStreamingResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create = async_to_streamed_response_wrapper(
            projects.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            projects.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            projects.delete,
        )
        self.create_deployment = async_to_streamed_response_wrapper(
            projects.create_deployment,
        )
        self.create_domain = async_to_streamed_response_wrapper(
            projects.create_domain,
        )
        self.create_env = async_to_streamed_response_wrapper(
            projects.create_env,
        )
        self.delete_domain = async_to_streamed_response_wrapper(
            projects.delete_domain,
        )
        self.delete_env = async_to_streamed_response_wrapper(
            projects.delete_env,
        )
        self.get_runtime_logs = async_to_streamed_response_wrapper(
            projects.get_runtime_logs,
        )
        self.list_deployments = async_to_streamed_response_wrapper(
            projects.list_deployments,
        )
        self.list_domains = async_to_streamed_response_wrapper(
            projects.list_domains,
        )
        self.list_env = async_to_streamed_response_wrapper(
            projects.list_env,
        )
