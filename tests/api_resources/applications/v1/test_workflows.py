# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_status(self, client: Casedev) -> None:
        workflow = client.applications.v1.workflows.get_status(
            id="id",
            project_id="projectId",
        )
        assert workflow is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: Casedev) -> None:
        response = client.applications.v1.workflows.with_raw_response.get_status(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert workflow is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: Casedev) -> None:
        with client.applications.v1.workflows.with_streaming_response.get_status(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.applications.v1.workflows.with_raw_response.get_status(
                id="",
                project_id="projectId",
            )


class TestAsyncWorkflows:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncCasedev) -> None:
        workflow = await async_client.applications.v1.workflows.get_status(
            id="id",
            project_id="projectId",
        )
        assert workflow is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncCasedev) -> None:
        response = await async_client.applications.v1.workflows.with_raw_response.get_status(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert workflow is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncCasedev) -> None:
        async with async_client.applications.v1.workflows.with_streaming_response.get_status(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.applications.v1.workflows.with_raw_response.get_status(
                id="",
                project_id="projectId",
            )
