# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.agent.v2 import ExecuteCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecute:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        execute = client.agent.v2.execute.create(
            prompt="prompt",
        )
        assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        execute = client.agent.v2.execute.create(
            prompt="prompt",
            agent_runtime=True,
            disabled_tools=["string"],
            enabled_tools=["string"],
            guidance="guidance",
            instructions="instructions",
            model="model",
            object_ids=["string"],
            sandbox={
                "cpu": 0,
                "memory_mi_b": 0,
            },
            vault_ids=["string"],
        )
        assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.agent.v2.execute.with_raw_response.create(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execute = response.parse()
        assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.agent.v2.execute.with_streaming_response.create(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execute = response.parse()
            assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExecute:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        execute = await async_client.agent.v2.execute.create(
            prompt="prompt",
        )
        assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        execute = await async_client.agent.v2.execute.create(
            prompt="prompt",
            agent_runtime=True,
            disabled_tools=["string"],
            enabled_tools=["string"],
            guidance="guidance",
            instructions="instructions",
            model="model",
            object_ids=["string"],
            sandbox={
                "cpu": 0,
                "memory_mi_b": 0,
            },
            vault_ids=["string"],
        )
        assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v2.execute.with_raw_response.create(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execute = await response.parse()
        assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v2.execute.with_streaming_response.create(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execute = await response.parse()
            assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

        assert cast(Any, response.is_closed) is True
