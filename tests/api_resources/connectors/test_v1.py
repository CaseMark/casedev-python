# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.connectors import V1SyncLinkResponse, V1TransferResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_sync_link(self, client: Casedev) -> None:
        v1 = client.connectors.v1.sync_link(
            connection_id="connection_id",
            direction="import",
            remote={"folder_id": "folder_id"},
            vault_id="vault_id",
        )
        assert_matches_type(V1SyncLinkResponse, v1, path=["response"])

    @parametrize
    def test_method_sync_link_with_all_params(self, client: Casedev) -> None:
        v1 = client.connectors.v1.sync_link(
            connection_id="connection_id",
            direction="import",
            remote={
                "folder_id": "folder_id",
                "container_id": "container_id",
                "path": "path",
                "site_id": "site_id",
            },
            vault_id="vault_id",
            matter_id="matter_id",
            policy={
                "collisions": "version",
                "deletes": "mirror",
                "filters": {
                    "exclude_mime": ["string"],
                    "max_size_bytes": 0,
                },
            },
        )
        assert_matches_type(V1SyncLinkResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_sync_link(self, client: Casedev) -> None:
        response = client.connectors.v1.with_raw_response.sync_link(
            connection_id="connection_id",
            direction="import",
            remote={"folder_id": "folder_id"},
            vault_id="vault_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1SyncLinkResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_sync_link(self, client: Casedev) -> None:
        with client.connectors.v1.with_streaming_response.sync_link(
            connection_id="connection_id",
            direction="import",
            remote={"folder_id": "folder_id"},
            vault_id="vault_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1SyncLinkResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_transfer(self, client: Casedev) -> None:
        v1 = client.connectors.v1.transfer(
            connection_id="connection_id",
            direction="import",
            remote={"folder_id": "folder_id"},
            vault_id="vault_id",
        )
        assert_matches_type(V1TransferResponse, v1, path=["response"])

    @parametrize
    def test_method_transfer_with_all_params(self, client: Casedev) -> None:
        v1 = client.connectors.v1.transfer(
            connection_id="connection_id",
            direction="import",
            remote={
                "folder_id": "folder_id",
                "container_id": "container_id",
                "path": "path",
                "site_id": "site_id",
            },
            vault_id="vault_id",
            matter_id="matter_id",
            policy={
                "collisions": "version",
                "deletes": "mirror",
                "filters": {
                    "exclude_mime": ["string"],
                    "max_size_bytes": 0,
                },
            },
            run_mode="auto",
        )
        assert_matches_type(V1TransferResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_transfer(self, client: Casedev) -> None:
        response = client.connectors.v1.with_raw_response.transfer(
            connection_id="connection_id",
            direction="import",
            remote={"folder_id": "folder_id"},
            vault_id="vault_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1TransferResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_transfer(self, client: Casedev) -> None:
        with client.connectors.v1.with_streaming_response.transfer(
            connection_id="connection_id",
            direction="import",
            remote={"folder_id": "folder_id"},
            vault_id="vault_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1TransferResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_sync_link(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.connectors.v1.sync_link(
            connection_id="connection_id",
            direction="import",
            remote={"folder_id": "folder_id"},
            vault_id="vault_id",
        )
        assert_matches_type(V1SyncLinkResponse, v1, path=["response"])

    @parametrize
    async def test_method_sync_link_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.connectors.v1.sync_link(
            connection_id="connection_id",
            direction="import",
            remote={
                "folder_id": "folder_id",
                "container_id": "container_id",
                "path": "path",
                "site_id": "site_id",
            },
            vault_id="vault_id",
            matter_id="matter_id",
            policy={
                "collisions": "version",
                "deletes": "mirror",
                "filters": {
                    "exclude_mime": ["string"],
                    "max_size_bytes": 0,
                },
            },
        )
        assert_matches_type(V1SyncLinkResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_sync_link(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.with_raw_response.sync_link(
            connection_id="connection_id",
            direction="import",
            remote={"folder_id": "folder_id"},
            vault_id="vault_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1SyncLinkResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_sync_link(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.with_streaming_response.sync_link(
            connection_id="connection_id",
            direction="import",
            remote={"folder_id": "folder_id"},
            vault_id="vault_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1SyncLinkResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_transfer(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.connectors.v1.transfer(
            connection_id="connection_id",
            direction="import",
            remote={"folder_id": "folder_id"},
            vault_id="vault_id",
        )
        assert_matches_type(V1TransferResponse, v1, path=["response"])

    @parametrize
    async def test_method_transfer_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.connectors.v1.transfer(
            connection_id="connection_id",
            direction="import",
            remote={
                "folder_id": "folder_id",
                "container_id": "container_id",
                "path": "path",
                "site_id": "site_id",
            },
            vault_id="vault_id",
            matter_id="matter_id",
            policy={
                "collisions": "version",
                "deletes": "mirror",
                "filters": {
                    "exclude_mime": ["string"],
                    "max_size_bytes": 0,
                },
            },
            run_mode="auto",
        )
        assert_matches_type(V1TransferResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_transfer(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.with_raw_response.transfer(
            connection_id="connection_id",
            direction="import",
            remote={"folder_id": "folder_id"},
            vault_id="vault_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1TransferResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_transfer(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.with_streaming_response.transfer(
            connection_id="connection_id",
            direction="import",
            remote={"folder_id": "folder_id"},
            vault_id="vault_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1TransferResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
