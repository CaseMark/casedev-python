# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgentTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        agent_type = client.matters.v1.agent_types.create(
            instructions="instructions",
            name="name",
        )
        assert agent_type is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        agent_type = client.matters.v1.agent_types.create(
            instructions="instructions",
            name="name",
            description="description",
            disabled_tools=["string"],
            enabled_tools=["string"],
            is_active=True,
            is_default=True,
            metadata={"foo": "bar"},
            model="model",
            skill_refs=["string"],
            slug="slug",
        )
        assert agent_type is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.matters.v1.agent_types.with_raw_response.create(
            instructions="instructions",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_type = response.parse()
        assert agent_type is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.matters.v1.agent_types.with_streaming_response.create(
            instructions="instructions",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_type = response.parse()
            assert agent_type is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        agent_type = client.matters.v1.agent_types.list()
        assert agent_type is None

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        agent_type = client.matters.v1.agent_types.list(
            active=True,
        )
        assert agent_type is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.matters.v1.agent_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_type = response.parse()
        assert agent_type is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.matters.v1.agent_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_type = response.parse()
            assert agent_type is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAgentTypes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        agent_type = await async_client.matters.v1.agent_types.create(
            instructions="instructions",
            name="name",
        )
        assert agent_type is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        agent_type = await async_client.matters.v1.agent_types.create(
            instructions="instructions",
            name="name",
            description="description",
            disabled_tools=["string"],
            enabled_tools=["string"],
            is_active=True,
            is_default=True,
            metadata={"foo": "bar"},
            model="model",
            skill_refs=["string"],
            slug="slug",
        )
        assert agent_type is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.agent_types.with_raw_response.create(
            instructions="instructions",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_type = await response.parse()
        assert agent_type is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.agent_types.with_streaming_response.create(
            instructions="instructions",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_type = await response.parse()
            assert agent_type is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        agent_type = await async_client.matters.v1.agent_types.list()
        assert agent_type is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        agent_type = await async_client.matters.v1.agent_types.list(
            active=True,
        )
        assert agent_type is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.agent_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_type = await response.parse()
        assert agent_type is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.agent_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_type = await response.parse()
            assert agent_type is None

        assert cast(Any, response.is_closed) is True
