# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.matters.v1 import (
    ContentPurgeCreateResponse,
    ContentPurgeRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContentPurges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        content_purge = client.matters.v1.content_purges.create(
            id="id",
            request_id="request_id",
        )
        assert_matches_type(ContentPurgeCreateResponse, content_purge, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        content_purge = client.matters.v1.content_purges.create(
            id="id",
            request_id="request_id",
            object_ids=["string"],
            session_ids=["string"],
            transcription_ids=["string"],
            work_item_ids=["string"],
        )
        assert_matches_type(ContentPurgeCreateResponse, content_purge, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.matters.v1.content_purges.with_raw_response.create(
            id="id",
            request_id="request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_purge = response.parse()
        assert_matches_type(ContentPurgeCreateResponse, content_purge, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.matters.v1.content_purges.with_streaming_response.create(
            id="id",
            request_id="request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_purge = response.parse()
            assert_matches_type(ContentPurgeCreateResponse, content_purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.content_purges.with_raw_response.create(
                id="",
                request_id="request_id",
            )

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        content_purge = client.matters.v1.content_purges.retrieve(
            "purgeId",
        )
        assert_matches_type(ContentPurgeRetrieveResponse, content_purge, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.matters.v1.content_purges.with_raw_response.retrieve(
            "purgeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_purge = response.parse()
        assert_matches_type(ContentPurgeRetrieveResponse, content_purge, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.matters.v1.content_purges.with_streaming_response.retrieve(
            "purgeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_purge = response.parse()
            assert_matches_type(ContentPurgeRetrieveResponse, content_purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `purge_id` but received ''"):
            client.matters.v1.content_purges.with_raw_response.retrieve(
                "",
            )


class TestAsyncContentPurges:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        content_purge = await async_client.matters.v1.content_purges.create(
            id="id",
            request_id="request_id",
        )
        assert_matches_type(ContentPurgeCreateResponse, content_purge, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        content_purge = await async_client.matters.v1.content_purges.create(
            id="id",
            request_id="request_id",
            object_ids=["string"],
            session_ids=["string"],
            transcription_ids=["string"],
            work_item_ids=["string"],
        )
        assert_matches_type(ContentPurgeCreateResponse, content_purge, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.content_purges.with_raw_response.create(
            id="id",
            request_id="request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_purge = await response.parse()
        assert_matches_type(ContentPurgeCreateResponse, content_purge, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.content_purges.with_streaming_response.create(
            id="id",
            request_id="request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_purge = await response.parse()
            assert_matches_type(ContentPurgeCreateResponse, content_purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.content_purges.with_raw_response.create(
                id="",
                request_id="request_id",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        content_purge = await async_client.matters.v1.content_purges.retrieve(
            "purgeId",
        )
        assert_matches_type(ContentPurgeRetrieveResponse, content_purge, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.content_purges.with_raw_response.retrieve(
            "purgeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_purge = await response.parse()
        assert_matches_type(ContentPurgeRetrieveResponse, content_purge, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.content_purges.with_streaming_response.retrieve(
            "purgeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_purge = await response.parse()
            assert_matches_type(ContentPurgeRetrieveResponse, content_purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `purge_id` but received ''"):
            await async_client.matters.v1.content_purges.with_raw_response.retrieve(
                "",
            )
