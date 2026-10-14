# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.vault import (
    FolderListResponse,
    FolderMoveResponse,
    FolderCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        folder = client.vault.folders.create(
            id="id",
            path="path",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.vault.folders.with_raw_response.create(
            id="id",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.vault.folders.with_streaming_response.create(
            id="id",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderCreateResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.folders.with_raw_response.create(
                id="",
                path="path",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        folder = client.vault.folders.list(
            "id",
        )
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.vault.folders.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.vault.folders.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderListResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.folders.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_move(self, client: Casedev) -> None:
        folder = client.vault.folders.move(
            id="id",
            new_path="newPath",
            path="path",
        )
        assert_matches_type(FolderMoveResponse, folder, path=["response"])

    @parametrize
    def test_method_move_with_all_params(self, client: Casedev) -> None:
        folder = client.vault.folders.move(
            id="id",
            new_path="newPath",
            path="path",
            expected_revision="expectedRevision",
        )
        assert_matches_type(FolderMoveResponse, folder, path=["response"])

    @parametrize
    def test_raw_response_move(self, client: Casedev) -> None:
        response = client.vault.folders.with_raw_response.move(
            id="id",
            new_path="newPath",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderMoveResponse, folder, path=["response"])

    @parametrize
    def test_streaming_response_move(self, client: Casedev) -> None:
        with client.vault.folders.with_streaming_response.move(
            id="id",
            new_path="newPath",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderMoveResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_move(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.folders.with_raw_response.move(
                id="",
                new_path="newPath",
                path="path",
            )


class TestAsyncFolders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        folder = await async_client.vault.folders.create(
            id="id",
            path="path",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.folders.with_raw_response.create(
            id="id",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.folders.with_streaming_response.create(
            id="id",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderCreateResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.folders.with_raw_response.create(
                id="",
                path="path",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        folder = await async_client.vault.folders.list(
            "id",
        )
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.folders.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderListResponse, folder, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.folders.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderListResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.folders.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_move(self, async_client: AsyncCasedev) -> None:
        folder = await async_client.vault.folders.move(
            id="id",
            new_path="newPath",
            path="path",
        )
        assert_matches_type(FolderMoveResponse, folder, path=["response"])

    @parametrize
    async def test_method_move_with_all_params(self, async_client: AsyncCasedev) -> None:
        folder = await async_client.vault.folders.move(
            id="id",
            new_path="newPath",
            path="path",
            expected_revision="expectedRevision",
        )
        assert_matches_type(FolderMoveResponse, folder, path=["response"])

    @parametrize
    async def test_raw_response_move(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.folders.with_raw_response.move(
            id="id",
            new_path="newPath",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderMoveResponse, folder, path=["response"])

    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.folders.with_streaming_response.move(
            id="id",
            new_path="newPath",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderMoveResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_move(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.folders.with_raw_response.move(
                id="",
                new_path="newPath",
                path="path",
            )
