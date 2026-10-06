# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.connectors.v1.installations import TokenCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        token = client.connectors.v1.installations.tokens.create(
            id="id",
            scopes=["read"],
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.connectors.v1.installations.tokens.with_raw_response.create(
            id="id",
            scopes=["read"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.connectors.v1.installations.tokens.with_streaming_response.create(
            id="id",
            scopes=["read"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenCreateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.installations.tokens.with_raw_response.create(
                id="",
                scopes=["read"],
            )

    @parametrize
    def test_method_revoke(self, client: Casedev) -> None:
        token = client.connectors.v1.installations.tokens.revoke(
            token_id="tokenId",
            id="id",
        )
        assert token is None

    @parametrize
    def test_raw_response_revoke(self, client: Casedev) -> None:
        response = client.connectors.v1.installations.tokens.with_raw_response.revoke(
            token_id="tokenId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert token is None

    @parametrize
    def test_streaming_response_revoke(self, client: Casedev) -> None:
        with client.connectors.v1.installations.tokens.with_streaming_response.revoke(
            token_id="tokenId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revoke(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.installations.tokens.with_raw_response.revoke(
                token_id="tokenId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            client.connectors.v1.installations.tokens.with_raw_response.revoke(
                token_id="",
                id="id",
            )


class TestAsyncTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        token = await async_client.connectors.v1.installations.tokens.create(
            id="id",
            scopes=["read"],
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.installations.tokens.with_raw_response.create(
            id="id",
            scopes=["read"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.installations.tokens.with_streaming_response.create(
            id="id",
            scopes=["read"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenCreateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.installations.tokens.with_raw_response.create(
                id="",
                scopes=["read"],
            )

    @parametrize
    async def test_method_revoke(self, async_client: AsyncCasedev) -> None:
        token = await async_client.connectors.v1.installations.tokens.revoke(
            token_id="tokenId",
            id="id",
        )
        assert token is None

    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.installations.tokens.with_raw_response.revoke(
            token_id="tokenId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert token is None

    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.installations.tokens.with_streaming_response.revoke(
            token_id="tokenId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.installations.tokens.with_raw_response.revoke(
                token_id="tokenId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            await async_client.connectors.v1.installations.tokens.with_raw_response.revoke(
                token_id="",
                id="id",
            )
