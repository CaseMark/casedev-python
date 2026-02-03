# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.privilege import V1DetectResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detect(self, client: Casedev) -> None:
        v1 = client.privilege.v1.detect()
        assert_matches_type(V1DetectResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detect_with_all_params(self, client: Casedev) -> None:
        v1 = client.privilege.v1.detect(
            categories=["attorney_client"],
            content="content",
            document_id="document_id",
            include_rationale=True,
            jurisdiction="US-Federal",
            model="model",
            vault_id="vault_id",
        )
        assert_matches_type(V1DetectResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_detect(self, client: Casedev) -> None:
        response = client.privilege.v1.with_raw_response.detect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1DetectResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_detect(self, client: Casedev) -> None:
        with client.privilege.v1.with_streaming_response.detect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1DetectResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detect(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.privilege.v1.detect()
        assert_matches_type(V1DetectResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detect_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.privilege.v1.detect(
            categories=["attorney_client"],
            content="content",
            document_id="document_id",
            include_rationale=True,
            jurisdiction="US-Federal",
            model="model",
            vault_id="vault_id",
        )
        assert_matches_type(V1DetectResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_detect(self, async_client: AsyncCasedev) -> None:
        response = await async_client.privilege.v1.with_raw_response.detect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1DetectResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_detect(self, async_client: AsyncCasedev) -> None:
        async with async_client.privilege.v1.with_streaming_response.detect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1DetectResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
