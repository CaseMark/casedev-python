# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeliveries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        delivery = client.webhooks.v1.deliveries.retrieve(
            "id",
        )
        assert delivery is None

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.webhooks.v1.deliveries.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert delivery is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.webhooks.v1.deliveries.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert delivery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.v1.deliveries.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        delivery = client.webhooks.v1.deliveries.list()
        assert delivery is None

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        delivery = client.webhooks.v1.deliveries.list(
            endpoint_id="endpoint_id",
            limit=1,
            status="pending",
        )
        assert delivery is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.webhooks.v1.deliveries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert delivery is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.webhooks.v1.deliveries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert delivery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replay(self, client: Casedev) -> None:
        delivery = client.webhooks.v1.deliveries.replay(
            id="id",
        )
        assert delivery is None

    @parametrize
    def test_method_replay_with_all_params(self, client: Casedev) -> None:
        delivery = client.webhooks.v1.deliveries.replay(
            id="id",
            payload={},
        )
        assert delivery is None

    @parametrize
    def test_raw_response_replay(self, client: Casedev) -> None:
        response = client.webhooks.v1.deliveries.with_raw_response.replay(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert delivery is None

    @parametrize
    def test_streaming_response_replay(self, client: Casedev) -> None:
        with client.webhooks.v1.deliveries.with_streaming_response.replay(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert delivery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replay(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.v1.deliveries.with_raw_response.replay(
                id="",
            )


class TestAsyncDeliveries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        delivery = await async_client.webhooks.v1.deliveries.retrieve(
            "id",
        )
        assert delivery is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.webhooks.v1.deliveries.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert delivery is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.webhooks.v1.deliveries.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert delivery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.v1.deliveries.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        delivery = await async_client.webhooks.v1.deliveries.list()
        assert delivery is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        delivery = await async_client.webhooks.v1.deliveries.list(
            endpoint_id="endpoint_id",
            limit=1,
            status="pending",
        )
        assert delivery is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.webhooks.v1.deliveries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert delivery is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.webhooks.v1.deliveries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert delivery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replay(self, async_client: AsyncCasedev) -> None:
        delivery = await async_client.webhooks.v1.deliveries.replay(
            id="id",
        )
        assert delivery is None

    @parametrize
    async def test_method_replay_with_all_params(self, async_client: AsyncCasedev) -> None:
        delivery = await async_client.webhooks.v1.deliveries.replay(
            id="id",
            payload={},
        )
        assert delivery is None

    @parametrize
    async def test_raw_response_replay(self, async_client: AsyncCasedev) -> None:
        response = await async_client.webhooks.v1.deliveries.with_raw_response.replay(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert delivery is None

    @parametrize
    async def test_streaming_response_replay(self, async_client: AsyncCasedev) -> None:
        async with async_client.webhooks.v1.deliveries.with_streaming_response.replay(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert delivery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replay(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.v1.deliveries.with_raw_response.replay(
                id="",
            )
