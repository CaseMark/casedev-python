# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        link = client.connectors.v1.links.retrieve(
            "id",
        )
        assert link is None

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.connectors.v1.links.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert link is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.connectors.v1.links.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert link is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.links.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Casedev) -> None:
        link = client.connectors.v1.links.update(
            id="id",
        )
        assert link is None

    @parametrize
    def test_method_update_with_all_params(self, client: Casedev) -> None:
        link = client.connectors.v1.links.update(
            id="id",
            mode="once",
            policy={},
            state="paused",
        )
        assert link is None

    @parametrize
    def test_raw_response_update(self, client: Casedev) -> None:
        response = client.connectors.v1.links.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert link is None

    @parametrize
    def test_streaming_response_update(self, client: Casedev) -> None:
        with client.connectors.v1.links.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert link is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.links.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        link = client.connectors.v1.links.list()
        assert link is None

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        link = client.connectors.v1.links.list(
            connection_id="connection_id",
            direction="import",
            mode="once",
            pair_id="pair_id",
            state="ready",
            vault_id="vault_id",
        )
        assert link is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.connectors.v1.links.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert link is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.connectors.v1.links.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert link is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        link = client.connectors.v1.links.delete(
            id="id",
        )
        assert link is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Casedev) -> None:
        link = client.connectors.v1.links.delete(
            id="id",
            vault_docs="keep",
        )
        assert link is None

    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.connectors.v1.links.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert link is None

    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.connectors.v1.links.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert link is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.links.with_raw_response.delete(
                id="",
            )

    @parametrize
    def test_method_list_objects(self, client: Casedev) -> None:
        link = client.connectors.v1.links.list_objects(
            id="id",
        )
        assert link is None

    @parametrize
    def test_method_list_objects_with_all_params(self, client: Casedev) -> None:
        link = client.connectors.v1.links.list_objects(
            id="id",
            cursor="cursor",
            state="pending",
        )
        assert link is None

    @parametrize
    def test_raw_response_list_objects(self, client: Casedev) -> None:
        response = client.connectors.v1.links.with_raw_response.list_objects(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert link is None

    @parametrize
    def test_streaming_response_list_objects(self, client: Casedev) -> None:
        with client.connectors.v1.links.with_streaming_response.list_objects(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert link is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_objects(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.links.with_raw_response.list_objects(
                id="",
            )


class TestAsyncLinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        link = await async_client.connectors.v1.links.retrieve(
            "id",
        )
        assert link is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.links.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert link is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.links.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert link is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.links.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCasedev) -> None:
        link = await async_client.connectors.v1.links.update(
            id="id",
        )
        assert link is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCasedev) -> None:
        link = await async_client.connectors.v1.links.update(
            id="id",
            mode="once",
            policy={},
            state="paused",
        )
        assert link is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.links.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert link is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.links.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert link is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.links.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        link = await async_client.connectors.v1.links.list()
        assert link is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        link = await async_client.connectors.v1.links.list(
            connection_id="connection_id",
            direction="import",
            mode="once",
            pair_id="pair_id",
            state="ready",
            vault_id="vault_id",
        )
        assert link is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.links.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert link is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.links.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert link is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        link = await async_client.connectors.v1.links.delete(
            id="id",
        )
        assert link is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCasedev) -> None:
        link = await async_client.connectors.v1.links.delete(
            id="id",
            vault_docs="keep",
        )
        assert link is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.links.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert link is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.links.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert link is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.links.with_raw_response.delete(
                id="",
            )

    @parametrize
    async def test_method_list_objects(self, async_client: AsyncCasedev) -> None:
        link = await async_client.connectors.v1.links.list_objects(
            id="id",
        )
        assert link is None

    @parametrize
    async def test_method_list_objects_with_all_params(self, async_client: AsyncCasedev) -> None:
        link = await async_client.connectors.v1.links.list_objects(
            id="id",
            cursor="cursor",
            state="pending",
        )
        assert link is None

    @parametrize
    async def test_raw_response_list_objects(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.links.with_raw_response.list_objects(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert link is None

    @parametrize
    async def test_streaming_response_list_objects(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.links.with_streaming_response.list_objects(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert link is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_objects(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.links.with_raw_response.list_objects(
                id="",
            )
