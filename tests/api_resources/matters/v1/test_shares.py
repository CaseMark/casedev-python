# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from casedev._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShares:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        share = client.matters.v1.shares.create(
            id="id",
            target_org_id="target_org_id",
        )
        assert share is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        share = client.matters.v1.shares.create(
            id="id",
            target_org_id="target_org_id",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            permission="read",
        )
        assert share is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.matters.v1.shares.with_raw_response.create(
            id="id",
            target_org_id="target_org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = response.parse()
        assert share is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.matters.v1.shares.with_streaming_response.create(
            id="id",
            target_org_id="target_org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = response.parse()
            assert share is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.shares.with_raw_response.create(
                id="",
                target_org_id="target_org_id",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        share = client.matters.v1.shares.list(
            "id",
        )
        assert share is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.matters.v1.shares.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = response.parse()
        assert share is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.matters.v1.shares.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = response.parse()
            assert share is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.shares.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        share = client.matters.v1.shares.delete(
            share_id="shareId",
            id="id",
        )
        assert share is None

    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.matters.v1.shares.with_raw_response.delete(
            share_id="shareId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = response.parse()
        assert share is None

    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.matters.v1.shares.with_streaming_response.delete(
            share_id="shareId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = response.parse()
            assert share is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.shares.with_raw_response.delete(
                share_id="shareId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            client.matters.v1.shares.with_raw_response.delete(
                share_id="",
                id="id",
            )


class TestAsyncShares:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        share = await async_client.matters.v1.shares.create(
            id="id",
            target_org_id="target_org_id",
        )
        assert share is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        share = await async_client.matters.v1.shares.create(
            id="id",
            target_org_id="target_org_id",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            permission="read",
        )
        assert share is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.shares.with_raw_response.create(
            id="id",
            target_org_id="target_org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = await response.parse()
        assert share is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.shares.with_streaming_response.create(
            id="id",
            target_org_id="target_org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = await response.parse()
            assert share is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.shares.with_raw_response.create(
                id="",
                target_org_id="target_org_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        share = await async_client.matters.v1.shares.list(
            "id",
        )
        assert share is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.shares.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = await response.parse()
        assert share is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.shares.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = await response.parse()
            assert share is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.shares.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        share = await async_client.matters.v1.shares.delete(
            share_id="shareId",
            id="id",
        )
        assert share is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.shares.with_raw_response.delete(
            share_id="shareId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = await response.parse()
        assert share is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.shares.with_streaming_response.delete(
            share_id="shareId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = await response.parse()
            assert share is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.shares.with_raw_response.delete(
                share_id="shareId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            await async_client.matters.v1.shares.with_raw_response.delete(
                share_id="",
                id="id",
            )
