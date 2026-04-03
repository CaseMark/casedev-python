# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.vault import (
    MemoryListResponse,
    MemoryCreateResponse,
    MemorySearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        memory = client.vault.memory.create(
            id="id",
            content="content",
            type="fact",
        )
        assert_matches_type(MemoryCreateResponse, memory, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        memory = client.vault.memory.create(
            id="id",
            content="content",
            type="fact",
            source="source",
            tags=["string"],
        )
        assert_matches_type(MemoryCreateResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.vault.memory.with_raw_response.create(
            id="id",
            content="content",
            type="fact",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryCreateResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.vault.memory.with_streaming_response.create(
            id="id",
            content="content",
            type="fact",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryCreateResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.memory.with_raw_response.create(
                id="",
                content="content",
                type="fact",
            )

    @parametrize
    def test_method_update(self, client: Casedev) -> None:
        memory = client.vault.memory.update(
            entry_id="entryId",
            id="id",
        )
        assert memory is None

    @parametrize
    def test_method_update_with_all_params(self, client: Casedev) -> None:
        memory = client.vault.memory.update(
            entry_id="entryId",
            id="id",
            content="content",
            source="source",
            tags=["string"],
        )
        assert memory is None

    @parametrize
    def test_raw_response_update(self, client: Casedev) -> None:
        response = client.vault.memory.with_raw_response.update(
            entry_id="entryId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert memory is None

    @parametrize
    def test_streaming_response_update(self, client: Casedev) -> None:
        with client.vault.memory.with_streaming_response.update(
            entry_id="entryId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.memory.with_raw_response.update(
                entry_id="entryId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.vault.memory.with_raw_response.update(
                entry_id="",
                id="id",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        memory = client.vault.memory.list(
            "id",
        )
        assert_matches_type(MemoryListResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.vault.memory.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryListResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.vault.memory.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryListResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.memory.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        memory = client.vault.memory.delete(
            entry_id="entryId",
            id="id",
        )
        assert memory is None

    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.vault.memory.with_raw_response.delete(
            entry_id="entryId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert memory is None

    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.vault.memory.with_streaming_response.delete(
            entry_id="entryId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.memory.with_raw_response.delete(
                entry_id="entryId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.vault.memory.with_raw_response.delete(
                entry_id="",
                id="id",
            )

    @parametrize
    def test_method_search(self, client: Casedev) -> None:
        memory = client.vault.memory.search(
            id="id",
            query="query",
        )
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Casedev) -> None:
        memory = client.vault.memory.search(
            id="id",
            query="query",
            limit=1,
            tags=["string"],
            types=["string"],
        )
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Casedev) -> None:
        response = client.vault.memory.with_raw_response.search(
            id="id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Casedev) -> None:
        with client.vault.memory.with_streaming_response.search(
            id="id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemorySearchResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.memory.with_raw_response.search(
                id="",
                query="query",
            )


class TestAsyncMemory:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        memory = await async_client.vault.memory.create(
            id="id",
            content="content",
            type="fact",
        )
        assert_matches_type(MemoryCreateResponse, memory, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        memory = await async_client.vault.memory.create(
            id="id",
            content="content",
            type="fact",
            source="source",
            tags=["string"],
        )
        assert_matches_type(MemoryCreateResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.memory.with_raw_response.create(
            id="id",
            content="content",
            type="fact",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryCreateResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.memory.with_streaming_response.create(
            id="id",
            content="content",
            type="fact",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryCreateResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.memory.with_raw_response.create(
                id="",
                content="content",
                type="fact",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCasedev) -> None:
        memory = await async_client.vault.memory.update(
            entry_id="entryId",
            id="id",
        )
        assert memory is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCasedev) -> None:
        memory = await async_client.vault.memory.update(
            entry_id="entryId",
            id="id",
            content="content",
            source="source",
            tags=["string"],
        )
        assert memory is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.memory.with_raw_response.update(
            entry_id="entryId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert memory is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.memory.with_streaming_response.update(
            entry_id="entryId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.memory.with_raw_response.update(
                entry_id="entryId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.vault.memory.with_raw_response.update(
                entry_id="",
                id="id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        memory = await async_client.vault.memory.list(
            "id",
        )
        assert_matches_type(MemoryListResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.memory.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryListResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.memory.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryListResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.memory.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        memory = await async_client.vault.memory.delete(
            entry_id="entryId",
            id="id",
        )
        assert memory is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.memory.with_raw_response.delete(
            entry_id="entryId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert memory is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.memory.with_streaming_response.delete(
            entry_id="entryId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.memory.with_raw_response.delete(
                entry_id="entryId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.vault.memory.with_raw_response.delete(
                entry_id="",
                id="id",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncCasedev) -> None:
        memory = await async_client.vault.memory.search(
            id="id",
            query="query",
        )
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncCasedev) -> None:
        memory = await async_client.vault.memory.search(
            id="id",
            query="query",
            limit=1,
            tags=["string"],
            types=["string"],
        )
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.memory.with_raw_response.search(
            id="id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.memory.with_streaming_response.search(
            id="id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemorySearchResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.memory.with_raw_response.search(
                id="",
                query="query",
            )
