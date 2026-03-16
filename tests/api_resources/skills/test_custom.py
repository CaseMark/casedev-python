# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.skills import CustomListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        custom = client.skills.custom.list()
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        custom = client.skills.custom.list(
            cursor="cursor",
            limit=1,
            tag="tag",
        )
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.skills.custom.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.skills.custom.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomListResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustom:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        custom = await async_client.skills.custom.list()
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        custom = await async_client.skills.custom.list(
            cursor="cursor",
            limit=1,
            tag="tag",
        )
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.skills.custom.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.skills.custom.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomListResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True
