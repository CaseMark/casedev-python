# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.agent.v1 import (
    RunExecResponse,
    RunWatchResponse,
    RunCancelResponse,
    RunCreateResponse,
    RunGetStatusResponse,
    RunGetDetailsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRun:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        run = client.agent.v1.run.create(
            agent_id="agentId",
            prompt="prompt",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        run = client.agent.v1.run.create(
            agent_id="agentId",
            prompt="prompt",
            guidance="guidance",
            model="model",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.agent.v1.run.with_raw_response.create(
            agent_id="agentId",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.agent.v1.run.with_streaming_response.create(
            agent_id="agentId",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Casedev) -> None:
        run = client.agent.v1.run.cancel(
            "id",
        )
        assert_matches_type(RunCancelResponse, run, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Casedev) -> None:
        response = client.agent.v1.run.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunCancelResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Casedev) -> None:
        with client.agent.v1.run.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunCancelResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.v1.run.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_exec(self, client: Casedev) -> None:
        run = client.agent.v1.run.exec(
            "id",
        )
        assert_matches_type(RunExecResponse, run, path=["response"])

    @parametrize
    def test_raw_response_exec(self, client: Casedev) -> None:
        response = client.agent.v1.run.with_raw_response.exec(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunExecResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_exec(self, client: Casedev) -> None:
        with client.agent.v1.run.with_streaming_response.exec(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunExecResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_exec(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.v1.run.with_raw_response.exec(
                "",
            )

    @parametrize
    def test_method_get_details(self, client: Casedev) -> None:
        run = client.agent.v1.run.get_details(
            "id",
        )
        assert_matches_type(RunGetDetailsResponse, run, path=["response"])

    @parametrize
    def test_raw_response_get_details(self, client: Casedev) -> None:
        response = client.agent.v1.run.with_raw_response.get_details(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetDetailsResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_get_details(self, client: Casedev) -> None:
        with client.agent.v1.run.with_streaming_response.get_details(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunGetDetailsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_details(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.v1.run.with_raw_response.get_details(
                "",
            )

    @parametrize
    def test_method_get_status(self, client: Casedev) -> None:
        run = client.agent.v1.run.get_status(
            "id",
        )
        assert_matches_type(RunGetStatusResponse, run, path=["response"])

    @parametrize
    def test_raw_response_get_status(self, client: Casedev) -> None:
        response = client.agent.v1.run.with_raw_response.get_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetStatusResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_get_status(self, client: Casedev) -> None:
        with client.agent.v1.run.with_streaming_response.get_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunGetStatusResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_status(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.v1.run.with_raw_response.get_status(
                "",
            )

    @parametrize
    def test_method_watch(self, client: Casedev) -> None:
        run = client.agent.v1.run.watch(
            id="id",
            callback_url="https://example.com",
        )
        assert_matches_type(RunWatchResponse, run, path=["response"])

    @parametrize
    def test_raw_response_watch(self, client: Casedev) -> None:
        response = client.agent.v1.run.with_raw_response.watch(
            id="id",
            callback_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunWatchResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_watch(self, client: Casedev) -> None:
        with client.agent.v1.run.with_streaming_response.watch(
            id="id",
            callback_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunWatchResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_watch(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.v1.run.with_raw_response.watch(
                id="",
                callback_url="https://example.com",
            )


class TestAsyncRun:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        run = await async_client.agent.v1.run.create(
            agent_id="agentId",
            prompt="prompt",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        run = await async_client.agent.v1.run.create(
            agent_id="agentId",
            prompt="prompt",
            guidance="guidance",
            model="model",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v1.run.with_raw_response.create(
            agent_id="agentId",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v1.run.with_streaming_response.create(
            agent_id="agentId",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncCasedev) -> None:
        run = await async_client.agent.v1.run.cancel(
            "id",
        )
        assert_matches_type(RunCancelResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v1.run.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunCancelResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v1.run.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunCancelResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.v1.run.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_exec(self, async_client: AsyncCasedev) -> None:
        run = await async_client.agent.v1.run.exec(
            "id",
        )
        assert_matches_type(RunExecResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_exec(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v1.run.with_raw_response.exec(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunExecResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_exec(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v1.run.with_streaming_response.exec(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunExecResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_exec(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.v1.run.with_raw_response.exec(
                "",
            )

    @parametrize
    async def test_method_get_details(self, async_client: AsyncCasedev) -> None:
        run = await async_client.agent.v1.run.get_details(
            "id",
        )
        assert_matches_type(RunGetDetailsResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_get_details(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v1.run.with_raw_response.get_details(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetDetailsResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_get_details(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v1.run.with_streaming_response.get_details(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunGetDetailsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_details(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.v1.run.with_raw_response.get_details(
                "",
            )

    @parametrize
    async def test_method_get_status(self, async_client: AsyncCasedev) -> None:
        run = await async_client.agent.v1.run.get_status(
            "id",
        )
        assert_matches_type(RunGetStatusResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v1.run.with_raw_response.get_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetStatusResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v1.run.with_streaming_response.get_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunGetStatusResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.v1.run.with_raw_response.get_status(
                "",
            )

    @parametrize
    async def test_method_watch(self, async_client: AsyncCasedev) -> None:
        run = await async_client.agent.v1.run.watch(
            id="id",
            callback_url="https://example.com",
        )
        assert_matches_type(RunWatchResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_watch(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v1.run.with_raw_response.watch(
            id="id",
            callback_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunWatchResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_watch(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v1.run.with_streaming_response.watch(
            id="id",
            callback_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunWatchResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_watch(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.v1.run.with_raw_response.watch(
                id="",
                callback_url="https://example.com",
            )
