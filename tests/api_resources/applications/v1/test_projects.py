# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.applications.v1 import (
    ProjectListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        project = client.applications.v1.projects.create(
            git_repo="gitRepo",
            name="name",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        project = client.applications.v1.projects.create(
            git_repo="gitRepo",
            name="name",
            build_command="buildCommand",
            environment_variables=[
                {
                    "key": "key",
                    "target": ["production"],
                    "value": "value",
                    "type": "plain",
                }
            ],
            framework="framework",
            git_branch="gitBranch",
            install_command="installCommand",
            output_directory="outputDirectory",
            root_directory="rootDirectory",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.applications.v1.projects.with_raw_response.create(
            git_repo="gitRepo",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.applications.v1.projects.with_streaming_response.create(
            git_repo="gitRepo",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        project = client.applications.v1.projects.retrieve(
            "id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.applications.v1.projects.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.applications.v1.projects.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.projects.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        project = client.applications.v1.projects.list()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.applications.v1.projects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.applications.v1.projects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        project = client.applications.v1.projects.delete(
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Casedev) -> None:
        project = client.applications.v1.projects.delete(
            id="id",
            delete_from_hosting=True,
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.applications.v1.projects.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.applications.v1.projects.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.projects.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_deployment(self, client: Casedev) -> None:
        project = client.applications.v1.projects.create_deployment(
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_deployment_with_all_params(self, client: Casedev) -> None:
        project = client.applications.v1.projects.create_deployment(
            id="id",
            environment_variables=[
                {
                    "key": "key",
                    "target": ["production"],
                    "value": "value",
                    "type": "plain",
                }
            ],
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_deployment(self, client: Casedev) -> None:
        response = client.applications.v1.projects.with_raw_response.create_deployment(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_deployment(self, client: Casedev) -> None:
        with client.applications.v1.projects.with_streaming_response.create_deployment(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_deployment(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.projects.with_raw_response.create_deployment(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_domain(self, client: Casedev) -> None:
        project = client.applications.v1.projects.create_domain(
            id="id",
            domain="domain",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_domain_with_all_params(self, client: Casedev) -> None:
        project = client.applications.v1.projects.create_domain(
            id="id",
            domain="domain",
            git_branch="gitBranch",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_domain(self, client: Casedev) -> None:
        response = client.applications.v1.projects.with_raw_response.create_domain(
            id="id",
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_domain(self, client: Casedev) -> None:
        with client.applications.v1.projects.with_streaming_response.create_domain(
            id="id",
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_domain(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.projects.with_raw_response.create_domain(
                id="",
                domain="domain",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_env(self, client: Casedev) -> None:
        project = client.applications.v1.projects.create_env(
            id="id",
            key="key",
            target=["production"],
            value="value",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_env_with_all_params(self, client: Casedev) -> None:
        project = client.applications.v1.projects.create_env(
            id="id",
            key="key",
            target=["production"],
            value="value",
            git_branch="gitBranch",
            type="plain",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_env(self, client: Casedev) -> None:
        response = client.applications.v1.projects.with_raw_response.create_env(
            id="id",
            key="key",
            target=["production"],
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_env(self, client: Casedev) -> None:
        with client.applications.v1.projects.with_streaming_response.create_env(
            id="id",
            key="key",
            target=["production"],
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_env(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.projects.with_raw_response.create_env(
                id="",
                key="key",
                target=["production"],
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_domain(self, client: Casedev) -> None:
        project = client.applications.v1.projects.delete_domain(
            domain="domain",
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_domain(self, client: Casedev) -> None:
        response = client.applications.v1.projects.with_raw_response.delete_domain(
            domain="domain",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_domain(self, client: Casedev) -> None:
        with client.applications.v1.projects.with_streaming_response.delete_domain(
            domain="domain",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_domain(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.projects.with_raw_response.delete_domain(
                domain="domain",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            client.applications.v1.projects.with_raw_response.delete_domain(
                domain="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_env(self, client: Casedev) -> None:
        project = client.applications.v1.projects.delete_env(
            env_id="envId",
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_env(self, client: Casedev) -> None:
        response = client.applications.v1.projects.with_raw_response.delete_env(
            env_id="envId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_env(self, client: Casedev) -> None:
        with client.applications.v1.projects.with_streaming_response.delete_env(
            env_id="envId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_env(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.projects.with_raw_response.delete_env(
                env_id="envId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_id` but received ''"):
            client.applications.v1.projects.with_raw_response.delete_env(
                env_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_runtime_logs(self, client: Casedev) -> None:
        project = client.applications.v1.projects.get_runtime_logs(
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_runtime_logs_with_all_params(self, client: Casedev) -> None:
        project = client.applications.v1.projects.get_runtime_logs(
            id="id",
            limit=0,
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_runtime_logs(self, client: Casedev) -> None:
        response = client.applications.v1.projects.with_raw_response.get_runtime_logs(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_runtime_logs(self, client: Casedev) -> None:
        with client.applications.v1.projects.with_streaming_response.get_runtime_logs(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_runtime_logs(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.projects.with_raw_response.get_runtime_logs(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_deployments(self, client: Casedev) -> None:
        project = client.applications.v1.projects.list_deployments(
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_deployments_with_all_params(self, client: Casedev) -> None:
        project = client.applications.v1.projects.list_deployments(
            id="id",
            limit=0,
            state="state",
            target="production",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_deployments(self, client: Casedev) -> None:
        response = client.applications.v1.projects.with_raw_response.list_deployments(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_deployments(self, client: Casedev) -> None:
        with client.applications.v1.projects.with_streaming_response.list_deployments(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_deployments(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.projects.with_raw_response.list_deployments(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_domains(self, client: Casedev) -> None:
        project = client.applications.v1.projects.list_domains(
            "id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_domains(self, client: Casedev) -> None:
        response = client.applications.v1.projects.with_raw_response.list_domains(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_domains(self, client: Casedev) -> None:
        with client.applications.v1.projects.with_streaming_response.list_domains(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_domains(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.projects.with_raw_response.list_domains(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_env(self, client: Casedev) -> None:
        project = client.applications.v1.projects.list_env(
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_env_with_all_params(self, client: Casedev) -> None:
        project = client.applications.v1.projects.list_env(
            id="id",
            decrypt=True,
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_env(self, client: Casedev) -> None:
        response = client.applications.v1.projects.with_raw_response.list_env(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_env(self, client: Casedev) -> None:
        with client.applications.v1.projects.with_streaming_response.list_env(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_env(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.projects.with_raw_response.list_env(
                id="",
            )


class TestAsyncProjects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.create(
            git_repo="gitRepo",
            name="name",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.create(
            git_repo="gitRepo",
            name="name",
            build_command="buildCommand",
            environment_variables=[
                {
                    "key": "key",
                    "target": ["production"],
                    "value": "value",
                    "type": "plain",
                }
            ],
            framework="framework",
            git_branch="gitBranch",
            install_command="installCommand",
            output_directory="outputDirectory",
            root_directory="rootDirectory",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.projects.with_raw_response.create(
            git_repo="gitRepo",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.projects.with_streaming_response.create(
            git_repo="gitRepo",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.retrieve(
            "id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.projects.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.projects.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.projects.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.list()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.projects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.projects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.delete(
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.delete(
            id="id",
            delete_from_hosting=True,
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.projects.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.projects.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.projects.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_deployment(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.create_deployment(
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_deployment_with_all_params(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.create_deployment(
            id="id",
            environment_variables=[
                {
                    "key": "key",
                    "target": ["production"],
                    "value": "value",
                    "type": "plain",
                }
            ],
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_deployment(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.projects.with_raw_response.create_deployment(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_deployment(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.projects.with_streaming_response.create_deployment(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_deployment(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.projects.with_raw_response.create_deployment(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_domain(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.create_domain(
            id="id",
            domain="domain",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_domain_with_all_params(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.create_domain(
            id="id",
            domain="domain",
            git_branch="gitBranch",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_domain(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.projects.with_raw_response.create_domain(
            id="id",
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_domain(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.projects.with_streaming_response.create_domain(
            id="id",
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_domain(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.projects.with_raw_response.create_domain(
                id="",
                domain="domain",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_env(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.create_env(
            id="id",
            key="key",
            target=["production"],
            value="value",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_env_with_all_params(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.create_env(
            id="id",
            key="key",
            target=["production"],
            value="value",
            git_branch="gitBranch",
            type="plain",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_env(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.projects.with_raw_response.create_env(
            id="id",
            key="key",
            target=["production"],
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_env(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.projects.with_streaming_response.create_env(
            id="id",
            key="key",
            target=["production"],
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_env(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.projects.with_raw_response.create_env(
                id="",
                key="key",
                target=["production"],
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_domain(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.delete_domain(
            domain="domain",
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_domain(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.projects.with_raw_response.delete_domain(
            domain="domain",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_domain(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.projects.with_streaming_response.delete_domain(
            domain="domain",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_domain(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.projects.with_raw_response.delete_domain(
                domain="domain",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            await async_client.applications.v1.projects.with_raw_response.delete_domain(
                domain="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_env(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.delete_env(
            env_id="envId",
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_env(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.projects.with_raw_response.delete_env(
            env_id="envId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_env(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.projects.with_streaming_response.delete_env(
            env_id="envId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_env(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.projects.with_raw_response.delete_env(
                env_id="envId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_id` but received ''"):
            await async_client.applications.v1.projects.with_raw_response.delete_env(
                env_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_runtime_logs(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.get_runtime_logs(
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_runtime_logs_with_all_params(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.get_runtime_logs(
            id="id",
            limit=0,
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_runtime_logs(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.projects.with_raw_response.get_runtime_logs(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_runtime_logs(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.projects.with_streaming_response.get_runtime_logs(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_runtime_logs(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.projects.with_raw_response.get_runtime_logs(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_deployments(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.list_deployments(
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_deployments_with_all_params(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.list_deployments(
            id="id",
            limit=0,
            state="state",
            target="production",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_deployments(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.projects.with_raw_response.list_deployments(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_deployments(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.projects.with_streaming_response.list_deployments(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_deployments(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.projects.with_raw_response.list_deployments(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_domains(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.list_domains(
            "id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_domains(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.projects.with_raw_response.list_domains(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_domains(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.projects.with_streaming_response.list_domains(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_domains(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.projects.with_raw_response.list_domains(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_env(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.list_env(
            id="id",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_env_with_all_params(self, async_client: AsyncCasedev) -> None:
        project = await async_client.applications.v1.projects.list_env(
            id="id",
            decrypt=True,
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_env(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.projects.with_raw_response.list_env(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_env(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.projects.with_streaming_response.list_env(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_env(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.projects.with_raw_response.list_env(
                id="",
            )
