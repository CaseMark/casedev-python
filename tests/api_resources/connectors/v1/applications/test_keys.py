# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.connectors.v1.applications import KeyBindResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_bind(self, client: Casedev) -> None:
        key = client.connectors.v1.applications.keys.bind(
            key_id="keyId",
            id="id",
        )
        assert_matches_type(KeyBindResponse, key, path=["response"])

    @parametrize
    def test_raw_response_bind(self, client: Casedev) -> None:
        response = client.connectors.v1.applications.keys.with_raw_response.bind(
            key_id="keyId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyBindResponse, key, path=["response"])

    @parametrize
    def test_streaming_response_bind(self, client: Casedev) -> None:
        with client.connectors.v1.applications.keys.with_streaming_response.bind(
            key_id="keyId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyBindResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bind(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.applications.keys.with_raw_response.bind(
                key_id="keyId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.connectors.v1.applications.keys.with_raw_response.bind(
                key_id="",
                id="id",
            )

    @parametrize
    def test_method_revoke(self, client: Casedev) -> None:
        key = client.connectors.v1.applications.keys.revoke(
            key_id="keyId",
            id="id",
        )
        assert key is None

    @parametrize
    def test_raw_response_revoke(self, client: Casedev) -> None:
        response = client.connectors.v1.applications.keys.with_raw_response.revoke(
            key_id="keyId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert key is None

    @parametrize
    def test_streaming_response_revoke(self, client: Casedev) -> None:
        with client.connectors.v1.applications.keys.with_streaming_response.revoke(
            key_id="keyId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revoke(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.applications.keys.with_raw_response.revoke(
                key_id="keyId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.connectors.v1.applications.keys.with_raw_response.revoke(
                key_id="",
                id="id",
            )


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_bind(self, async_client: AsyncCasedev) -> None:
        key = await async_client.connectors.v1.applications.keys.bind(
            key_id="keyId",
            id="id",
        )
        assert_matches_type(KeyBindResponse, key, path=["response"])

    @parametrize
    async def test_raw_response_bind(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.applications.keys.with_raw_response.bind(
            key_id="keyId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyBindResponse, key, path=["response"])

    @parametrize
    async def test_streaming_response_bind(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.applications.keys.with_streaming_response.bind(
            key_id="keyId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyBindResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bind(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.applications.keys.with_raw_response.bind(
                key_id="keyId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.connectors.v1.applications.keys.with_raw_response.bind(
                key_id="",
                id="id",
            )

    @parametrize
    async def test_method_revoke(self, async_client: AsyncCasedev) -> None:
        key = await async_client.connectors.v1.applications.keys.revoke(
            key_id="keyId",
            id="id",
        )
        assert key is None

    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.applications.keys.with_raw_response.revoke(
            key_id="keyId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert key is None

    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.applications.keys.with_streaming_response.revoke(
            key_id="keyId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.applications.keys.with_raw_response.revoke(
                key_id="keyId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.connectors.v1.applications.keys.with_raw_response.revoke(
                key_id="",
                id="id",
            )
