# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        v1 = client.operator.v1.create(
            name="name",
        )
        assert v1 is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        v1 = client.operator.v1.create(
            name="name",
            model="model",
            size="small",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.operator.v1.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.operator.v1.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_chat_completion(self, client: Casedev) -> None:
        v1 = client.operator.v1.create_chat_completion()
        assert v1 is None

    @parametrize
    def test_raw_response_create_chat_completion(self, client: Casedev) -> None:
        response = client.operator.v1.with_raw_response.create_chat_completion()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_create_chat_completion(self, client: Casedev) -> None:
        with client.operator.v1.with_streaming_response.create_chat_completion() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_response(self, client: Casedev) -> None:
        v1 = client.operator.v1.create_response()
        assert v1 is None

    @parametrize
    def test_raw_response_create_response(self, client: Casedev) -> None:
        response = client.operator.v1.with_raw_response.create_response()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_create_response(self, client: Casedev) -> None:
        with client.operator.v1.with_streaming_response.create_response() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_status(self, client: Casedev) -> None:
        v1 = client.operator.v1.get_status()
        assert v1 is None

    @parametrize
    def test_raw_response_get_status(self, client: Casedev) -> None:
        response = client.operator.v1.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_get_status(self, client: Casedev) -> None:
        with client.operator.v1.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.operator.v1.create(
            name="name",
        )
        assert v1 is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.operator.v1.create(
            name="name",
            model="model",
            size="small",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.operator.v1.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.operator.v1.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_chat_completion(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.operator.v1.create_chat_completion()
        assert v1 is None

    @parametrize
    async def test_raw_response_create_chat_completion(self, async_client: AsyncCasedev) -> None:
        response = await async_client.operator.v1.with_raw_response.create_chat_completion()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_create_chat_completion(self, async_client: AsyncCasedev) -> None:
        async with async_client.operator.v1.with_streaming_response.create_chat_completion() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_response(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.operator.v1.create_response()
        assert v1 is None

    @parametrize
    async def test_raw_response_create_response(self, async_client: AsyncCasedev) -> None:
        response = await async_client.operator.v1.with_raw_response.create_response()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_create_response(self, async_client: AsyncCasedev) -> None:
        async with async_client.operator.v1.with_streaming_response.create_response() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_status(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.operator.v1.get_status()
        assert v1 is None

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncCasedev) -> None:
        response = await async_client.operator.v1.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncCasedev) -> None:
        async with async_client.operator.v1.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True
