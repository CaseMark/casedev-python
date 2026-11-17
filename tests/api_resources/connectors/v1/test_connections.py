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
    ConnectionSearchResponse,
    ConnectionRetrieveResponse,
    ConnectionResolveLinkResponse,
    ConnectionListContentsResponse,
    ConnectionCreateMicrosoftAdminApprovalResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.create(
            provider="box",
            return_url="return_url",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.create(
            provider="box",
            return_url="return_url",
            scope_tier="box.readwrite",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.connectors.v1.connections.with_raw_response.create(
            provider="box",
            return_url="return_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.connectors.v1.connections.with_streaming_response.create(
            provider="box",
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
            id="id",
        )
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.retrieve(
            id="id",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.connectors.v1.connections.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.connectors.v1.connections.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.connections.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.list()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.list(
            cursor="cursor",
            limit=1,
            provider="provider",
            status="pending",
            x_case_connector_subject="x-case-connector-subject",
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
            x_case_connector_subject="x-case-connector-subject",
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
            x_case_connector_subject="x-case-connector-subject",
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

    @parametrize
    def test_method_create_folder(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.create_folder(
            id="id",
            name="name",
        )
        assert connection is None

    @parametrize
    def test_method_create_folder_with_all_params(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.create_folder(
            id="id",
            name="name",
            container="container",
            parent="parent",
            site="site",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert connection is None

    @parametrize
    def test_raw_response_create_folder(self, client: Casedev) -> None:
        response = client.connectors.v1.connections.with_raw_response.create_folder(
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert connection is None

    @parametrize
    def test_streaming_response_create_folder(self, client: Casedev) -> None:
        with client.connectors.v1.connections.with_streaming_response.create_folder(
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_folder(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.connections.with_raw_response.create_folder(
                id="",
                name="name",
            )

    @parametrize
    def test_method_create_microsoft_admin_approval(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.create_microsoft_admin_approval(
            id="id",
        )
        assert_matches_type(ConnectionCreateMicrosoftAdminApprovalResponse, connection, path=["response"])

    @parametrize
    def test_method_create_microsoft_admin_approval_with_all_params(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.create_microsoft_admin_approval(
            id="id",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert_matches_type(ConnectionCreateMicrosoftAdminApprovalResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_create_microsoft_admin_approval(self, client: Casedev) -> None:
        response = client.connectors.v1.connections.with_raw_response.create_microsoft_admin_approval(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionCreateMicrosoftAdminApprovalResponse, connection, path=["response"])

    @parametrize
    def test_streaming_response_create_microsoft_admin_approval(self, client: Casedev) -> None:
        with client.connectors.v1.connections.with_streaming_response.create_microsoft_admin_approval(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionCreateMicrosoftAdminApprovalResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_microsoft_admin_approval(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.connections.with_raw_response.create_microsoft_admin_approval(
                id="",
            )

    @parametrize
    def test_method_list_contents(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.list_contents(
            id="id",
        )
        assert_matches_type(ConnectionListContentsResponse, connection, path=["response"])

    @parametrize
    def test_method_list_contents_with_all_params(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.list_contents(
            id="id",
            container="container",
            cursor="cursor",
            page_size=1,
            parent="parent",
            site="site",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert_matches_type(ConnectionListContentsResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_list_contents(self, client: Casedev) -> None:
        response = client.connectors.v1.connections.with_raw_response.list_contents(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionListContentsResponse, connection, path=["response"])

    @parametrize
    def test_streaming_response_list_contents(self, client: Casedev) -> None:
        with client.connectors.v1.connections.with_streaming_response.list_contents(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionListContentsResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_contents(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.connections.with_raw_response.list_contents(
                id="",
            )

    @parametrize
    def test_method_resolve_link(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.resolve_link(
            id="id",
            url="url",
        )
        assert_matches_type(ConnectionResolveLinkResponse, connection, path=["response"])

    @parametrize
    def test_method_resolve_link_with_all_params(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.resolve_link(
            id="id",
            url="url",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert_matches_type(ConnectionResolveLinkResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_resolve_link(self, client: Casedev) -> None:
        response = client.connectors.v1.connections.with_raw_response.resolve_link(
            id="id",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionResolveLinkResponse, connection, path=["response"])

    @parametrize
    def test_streaming_response_resolve_link(self, client: Casedev) -> None:
        with client.connectors.v1.connections.with_streaming_response.resolve_link(
            id="id",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionResolveLinkResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resolve_link(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.connections.with_raw_response.resolve_link(
                id="",
                url="url",
            )

    @parametrize
    def test_method_search(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.search(
            id="id",
            query="query",
        )
        assert_matches_type(ConnectionSearchResponse, connection, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.search(
            id="id",
            query="query",
            container="container",
            cursor="cursor",
            kind="file",
            page_size=1000,
            parent="parent",
            site="site",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert_matches_type(ConnectionSearchResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Casedev) -> None:
        response = client.connectors.v1.connections.with_raw_response.search(
            id="id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionSearchResponse, connection, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Casedev) -> None:
        with client.connectors.v1.connections.with_streaming_response.search(
            id="id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionSearchResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.connections.with_raw_response.search(
                id="",
                query="query",
            )

    @parametrize
    def test_method_update_all(self, client: Casedev) -> None:
        connection = client.connectors.v1.connections.update_all(
            confirm_organization_wide=True,
            enabled=True,
            provider="provider",
        )
        assert connection is None

    @parametrize
    def test_raw_response_update_all(self, client: Casedev) -> None:
        response = client.connectors.v1.connections.with_raw_response.update_all(
            confirm_organization_wide=True,
            enabled=True,
            provider="provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert connection is None

    @parametrize
    def test_streaming_response_update_all(self, client: Casedev) -> None:
        with client.connectors.v1.connections.with_streaming_response.update_all(
            confirm_organization_wide=True,
            enabled=True,
            provider="provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.create(
            provider="box",
            return_url="return_url",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.create(
            provider="box",
            return_url="return_url",
            scope_tier="box.readwrite",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.connections.with_raw_response.create(
            provider="box",
            return_url="return_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.connections.with_streaming_response.create(
            provider="box",
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
            id="id",
        )
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.retrieve(
            id="id",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.connections.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.connections.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.connections.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.list()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.list(
            cursor="cursor",
            limit=1,
            provider="provider",
            status="pending",
            x_case_connector_subject="x-case-connector-subject",
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
            x_case_connector_subject="x-case-connector-subject",
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
            x_case_connector_subject="x-case-connector-subject",
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

    @parametrize
    async def test_method_create_folder(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.create_folder(
            id="id",
            name="name",
        )
        assert connection is None

    @parametrize
    async def test_method_create_folder_with_all_params(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.create_folder(
            id="id",
            name="name",
            container="container",
            parent="parent",
            site="site",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert connection is None

    @parametrize
    async def test_raw_response_create_folder(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.connections.with_raw_response.create_folder(
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert connection is None

    @parametrize
    async def test_streaming_response_create_folder(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.connections.with_streaming_response.create_folder(
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_folder(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.connections.with_raw_response.create_folder(
                id="",
                name="name",
            )

    @parametrize
    async def test_method_create_microsoft_admin_approval(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.create_microsoft_admin_approval(
            id="id",
        )
        assert_matches_type(ConnectionCreateMicrosoftAdminApprovalResponse, connection, path=["response"])

    @parametrize
    async def test_method_create_microsoft_admin_approval_with_all_params(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.create_microsoft_admin_approval(
            id="id",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert_matches_type(ConnectionCreateMicrosoftAdminApprovalResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_create_microsoft_admin_approval(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.connections.with_raw_response.create_microsoft_admin_approval(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionCreateMicrosoftAdminApprovalResponse, connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_microsoft_admin_approval(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.connections.with_streaming_response.create_microsoft_admin_approval(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionCreateMicrosoftAdminApprovalResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_microsoft_admin_approval(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.connections.with_raw_response.create_microsoft_admin_approval(
                id="",
            )

    @parametrize
    async def test_method_list_contents(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.list_contents(
            id="id",
        )
        assert_matches_type(ConnectionListContentsResponse, connection, path=["response"])

    @parametrize
    async def test_method_list_contents_with_all_params(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.list_contents(
            id="id",
            container="container",
            cursor="cursor",
            page_size=1,
            parent="parent",
            site="site",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert_matches_type(ConnectionListContentsResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_list_contents(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.connections.with_raw_response.list_contents(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionListContentsResponse, connection, path=["response"])

    @parametrize
    async def test_streaming_response_list_contents(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.connections.with_streaming_response.list_contents(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionListContentsResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_contents(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.connections.with_raw_response.list_contents(
                id="",
            )

    @parametrize
    async def test_method_resolve_link(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.resolve_link(
            id="id",
            url="url",
        )
        assert_matches_type(ConnectionResolveLinkResponse, connection, path=["response"])

    @parametrize
    async def test_method_resolve_link_with_all_params(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.resolve_link(
            id="id",
            url="url",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert_matches_type(ConnectionResolveLinkResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_resolve_link(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.connections.with_raw_response.resolve_link(
            id="id",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionResolveLinkResponse, connection, path=["response"])

    @parametrize
    async def test_streaming_response_resolve_link(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.connections.with_streaming_response.resolve_link(
            id="id",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionResolveLinkResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resolve_link(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.connections.with_raw_response.resolve_link(
                id="",
                url="url",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.search(
            id="id",
            query="query",
        )
        assert_matches_type(ConnectionSearchResponse, connection, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.search(
            id="id",
            query="query",
            container="container",
            cursor="cursor",
            kind="file",
            page_size=1000,
            parent="parent",
            site="site",
            x_case_connector_subject="x-case-connector-subject",
        )
        assert_matches_type(ConnectionSearchResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.connections.with_raw_response.search(
            id="id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionSearchResponse, connection, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.connections.with_streaming_response.search(
            id="id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionSearchResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.connections.with_raw_response.search(
                id="",
                query="query",
            )

    @parametrize
    async def test_method_update_all(self, async_client: AsyncCasedev) -> None:
        connection = await async_client.connectors.v1.connections.update_all(
            confirm_organization_wide=True,
            enabled=True,
            provider="provider",
        )
        assert connection is None

    @parametrize
    async def test_raw_response_update_all(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.connections.with_raw_response.update_all(
            confirm_organization_wide=True,
            enabled=True,
            provider="provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert connection is None

    @parametrize
    async def test_streaming_response_update_all(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.connections.with_streaming_response.update_all(
            confirm_organization_wide=True,
            enabled=True,
            provider="provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True
