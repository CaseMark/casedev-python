# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.media.v1.transcripts import RetrieveCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetrieve:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        retrieve = client.media.v1.transcripts.retrieve.create(
            object_id="object_id",
            vault_id="vault_id",
        )
        assert_matches_type(RetrieveCreateResponse, retrieve, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        retrieve = client.media.v1.transcripts.retrieve.create(
            object_id="object_id",
            vault_id="vault_id",
            transcript={
                "object_id": "object_id",
                "vault_id": "vault_id",
            },
        )
        assert_matches_type(RetrieveCreateResponse, retrieve, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.media.v1.transcripts.retrieve.with_raw_response.create(
            object_id="object_id",
            vault_id="vault_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieve = response.parse()
        assert_matches_type(RetrieveCreateResponse, retrieve, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.media.v1.transcripts.retrieve.with_streaming_response.create(
            object_id="object_id",
            vault_id="vault_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieve = response.parse()
            assert_matches_type(RetrieveCreateResponse, retrieve, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRetrieve:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        retrieve = await async_client.media.v1.transcripts.retrieve.create(
            object_id="object_id",
            vault_id="vault_id",
        )
        assert_matches_type(RetrieveCreateResponse, retrieve, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        retrieve = await async_client.media.v1.transcripts.retrieve.create(
            object_id="object_id",
            vault_id="vault_id",
            transcript={
                "object_id": "object_id",
                "vault_id": "vault_id",
            },
        )
        assert_matches_type(RetrieveCreateResponse, retrieve, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.media.v1.transcripts.retrieve.with_raw_response.create(
            object_id="object_id",
            vault_id="vault_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieve = await response.parse()
        assert_matches_type(RetrieveCreateResponse, retrieve, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.media.v1.transcripts.retrieve.with_streaming_response.create(
            object_id="object_id",
            vault_id="vault_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieve = await response.parse()
            assert_matches_type(RetrieveCreateResponse, retrieve, path=["response"])

        assert cast(Any, response.is_closed) is True
