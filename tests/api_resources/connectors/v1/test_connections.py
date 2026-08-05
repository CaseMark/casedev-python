# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.connectors.v1 import (
    ConnectionListResponse,
    ConnectionBrowseResponse,
    ConnectionCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.create(
            provider="clio",
            return_url="return_url",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.create(
            provider="clio",
            return_url="return_url",
            scope_tier="clio.us",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.connectors.v1.connections.with_raw_response.create(
            provider="clio",
            return_url="return_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.connectors.v1.connections.with_streaming_response.create(
            provider="clio",
            return_url="return_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.retrieve(
            "id",
        )
        assert connection is None

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.connectors.v1.connections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert connection is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.connectors.v1.connections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.connections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.list()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.list(
            provider="provider",
            status="pending",
        )
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.connectors.v1.connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.connectors.v1.connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.delete(
            id="id",
        )
        assert connection is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.delete(
            id="id",
            purge=True,
        )
        assert connection is None

    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.connectors.v1.connections.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert connection is None

    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.connectors.v1.connections.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.connections.with_raw_response.delete(
                id="",
            )

    @parametrize
    def test_method_browse(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.browse(
            id="id",
        )
        assert_matches_type(ConnectionBrowseResponse, connection, path=["response"])

    @parametrize
    def test_method_browse_with_all_params(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.browse(
            id="id",
            container="container",
            cursor="cursor",
            page_size=1000,
            parent="parent",
            query="query",
            site="site",
        )
        assert_matches_type(ConnectionBrowseResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_browse(self, client: Casedev) -> None:
        response = client.connectors.v1.connections.with_raw_response.browse(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionBrowseResponse, connection, path=["response"])

    @parametrize
    def test_streaming_response_browse(self, client: Casedev) -> None:
        with client.connectors.v1.connections.with_streaming_response.browse(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionBrowseResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_browse(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.connections.with_raw_response.browse(
                id="",
            )


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.create(
            provider="clio",
            return_url="return_url",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.create(
            provider="clio",
            return_url="return_url",
            scope_tier="clio.us",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.connections.with_raw_response.create(
            provider="clio",
            return_url="return_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.connections.with_streaming_response.create(
            provider="clio",
            return_url="return_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.retrieve(
            "id",
        )
        assert connection is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.connections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert connection is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.connections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.connections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.list()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.list(
            provider="provider",
            status="pending",
        )
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.delete(
            id="id",
        )
        assert connection is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.delete(
            id="id",
            purge=True,
        )
        assert connection is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.connections.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert connection is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.connections.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.connections.with_raw_response.delete(
                id="",
            )

    @parametrize
    async def test_method_browse(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.browse(
            id="id",
        )
        assert_matches_type(ConnectionBrowseResponse, connection, path=["response"])

    @parametrize
    async def test_method_browse_with_all_params(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.browse(
            id="id",
            container="container",
            cursor="cursor",
            page_size=1000,
            parent="parent",
            query="query",
            site="site",
        )
        assert_matches_type(ConnectionBrowseResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_browse(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.connections.with_raw_response.browse(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionBrowseResponse, connection, path=["response"])

    @parametrize
    async def test_streaming_response_browse(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.connections.with_streaming_response.browse(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionBrowseResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_browse(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.connections.with_raw_response.browse(
                id="",
            )
