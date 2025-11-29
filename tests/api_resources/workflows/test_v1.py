# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from casedotdev_sdk_py import Casemark, AsyncCasemark
from casedotdev_sdk_py.types.workflows import V1ExecuteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Casemark) -> None:
        v1 = client.workflows.v1.retrieve(
            "id",
        )
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Casemark) -> None:
        response = client.workflows.v1.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Casemark) -> None:
        with client.workflows.v1.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Casemark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workflows.v1.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Casemark) -> None:
        v1 = client.workflows.v1.list()
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Casemark) -> None:
        v1 = client.workflows.v1.list(
            category="category",
            limit=1,
            offset=0,
            published=True,
            sub_category="sub_category",
            type="type",
        )
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Casemark) -> None:
        response = client.workflows.v1.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Casemark) -> None:
        with client.workflows.v1.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute(self, client: Casemark) -> None:
        v1 = client.workflows.v1.execute(
            id="id",
            input={},
        )
        assert_matches_type(V1ExecuteResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute_with_all_params(self, client: Casemark) -> None:
        v1 = client.workflows.v1.execute(
            id="id",
            input={},
            options={
                "format": "json",
                "model": "model",
            },
        )
        assert_matches_type(V1ExecuteResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_execute(self, client: Casemark) -> None:
        response = client.workflows.v1.with_raw_response.execute(
            id="id",
            input={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ExecuteResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_execute(self, client: Casemark) -> None:
        with client.workflows.v1.with_streaming_response.execute(
            id="id",
            input={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ExecuteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_execute(self, client: Casemark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workflows.v1.with_raw_response.execute(
                id="",
                input={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execution_retrieve(self, client: Casemark) -> None:
        v1 = client.workflows.v1.execution_retrieve(
            "exec_abc123def456",
        )
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_execution_retrieve(self, client: Casemark) -> None:
        response = client.workflows.v1.with_raw_response.execution_retrieve(
            "exec_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_execution_retrieve(self, client: Casemark) -> None:
        with client.workflows.v1.with_streaming_response.execution_retrieve(
            "exec_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_execution_retrieve(self, client: Casemark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workflows.v1.with_raw_response.execution_retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: Casemark) -> None:
        v1 = client.workflows.v1.search(
            query="query",
        )
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Casemark) -> None:
        v1 = client.workflows.v1.search(
            query="query",
            category="category",
            limit=1,
        )
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Casemark) -> None:
        response = client.workflows.v1.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Casemark) -> None:
        with client.workflows.v1.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasemark) -> None:
        v1 = await async_client.workflows.v1.retrieve(
            "id",
        )
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasemark) -> None:
        response = await async_client.workflows.v1.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasemark) -> None:
        async with async_client.workflows.v1.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasemark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workflows.v1.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCasemark) -> None:
        v1 = await async_client.workflows.v1.list()
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasemark) -> None:
        v1 = await async_client.workflows.v1.list(
            category="category",
            limit=1,
            offset=0,
            published=True,
            sub_category="sub_category",
            type="type",
        )
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasemark) -> None:
        response = await async_client.workflows.v1.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasemark) -> None:
        async with async_client.workflows.v1.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute(self, async_client: AsyncCasemark) -> None:
        v1 = await async_client.workflows.v1.execute(
            id="id",
            input={},
        )
        assert_matches_type(V1ExecuteResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncCasemark) -> None:
        v1 = await async_client.workflows.v1.execute(
            id="id",
            input={},
            options={
                "format": "json",
                "model": "model",
            },
        )
        assert_matches_type(V1ExecuteResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncCasemark) -> None:
        response = await async_client.workflows.v1.with_raw_response.execute(
            id="id",
            input={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ExecuteResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncCasemark) -> None:
        async with async_client.workflows.v1.with_streaming_response.execute(
            id="id",
            input={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ExecuteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_execute(self, async_client: AsyncCasemark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workflows.v1.with_raw_response.execute(
                id="",
                input={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execution_retrieve(self, async_client: AsyncCasemark) -> None:
        v1 = await async_client.workflows.v1.execution_retrieve(
            "exec_abc123def456",
        )
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_execution_retrieve(self, async_client: AsyncCasemark) -> None:
        response = await async_client.workflows.v1.with_raw_response.execution_retrieve(
            "exec_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_execution_retrieve(self, async_client: AsyncCasemark) -> None:
        async with async_client.workflows.v1.with_streaming_response.execution_retrieve(
            "exec_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_execution_retrieve(self, async_client: AsyncCasemark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workflows.v1.with_raw_response.execution_retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncCasemark) -> None:
        v1 = await async_client.workflows.v1.search(
            query="query",
        )
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncCasemark) -> None:
        v1 = await async_client.workflows.v1.search(
            query="query",
            category="category",
            limit=1,
        )
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncCasemark) -> None:
        response = await async_client.workflows.v1.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncCasemark) -> None:
        async with async_client.workflows.v1.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True
