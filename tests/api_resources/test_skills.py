# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types import SkillReadResponse, SkillResolveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSkills:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_read(self, client: Casedev) -> None:
        skill = client.skills.read(
            "slug",
        )
        assert_matches_type(SkillReadResponse, skill, path=["response"])

    @parametrize
    def test_raw_response_read(self, client: Casedev) -> None:
        response = client.skills.with_raw_response.read(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillReadResponse, skill, path=["response"])

    @parametrize
    def test_streaming_response_read(self, client: Casedev) -> None:
        with client.skills.with_streaming_response.read(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillReadResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_read(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.skills.with_raw_response.read(
                "",
            )

    @parametrize
    def test_method_resolve(self, client: Casedev) -> None:
        skill = client.skills.resolve(
            q="q",
        )
        assert_matches_type(SkillResolveResponse, skill, path=["response"])

    @parametrize
    def test_method_resolve_with_all_params(self, client: Casedev) -> None:
        skill = client.skills.resolve(
            q="q",
            limit=1,
        )
        assert_matches_type(SkillResolveResponse, skill, path=["response"])

    @parametrize
    def test_raw_response_resolve(self, client: Casedev) -> None:
        response = client.skills.with_raw_response.resolve(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillResolveResponse, skill, path=["response"])

    @parametrize
    def test_streaming_response_resolve(self, client: Casedev) -> None:
        with client.skills.with_streaming_response.resolve(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillResolveResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSkills:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_read(self, async_client: AsyncCasedev) -> None:
        skill = await async_client.skills.read(
            "slug",
        )
        assert_matches_type(SkillReadResponse, skill, path=["response"])

    @parametrize
    async def test_raw_response_read(self, async_client: AsyncCasedev) -> None:
        response = await async_client.skills.with_raw_response.read(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillReadResponse, skill, path=["response"])

    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncCasedev) -> None:
        async with async_client.skills.with_streaming_response.read(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillReadResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_read(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.skills.with_raw_response.read(
                "",
            )

    @parametrize
    async def test_method_resolve(self, async_client: AsyncCasedev) -> None:
        skill = await async_client.skills.resolve(
            q="q",
        )
        assert_matches_type(SkillResolveResponse, skill, path=["response"])

    @parametrize
    async def test_method_resolve_with_all_params(self, async_client: AsyncCasedev) -> None:
        skill = await async_client.skills.resolve(
            q="q",
            limit=1,
        )
        assert_matches_type(SkillResolveResponse, skill, path=["response"])

    @parametrize
    async def test_raw_response_resolve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.skills.with_raw_response.resolve(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillResolveResponse, skill, path=["response"])

    @parametrize
    async def test_streaming_response_resolve(self, async_client: AsyncCasedev) -> None:
        async with async_client.skills.with_streaming_response.resolve(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillResolveResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True
