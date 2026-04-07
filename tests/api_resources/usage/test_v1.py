# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from casedev._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        v1 = client.usage.v1.retrieve()
        assert v1 is None

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Casedev) -> None:
        v1 = client.usage.v1.retrieve(
            granularity="summary",
            period_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            period_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert v1 is None

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.usage.v1.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.usage.v1.with_streaming_response.retrieve() as response:
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
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.usage.v1.retrieve()
        assert v1 is None

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.usage.v1.retrieve(
            granularity="summary",
            period_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            period_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.usage.v1.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.usage.v1.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True
