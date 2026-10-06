# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.matters.v1 import PurgeRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPurges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        purge = client.matters.v1.purges.retrieve(
            "purgeId",
        )
        assert_matches_type(PurgeRetrieveResponse, purge, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.matters.v1.purges.with_raw_response.retrieve(
            "purgeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge = response.parse()
        assert_matches_type(PurgeRetrieveResponse, purge, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.matters.v1.purges.with_streaming_response.retrieve(
            "purgeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge = response.parse()
            assert_matches_type(PurgeRetrieveResponse, purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `purge_id` but received ''"):
            client.matters.v1.purges.with_raw_response.retrieve(
                "",
            )


class TestAsyncPurges:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        purge = await async_client.matters.v1.purges.retrieve(
            "purgeId",
        )
        assert_matches_type(PurgeRetrieveResponse, purge, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.purges.with_raw_response.retrieve(
            "purgeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge = await response.parse()
        assert_matches_type(PurgeRetrieveResponse, purge, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.purges.with_streaming_response.retrieve(
            "purgeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge = await response.parse()
            assert_matches_type(PurgeRetrieveResponse, purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `purge_id` but received ''"):
            await async_client.matters.v1.purges.with_raw_response.retrieve(
                "",
            )
