# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeployments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        deployment = client.applications.v1.deployments.create(
            project_id="projectId",
        )
        assert deployment is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        deployment = client.applications.v1.deployments.create(
            project_id="projectId",
            ref="ref",
            target="production",
        )
        assert deployment is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.applications.v1.deployments.with_raw_response.create(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert deployment is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.applications.v1.deployments.with_streaming_response.create(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        deployment = client.applications.v1.deployments.retrieve(
            id="id",
            project_id="projectId",
        )
        assert deployment is None

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Casedev) -> None:
        deployment = client.applications.v1.deployments.retrieve(
            id="id",
            project_id="projectId",
            include_logs=True,
        )
        assert deployment is None

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.applications.v1.deployments.with_raw_response.retrieve(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert deployment is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.applications.v1.deployments.with_streaming_response.retrieve(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.deployments.with_raw_response.retrieve(
                id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        deployment = client.applications.v1.deployments.list(
            project_id="projectId",
        )
        assert deployment is None

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        deployment = client.applications.v1.deployments.list(
            project_id="projectId",
            limit=0,
            state="state",
            target="production",
        )
        assert deployment is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.applications.v1.deployments.with_raw_response.list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert deployment is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.applications.v1.deployments.with_streaming_response.list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Casedev) -> None:
        deployment = client.applications.v1.deployments.cancel(
            id="id",
            project_id="projectId",
        )
        assert deployment is None

    @parametrize
    def test_raw_response_cancel(self, client: Casedev) -> None:
        response = client.applications.v1.deployments.with_raw_response.cancel(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert deployment is None

    @parametrize
    def test_streaming_response_cancel(self, client: Casedev) -> None:
        with client.applications.v1.deployments.with_streaming_response.cancel(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.deployments.with_raw_response.cancel(
                id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_create_from_files(self, client: Casedev) -> None:
        deployment = client.applications.v1.deployments.create_from_files()
        assert deployment is None

    @parametrize
    def test_raw_response_create_from_files(self, client: Casedev) -> None:
        response = client.applications.v1.deployments.with_raw_response.create_from_files()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert deployment is None

    @parametrize
    def test_streaming_response_create_from_files(self, client: Casedev) -> None:
        with client.applications.v1.deployments.with_streaming_response.create_from_files() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_logs(self, client: Casedev) -> None:
        deployment = client.applications.v1.deployments.get_logs(
            id="id",
            project_id="projectId",
        )
        assert deployment is None

    @parametrize
    def test_raw_response_get_logs(self, client: Casedev) -> None:
        response = client.applications.v1.deployments.with_raw_response.get_logs(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert deployment is None

    @parametrize
    def test_streaming_response_get_logs(self, client: Casedev) -> None:
        with client.applications.v1.deployments.with_streaming_response.get_logs(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_logs(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.deployments.with_raw_response.get_logs(
                id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_get_status(self, client: Casedev) -> None:
        deployment = client.applications.v1.deployments.get_status(
            "id",
        )
        assert deployment is None

    @parametrize
    def test_raw_response_get_status(self, client: Casedev) -> None:
        response = client.applications.v1.deployments.with_raw_response.get_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert deployment is None

    @parametrize
    def test_streaming_response_get_status(self, client: Casedev) -> None:
        with client.applications.v1.deployments.with_streaming_response.get_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_status(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.deployments.with_raw_response.get_status(
                "",
            )

    @parametrize
    def test_method_stream(self, client: Casedev) -> None:
        deployment = client.applications.v1.deployments.stream(
            id="id",
            project_id="projectId",
        )
        assert deployment is None

    @parametrize
    def test_method_stream_with_all_params(self, client: Casedev) -> None:
        deployment = client.applications.v1.deployments.stream(
            id="id",
            project_id="projectId",
            start_index=0,
        )
        assert deployment is None

    @parametrize
    def test_raw_response_stream(self, client: Casedev) -> None:
        response = client.applications.v1.deployments.with_raw_response.stream(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert deployment is None

    @parametrize
    def test_streaming_response_stream(self, client: Casedev) -> None:
        with client.applications.v1.deployments.with_streaming_response.stream(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stream(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.deployments.with_raw_response.stream(
                id="",
                project_id="projectId",
            )


class TestAsyncDeployments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        deployment = await async_client.applications.v1.deployments.create(
            project_id="projectId",
        )
        assert deployment is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        deployment = await async_client.applications.v1.deployments.create(
            project_id="projectId",
            ref="ref",
            target="production",
        )
        assert deployment is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.deployments.with_raw_response.create(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert deployment is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.deployments.with_streaming_response.create(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        deployment = await async_client.applications.v1.deployments.retrieve(
            id="id",
            project_id="projectId",
        )
        assert deployment is None

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCasedev) -> None:
        deployment = await async_client.applications.v1.deployments.retrieve(
            id="id",
            project_id="projectId",
            include_logs=True,
        )
        assert deployment is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.deployments.with_raw_response.retrieve(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert deployment is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.deployments.with_streaming_response.retrieve(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.deployments.with_raw_response.retrieve(
                id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        deployment = await async_client.applications.v1.deployments.list(
            project_id="projectId",
        )
        assert deployment is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        deployment = await async_client.applications.v1.deployments.list(
            project_id="projectId",
            limit=0,
            state="state",
            target="production",
        )
        assert deployment is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.deployments.with_raw_response.list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert deployment is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.deployments.with_streaming_response.list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncCasedev) -> None:
        deployment = await async_client.applications.v1.deployments.cancel(
            id="id",
            project_id="projectId",
        )
        assert deployment is None

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.deployments.with_raw_response.cancel(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert deployment is None

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.deployments.with_streaming_response.cancel(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.deployments.with_raw_response.cancel(
                id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_create_from_files(self, async_client: AsyncCasedev) -> None:
        deployment = await async_client.applications.v1.deployments.create_from_files()
        assert deployment is None

    @parametrize
    async def test_raw_response_create_from_files(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.deployments.with_raw_response.create_from_files()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert deployment is None

    @parametrize
    async def test_streaming_response_create_from_files(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.deployments.with_streaming_response.create_from_files() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_logs(self, async_client: AsyncCasedev) -> None:
        deployment = await async_client.applications.v1.deployments.get_logs(
            id="id",
            project_id="projectId",
        )
        assert deployment is None

    @parametrize
    async def test_raw_response_get_logs(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.deployments.with_raw_response.get_logs(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert deployment is None

    @parametrize
    async def test_streaming_response_get_logs(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.deployments.with_streaming_response.get_logs(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_logs(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.deployments.with_raw_response.get_logs(
                id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_get_status(self, async_client: AsyncCasedev) -> None:
        deployment = await async_client.applications.v1.deployments.get_status(
            "id",
        )
        assert deployment is None

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.deployments.with_raw_response.get_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert deployment is None

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.deployments.with_streaming_response.get_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.deployments.with_raw_response.get_status(
                "",
            )

    @parametrize
    async def test_method_stream(self, async_client: AsyncCasedev) -> None:
        deployment = await async_client.applications.v1.deployments.stream(
            id="id",
            project_id="projectId",
        )
        assert deployment is None

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncCasedev) -> None:
        deployment = await async_client.applications.v1.deployments.stream(
            id="id",
            project_id="projectId",
            start_index=0,
        )
        assert deployment is None

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.deployments.with_raw_response.stream(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert deployment is None

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.deployments.with_streaming_response.stream(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stream(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.deployments.with_raw_response.stream(
                id="",
                project_id="projectId",
            )
