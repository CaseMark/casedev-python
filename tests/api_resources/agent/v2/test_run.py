# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.agent.v2 import (
    RunExecResponse,
    RunCreateResponse,
    RunGetStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRun:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        run = client.agent.v2.run.create(
            agent_id="agentId",
            prompt="prompt",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        run = client.agent.v2.run.create(
            agent_id="agentId",
            prompt="prompt",
            callback_url="https://example.com",
            guidance="guidance",
            model="model",
            object_ids=["string"],
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.agent.v2.run.with_raw_response.create(
            agent_id="agentId",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.agent.v2.run.with_streaming_response.create(
            agent_id="agentId",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_events(self, client: Casedev) -> None:
        run_stream = client.agent.v2.run.events(
            id="id",
        )
        run_stream.response.close()

    @parametrize
    def test_method_events_with_all_params(self, client: Casedev) -> None:
        run_stream = client.agent.v2.run.events(
            id="id",
            last_event_id=0,
        )
        run_stream.response.close()

    @parametrize
    def test_raw_response_events(self, client: Casedev) -> None:
        response = client.agent.v2.run.with_raw_response.events(
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_events(self, client: Casedev) -> None:
        with client.agent.v2.run.with_streaming_response.events(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_events(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.v2.run.with_raw_response.events(
                id="",
            )

    @parametrize
    def test_method_exec(self, client: Casedev) -> None:
        run = client.agent.v2.run.exec(
            "id",
        )
        assert_matches_type(RunExecResponse, run, path=["response"])

    @parametrize
    def test_raw_response_exec(self, client: Casedev) -> None:
        response = client.agent.v2.run.with_raw_response.exec(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunExecResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_exec(self, client: Casedev) -> None:
        with client.agent.v2.run.with_streaming_response.exec(
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
            client.agent.v2.run.with_raw_response.exec(
                "",
            )

    @parametrize
    def test_method_get_details(self, client: Casedev) -> None:
        run = client.agent.v2.run.get_details(
            "id",
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_raw_response_get_details(self, client: Casedev) -> None:
        response = client.agent.v2.run.with_raw_response.get_details(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_streaming_response_get_details(self, client: Casedev) -> None:
        with client.agent.v2.run.with_streaming_response.get_details(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_details(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.v2.run.with_raw_response.get_details(
                "",
            )

    @parametrize
    def test_method_get_status(self, client: Casedev) -> None:
        run = client.agent.v2.run.get_status(
            "id",
        )
        assert_matches_type(RunGetStatusResponse, run, path=["response"])

    @parametrize
    def test_raw_response_get_status(self, client: Casedev) -> None:
        response = client.agent.v2.run.with_raw_response.get_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunGetStatusResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_get_status(self, client: Casedev) -> None:
        with client.agent.v2.run.with_streaming_response.get_status(
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
            client.agent.v2.run.with_raw_response.get_status(
                "",
            )


class TestAsyncRun:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        run = await async_client.agent.v2.run.create(
            agent_id="agentId",
            prompt="prompt",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        run = await async_client.agent.v2.run.create(
            agent_id="agentId",
            prompt="prompt",
            callback_url="https://example.com",
            guidance="guidance",
            model="model",
            object_ids=["string"],
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v2.run.with_raw_response.create(
            agent_id="agentId",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v2.run.with_streaming_response.create(
            agent_id="agentId",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_events(self, async_client: AsyncCasedev) -> None:
        run_stream = await async_client.agent.v2.run.events(
            id="id",
        )
        await run_stream.response.aclose()

    @parametrize
    async def test_method_events_with_all_params(self, async_client: AsyncCasedev) -> None:
        run_stream = await async_client.agent.v2.run.events(
            id="id",
            last_event_id=0,
        )
        await run_stream.response.aclose()

    @parametrize
    async def test_raw_response_events(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v2.run.with_raw_response.events(
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_events(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v2.run.with_streaming_response.events(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_events(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.v2.run.with_raw_response.events(
                id="",
            )

    @parametrize
    async def test_method_exec(self, async_client: AsyncCasedev) -> None:
        run = await async_client.agent.v2.run.exec(
            "id",
        )
        assert_matches_type(RunExecResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_exec(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v2.run.with_raw_response.exec(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunExecResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_exec(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v2.run.with_streaming_response.exec(
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
            await async_client.agent.v2.run.with_raw_response.exec(
                "",
            )

    @parametrize
    async def test_method_get_details(self, async_client: AsyncCasedev) -> None:
        run = await async_client.agent.v2.run.get_details(
            "id",
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_raw_response_get_details(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v2.run.with_raw_response.get_details(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_streaming_response_get_details(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v2.run.with_streaming_response.get_details(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_details(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.v2.run.with_raw_response.get_details(
                "",
            )

    @parametrize
    async def test_method_get_status(self, async_client: AsyncCasedev) -> None:
        run = await async_client.agent.v2.run.get_status(
            "id",
        )
        assert_matches_type(RunGetStatusResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v2.run.with_raw_response.get_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunGetStatusResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v2.run.with_streaming_response.get_status(
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
            await async_client.agent.v2.run.with_raw_response.get_status(
                "",
            )
