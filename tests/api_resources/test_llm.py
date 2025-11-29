# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedotdev_sdk_py import Casemark, AsyncCasemark

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLlm:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_config(self, client: Casemark) -> None:
        llm = client.llm.retrieve_config()
        assert llm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_config(self, client: Casemark) -> None:
        response = client.llm.with_raw_response.retrieve_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert llm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_config(self, client: Casemark) -> None:
        with client.llm.with_streaming_response.retrieve_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert llm is None

        assert cast(Any, response.is_closed) is True


class TestAsyncLlm:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_config(self, async_client: AsyncCasemark) -> None:
        llm = await async_client.llm.retrieve_config()
        assert llm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_config(self, async_client: AsyncCasemark) -> None:
        response = await async_client.llm.with_raw_response.retrieve_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert llm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_config(self, async_client: AsyncCasemark) -> None:
        async with async_client.llm.with_streaming_response.retrieve_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert llm is None

        assert cast(Any, response.is_closed) is True
