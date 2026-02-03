# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.database.v1 import project_create_params, project_create_branch_params, project_get_connection_params
from ....types.database.v1.project_list_response import ProjectListResponse
from ....types.database.v1.project_create_response import ProjectCreateResponse
from ....types.database.v1.project_delete_response import ProjectDeleteResponse
from ....types.database.v1.project_retrieve_response import ProjectRetrieveResponse
from ....types.database.v1.project_create_branch_response import ProjectCreateBranchResponse
from ....types.database.v1.project_list_branches_response import ProjectListBranchesResponse
from ....types.database.v1.project_get_connection_response import ProjectGetConnectionResponse

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
        name: str,
        description: str | Omit = omit,
        region: Literal[
            "aws-us-east-1",
            "aws-us-east-2",
            "aws-us-west-2",
            "aws-eu-central-1",
            "aws-eu-west-1",
            "aws-eu-west-2",
            "aws-ap-southeast-1",
            "aws-ap-southeast-2",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectCreateResponse:
        """Creates a new serverless Postgres database project powered by Neon.

        Includes
        automatic scaling, connection pooling, and a default 'main' branch with 'neondb'
        database. Supports branching for isolated dev/staging environments. Perfect for
        case management applications, document workflows, and litigation support
        systems.

        Args:
          name: Project name (letters, numbers, hyphens, underscores only)

          description: Optional project description

          region: AWS region for database deployment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/database/v1/projects",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "region": region,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateResponse,
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
    ) -> ProjectRetrieveResponse:
        """
        Retrieves detailed information about a specific database project including
        branches, databases, storage/compute metrics, connection host, and linked
        deployments. Fetches live usage statistics from Neon API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/database/v1/projects/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
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
        """
        Retrieves all serverless Postgres database projects for the authenticated
        organization. Includes storage and compute metrics, plus linked deployments from
        Thurgood apps and Compute instances.
        """
        return self._get(
            "/database/v1/projects",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectListResponse,
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
    ) -> ProjectDeleteResponse:
        """
        Permanently deletes a database project from Neon and marks it as deleted in
        Case.dev. This action cannot be undone and will destroy all data including
        branches and databases. Use with caution.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/database/v1/projects/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDeleteResponse,
        )

    def create_branch(
        self,
        id: str,
        *,
        name: str,
        parent_branch_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectCreateBranchResponse:
        """Creates a new branch from the specified parent branch (or default 'main'
        branch).

        Branches provide instant point-in-time clones of your database for
        isolated development, staging, testing, or feature work. Perfect for testing
        schema changes, running migrations safely, or creating ephemeral preview
        environments.

        Args:
          name: Branch name (letters, numbers, hyphens, underscores only)

          parent_branch_id: Parent branch ID to clone from (defaults to main branch)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/database/v1/projects/{id}/branches",
            body=maybe_transform(
                {
                    "name": name,
                    "parent_branch_id": parent_branch_id,
                },
                project_create_branch_params.ProjectCreateBranchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateBranchResponse,
        )

    def get_connection(
        self,
        id: str,
        *,
        branch: str | Omit = omit,
        pooled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectGetConnectionResponse:
        """Retrieves the PostgreSQL connection URI for a database project.

        Supports
        selecting specific branches and pooled vs direct connections. Connection strings
        include credentials and should be stored securely. Use for configuring
        applications and deployment environments.

        Args:
          branch: Branch name (defaults to 'main')

          pooled: Use pooled connection (PgBouncer)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/database/v1/projects/{id}/connection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "branch": branch,
                        "pooled": pooled,
                    },
                    project_get_connection_params.ProjectGetConnectionParams,
                ),
            ),
            cast_to=ProjectGetConnectionResponse,
        )

    def list_branches(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectListBranchesResponse:
        """Retrieves all branches for a database project.

        Branches enable isolated
        development and testing environments with instant point-in-time cloning. Each
        branch includes the default branch and any custom branches created for staging,
        testing, or feature development.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/database/v1/projects/{id}/branches",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectListBranchesResponse,
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
        name: str,
        description: str | Omit = omit,
        region: Literal[
            "aws-us-east-1",
            "aws-us-east-2",
            "aws-us-west-2",
            "aws-eu-central-1",
            "aws-eu-west-1",
            "aws-eu-west-2",
            "aws-ap-southeast-1",
            "aws-ap-southeast-2",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectCreateResponse:
        """Creates a new serverless Postgres database project powered by Neon.

        Includes
        automatic scaling, connection pooling, and a default 'main' branch with 'neondb'
        database. Supports branching for isolated dev/staging environments. Perfect for
        case management applications, document workflows, and litigation support
        systems.

        Args:
          name: Project name (letters, numbers, hyphens, underscores only)

          description: Optional project description

          region: AWS region for database deployment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/database/v1/projects",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "region": region,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateResponse,
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
    ) -> ProjectRetrieveResponse:
        """
        Retrieves detailed information about a specific database project including
        branches, databases, storage/compute metrics, connection host, and linked
        deployments. Fetches live usage statistics from Neon API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/database/v1/projects/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
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
        """
        Retrieves all serverless Postgres database projects for the authenticated
        organization. Includes storage and compute metrics, plus linked deployments from
        Thurgood apps and Compute instances.
        """
        return await self._get(
            "/database/v1/projects",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectListResponse,
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
    ) -> ProjectDeleteResponse:
        """
        Permanently deletes a database project from Neon and marks it as deleted in
        Case.dev. This action cannot be undone and will destroy all data including
        branches and databases. Use with caution.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/database/v1/projects/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDeleteResponse,
        )

    async def create_branch(
        self,
        id: str,
        *,
        name: str,
        parent_branch_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectCreateBranchResponse:
        """Creates a new branch from the specified parent branch (or default 'main'
        branch).

        Branches provide instant point-in-time clones of your database for
        isolated development, staging, testing, or feature work. Perfect for testing
        schema changes, running migrations safely, or creating ephemeral preview
        environments.

        Args:
          name: Branch name (letters, numbers, hyphens, underscores only)

          parent_branch_id: Parent branch ID to clone from (defaults to main branch)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/database/v1/projects/{id}/branches",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_branch_id": parent_branch_id,
                },
                project_create_branch_params.ProjectCreateBranchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateBranchResponse,
        )

    async def get_connection(
        self,
        id: str,
        *,
        branch: str | Omit = omit,
        pooled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectGetConnectionResponse:
        """Retrieves the PostgreSQL connection URI for a database project.

        Supports
        selecting specific branches and pooled vs direct connections. Connection strings
        include credentials and should be stored securely. Use for configuring
        applications and deployment environments.

        Args:
          branch: Branch name (defaults to 'main')

          pooled: Use pooled connection (PgBouncer)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/database/v1/projects/{id}/connection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "branch": branch,
                        "pooled": pooled,
                    },
                    project_get_connection_params.ProjectGetConnectionParams,
                ),
            ),
            cast_to=ProjectGetConnectionResponse,
        )

    async def list_branches(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectListBranchesResponse:
        """Retrieves all branches for a database project.

        Branches enable isolated
        development and testing environments with instant point-in-time cloning. Each
        branch includes the default branch and any custom branches created for staging,
        testing, or feature development.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/database/v1/projects/{id}/branches",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectListBranchesResponse,
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
        self.create_branch = to_raw_response_wrapper(
            projects.create_branch,
        )
        self.get_connection = to_raw_response_wrapper(
            projects.get_connection,
        )
        self.list_branches = to_raw_response_wrapper(
            projects.list_branches,
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
        self.create_branch = async_to_raw_response_wrapper(
            projects.create_branch,
        )
        self.get_connection = async_to_raw_response_wrapper(
            projects.get_connection,
        )
        self.list_branches = async_to_raw_response_wrapper(
            projects.list_branches,
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
        self.create_branch = to_streamed_response_wrapper(
            projects.create_branch,
        )
        self.get_connection = to_streamed_response_wrapper(
            projects.get_connection,
        )
        self.list_branches = to_streamed_response_wrapper(
            projects.list_branches,
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
        self.create_branch = async_to_streamed_response_wrapper(
            projects.create_branch,
        )
        self.get_connection = async_to_streamed_response_wrapper(
            projects.get_connection,
        )
        self.list_branches = async_to_streamed_response_wrapper(
            projects.list_branches,
        )
