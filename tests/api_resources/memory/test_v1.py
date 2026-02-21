# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.memory import (
    V1ListResponse,
    V1CreateResponse,
    V1DeleteResponse,
    V1SearchResponse,
    V1RetrieveResponse,
    V1DeleteAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        v1 = client.memory.v1.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(V1CreateResponse, v1, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        v1 = client.memory.v1.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            category="category",
            extraction_prompt="extraction_prompt",
            infer=True,
            metadata={"foo": "bar"},
            tag_1="tag_1",
            tag_10="tag_10",
            tag_11="tag_11",
            tag_12="tag_12",
            tag_2="tag_2",
            tag_3="tag_3",
            tag_4="tag_4",
            tag_5="tag_5",
            tag_6="tag_6",
            tag_7="tag_7",
            tag_8="tag_8",
            tag_9="tag_9",
        )
        assert_matches_type(V1CreateResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.memory.v1.with_raw_response.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1CreateResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.memory.v1.with_streaming_response.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1CreateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        v1 = client.memory.v1.retrieve(
            "id",
        )
        assert_matches_type(V1RetrieveResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.memory.v1.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1RetrieveResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.memory.v1.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1RetrieveResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memory.v1.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        v1 = client.memory.v1.list()
        assert_matches_type(V1ListResponse, v1, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        v1 = client.memory.v1.list(
            category="category",
            limit=0,
            offset=0,
            tag_1="tag_1",
            tag_10="tag_10",
            tag_11="tag_11",
            tag_12="tag_12",
            tag_2="tag_2",
            tag_3="tag_3",
            tag_4="tag_4",
            tag_5="tag_5",
            tag_6="tag_6",
            tag_7="tag_7",
            tag_8="tag_8",
            tag_9="tag_9",
        )
        assert_matches_type(V1ListResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.memory.v1.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.memory.v1.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        v1 = client.memory.v1.delete(
            "id",
        )
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.memory.v1.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.memory.v1.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1DeleteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memory.v1.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_delete_all(self, client: Casedev) -> None:
        v1 = client.memory.v1.delete_all()
        assert_matches_type(V1DeleteAllResponse, v1, path=["response"])

    @parametrize
    def test_method_delete_all_with_all_params(self, client: Casedev) -> None:
        v1 = client.memory.v1.delete_all(
            tag_1="tag_1",
            tag_10="tag_10",
            tag_11="tag_11",
            tag_12="tag_12",
            tag_2="tag_2",
            tag_3="tag_3",
            tag_4="tag_4",
            tag_5="tag_5",
            tag_6="tag_6",
            tag_7="tag_7",
            tag_8="tag_8",
            tag_9="tag_9",
        )
        assert_matches_type(V1DeleteAllResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_delete_all(self, client: Casedev) -> None:
        response = client.memory.v1.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1DeleteAllResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_delete_all(self, client: Casedev) -> None:
        with client.memory.v1.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1DeleteAllResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: Casedev) -> None:
        v1 = client.memory.v1.search(
            query="query",
        )
        assert_matches_type(V1SearchResponse, v1, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Casedev) -> None:
        v1 = client.memory.v1.search(
            query="query",
            category="category",
            tag_1="tag_1",
            tag_10="tag_10",
            tag_11="tag_11",
            tag_12="tag_12",
            tag_2="tag_2",
            tag_3="tag_3",
            tag_4="tag_4",
            tag_5="tag_5",
            tag_6="tag_6",
            tag_7="tag_7",
            tag_8="tag_8",
            tag_9="tag_9",
            top_k=1,
        )
        assert_matches_type(V1SearchResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Casedev) -> None:
        response = client.memory.v1.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1SearchResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Casedev) -> None:
        with client.memory.v1.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1SearchResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.memory.v1.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(V1CreateResponse, v1, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.memory.v1.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            category="category",
            extraction_prompt="extraction_prompt",
            infer=True,
            metadata={"foo": "bar"},
            tag_1="tag_1",
            tag_10="tag_10",
            tag_11="tag_11",
            tag_12="tag_12",
            tag_2="tag_2",
            tag_3="tag_3",
            tag_4="tag_4",
            tag_5="tag_5",
            tag_6="tag_6",
            tag_7="tag_7",
            tag_8="tag_8",
            tag_9="tag_9",
        )
        assert_matches_type(V1CreateResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.memory.v1.with_raw_response.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1CreateResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.memory.v1.with_streaming_response.create(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1CreateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.memory.v1.retrieve(
            "id",
        )
        assert_matches_type(V1RetrieveResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.memory.v1.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1RetrieveResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.memory.v1.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1RetrieveResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memory.v1.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.memory.v1.list()
        assert_matches_type(V1ListResponse, v1, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.memory.v1.list(
            category="category",
            limit=0,
            offset=0,
            tag_1="tag_1",
            tag_10="tag_10",
            tag_11="tag_11",
            tag_12="tag_12",
            tag_2="tag_2",
            tag_3="tag_3",
            tag_4="tag_4",
            tag_5="tag_5",
            tag_6="tag_6",
            tag_7="tag_7",
            tag_8="tag_8",
            tag_9="tag_9",
        )
        assert_matches_type(V1ListResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.memory.v1.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.memory.v1.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.memory.v1.delete(
            "id",
        )
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.memory.v1.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.memory.v1.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1DeleteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memory.v1.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_delete_all(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.memory.v1.delete_all()
        assert_matches_type(V1DeleteAllResponse, v1, path=["response"])

    @parametrize
    async def test_method_delete_all_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.memory.v1.delete_all(
            tag_1="tag_1",
            tag_10="tag_10",
            tag_11="tag_11",
            tag_12="tag_12",
            tag_2="tag_2",
            tag_3="tag_3",
            tag_4="tag_4",
            tag_5="tag_5",
            tag_6="tag_6",
            tag_7="tag_7",
            tag_8="tag_8",
            tag_9="tag_9",
        )
        assert_matches_type(V1DeleteAllResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncCasedev) -> None:
        response = await async_client.memory.v1.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1DeleteAllResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncCasedev) -> None:
        async with async_client.memory.v1.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1DeleteAllResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.memory.v1.search(
            query="query",
        )
        assert_matches_type(V1SearchResponse, v1, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.memory.v1.search(
            query="query",
            category="category",
            tag_1="tag_1",
            tag_10="tag_10",
            tag_11="tag_11",
            tag_12="tag_12",
            tag_2="tag_2",
            tag_3="tag_3",
            tag_4="tag_4",
            tag_5="tag_5",
            tag_6="tag_6",
            tag_7="tag_7",
            tag_8="tag_8",
            tag_9="tag_9",
            top_k=1,
        )
        assert_matches_type(V1SearchResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncCasedev) -> None:
        response = await async_client.memory.v1.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1SearchResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncCasedev) -> None:
        async with async_client.memory.v1.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1SearchResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
