# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEventTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        event_type = client.webhooks.v1.event_types.list()
        assert event_type is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.webhooks.v1.event_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_type = response.parse()
        assert event_type is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.webhooks.v1.event_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_type = response.parse()
            assert event_type is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEventTypes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        event_type = await async_client.webhooks.v1.event_types.list()
        assert event_type is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.webhooks.v1.event_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_type = await response.parse()
        assert event_type is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.webhooks.v1.event_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_type = await response.parse()
            assert event_type is None

        assert cast(Any, response.is_closed) is True
