# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from casedotdev_sdk_py import Casemark, AsyncCasemark

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpeak:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Casemark) -> None:
        speak = client.voice.v1.speak.create(
            body={},
        )
        assert_matches_type(object, speak, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Casemark) -> None:
        response = client.voice.v1.speak.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speak = response.parse()
        assert_matches_type(object, speak, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Casemark) -> None:
        with client.voice.v1.speak.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speak = response.parse()
            assert_matches_type(object, speak, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream(self, client: Casemark) -> None:
        speak = client.voice.v1.speak.stream(
            body={},
        )
        assert_matches_type(object, speak, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stream(self, client: Casemark) -> None:
        response = client.voice.v1.speak.with_raw_response.stream(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speak = response.parse()
        assert_matches_type(object, speak, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stream(self, client: Casemark) -> None:
        with client.voice.v1.speak.with_streaming_response.stream(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speak = response.parse()
            assert_matches_type(object, speak, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSpeak:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCasemark) -> None:
        speak = await async_client.voice.v1.speak.create(
            body={},
        )
        assert_matches_type(object, speak, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasemark) -> None:
        response = await async_client.voice.v1.speak.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speak = await response.parse()
        assert_matches_type(object, speak, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasemark) -> None:
        async with async_client.voice.v1.speak.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speak = await response.parse()
            assert_matches_type(object, speak, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream(self, async_client: AsyncCasemark) -> None:
        speak = await async_client.voice.v1.speak.stream(
            body={},
        )
        assert_matches_type(object, speak, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncCasemark) -> None:
        response = await async_client.voice.v1.speak.with_raw_response.stream(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speak = await response.parse()
        assert_matches_type(object, speak, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncCasemark) -> None:
        async with async_client.voice.v1.speak.with_streaming_response.stream(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speak = await response.parse()
            assert_matches_type(object, speak, path=["response"])

        assert cast(Any, response.is_closed) is True
