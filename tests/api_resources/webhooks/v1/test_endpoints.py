# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEndpoints:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        endpoint = client.webhooks.v1.endpoints.create(
            event_type_filters=["string"],
            url="https://example.com",
        )
        assert endpoint is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        endpoint = client.webhooks.v1.endpoints.create(
            event_type_filters=["string"],
            url="https://example.com",
            description="description",
            resource_scopes={
                "matter_ids": ["string"],
                "vault_ids": ["string"],
            },
        )
        assert endpoint is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.webhooks.v1.endpoints.with_raw_response.create(
            event_type_filters=["string"],
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = response.parse()
        assert endpoint is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.webhooks.v1.endpoints.with_streaming_response.create(
            event_type_filters=["string"],
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        endpoint = client.webhooks.v1.endpoints.retrieve(
            "id",
        )
        assert endpoint is None

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.webhooks.v1.endpoints.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = response.parse()
        assert endpoint is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.webhooks.v1.endpoints.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.v1.endpoints.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Casedev) -> None:
        endpoint = client.webhooks.v1.endpoints.update(
            id="id",
        )
        assert endpoint is None

    @parametrize
    def test_method_update_with_all_params(self, client: Casedev) -> None:
        endpoint = client.webhooks.v1.endpoints.update(
            id="id",
            description="description",
            event_type_filters=["string"],
            resource_scopes={
                "matter_ids": ["string"],
                "vault_ids": ["string"],
            },
            status="active",
            url="https://example.com",
        )
        assert endpoint is None

    @parametrize
    def test_raw_response_update(self, client: Casedev) -> None:
        response = client.webhooks.v1.endpoints.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = response.parse()
        assert endpoint is None

    @parametrize
    def test_streaming_response_update(self, client: Casedev) -> None:
        with client.webhooks.v1.endpoints.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.v1.endpoints.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        endpoint = client.webhooks.v1.endpoints.list()
        assert endpoint is None

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        endpoint = client.webhooks.v1.endpoints.list(
            limit=1,
            status="active",
        )
        assert endpoint is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.webhooks.v1.endpoints.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = response.parse()
        assert endpoint is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.webhooks.v1.endpoints.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        endpoint = client.webhooks.v1.endpoints.delete(
            "id",
        )
        assert endpoint is None

    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.webhooks.v1.endpoints.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = response.parse()
        assert endpoint is None

    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.webhooks.v1.endpoints.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.v1.endpoints.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_rotate_secret(self, client: Casedev) -> None:
        endpoint = client.webhooks.v1.endpoints.rotate_secret(
            id="id",
        )
        assert endpoint is None

    @parametrize
    def test_method_rotate_secret_with_all_params(self, client: Casedev) -> None:
        endpoint = client.webhooks.v1.endpoints.rotate_secret(
            id="id",
            previous_secret_expires_in_sec=0,
        )
        assert endpoint is None

    @parametrize
    def test_raw_response_rotate_secret(self, client: Casedev) -> None:
        response = client.webhooks.v1.endpoints.with_raw_response.rotate_secret(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = response.parse()
        assert endpoint is None

    @parametrize
    def test_streaming_response_rotate_secret(self, client: Casedev) -> None:
        with client.webhooks.v1.endpoints.with_streaming_response.rotate_secret(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rotate_secret(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.v1.endpoints.with_raw_response.rotate_secret(
                id="",
            )

    @parametrize
    def test_method_test(self, client: Casedev) -> None:
        endpoint = client.webhooks.v1.endpoints.test(
            id="id",
        )
        assert endpoint is None

    @parametrize
    def test_method_test_with_all_params(self, client: Casedev) -> None:
        endpoint = client.webhooks.v1.endpoints.test(
            id="id",
            event_type="eventType",
            payload={},
        )
        assert endpoint is None

    @parametrize
    def test_raw_response_test(self, client: Casedev) -> None:
        response = client.webhooks.v1.endpoints.with_raw_response.test(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = response.parse()
        assert endpoint is None

    @parametrize
    def test_streaming_response_test(self, client: Casedev) -> None:
        with client.webhooks.v1.endpoints.with_streaming_response.test(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_test(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.v1.endpoints.with_raw_response.test(
                id="",
            )


class TestAsyncEndpoints:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        endpoint = await async_client.webhooks.v1.endpoints.create(
            event_type_filters=["string"],
            url="https://example.com",
        )
        assert endpoint is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        endpoint = await async_client.webhooks.v1.endpoints.create(
            event_type_filters=["string"],
            url="https://example.com",
            description="description",
            resource_scopes={
                "matter_ids": ["string"],
                "vault_ids": ["string"],
            },
        )
        assert endpoint is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.webhooks.v1.endpoints.with_raw_response.create(
            event_type_filters=["string"],
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = await response.parse()
        assert endpoint is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.webhooks.v1.endpoints.with_streaming_response.create(
            event_type_filters=["string"],
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = await response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        endpoint = await async_client.webhooks.v1.endpoints.retrieve(
            "id",
        )
        assert endpoint is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.webhooks.v1.endpoints.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = await response.parse()
        assert endpoint is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.webhooks.v1.endpoints.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = await response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.v1.endpoints.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCasedev) -> None:
        endpoint = await async_client.webhooks.v1.endpoints.update(
            id="id",
        )
        assert endpoint is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCasedev) -> None:
        endpoint = await async_client.webhooks.v1.endpoints.update(
            id="id",
            description="description",
            event_type_filters=["string"],
            resource_scopes={
                "matter_ids": ["string"],
                "vault_ids": ["string"],
            },
            status="active",
            url="https://example.com",
        )
        assert endpoint is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCasedev) -> None:
        response = await async_client.webhooks.v1.endpoints.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = await response.parse()
        assert endpoint is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCasedev) -> None:
        async with async_client.webhooks.v1.endpoints.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = await response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.v1.endpoints.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        endpoint = await async_client.webhooks.v1.endpoints.list()
        assert endpoint is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        endpoint = await async_client.webhooks.v1.endpoints.list(
            limit=1,
            status="active",
        )
        assert endpoint is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.webhooks.v1.endpoints.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = await response.parse()
        assert endpoint is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.webhooks.v1.endpoints.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = await response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        endpoint = await async_client.webhooks.v1.endpoints.delete(
            "id",
        )
        assert endpoint is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.webhooks.v1.endpoints.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = await response.parse()
        assert endpoint is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.webhooks.v1.endpoints.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = await response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.v1.endpoints.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_rotate_secret(self, async_client: AsyncCasedev) -> None:
        endpoint = await async_client.webhooks.v1.endpoints.rotate_secret(
            id="id",
        )
        assert endpoint is None

    @parametrize
    async def test_method_rotate_secret_with_all_params(self, async_client: AsyncCasedev) -> None:
        endpoint = await async_client.webhooks.v1.endpoints.rotate_secret(
            id="id",
            previous_secret_expires_in_sec=0,
        )
        assert endpoint is None

    @parametrize
    async def test_raw_response_rotate_secret(self, async_client: AsyncCasedev) -> None:
        response = await async_client.webhooks.v1.endpoints.with_raw_response.rotate_secret(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = await response.parse()
        assert endpoint is None

    @parametrize
    async def test_streaming_response_rotate_secret(self, async_client: AsyncCasedev) -> None:
        async with async_client.webhooks.v1.endpoints.with_streaming_response.rotate_secret(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = await response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rotate_secret(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.v1.endpoints.with_raw_response.rotate_secret(
                id="",
            )

    @parametrize
    async def test_method_test(self, async_client: AsyncCasedev) -> None:
        endpoint = await async_client.webhooks.v1.endpoints.test(
            id="id",
        )
        assert endpoint is None

    @parametrize
    async def test_method_test_with_all_params(self, async_client: AsyncCasedev) -> None:
        endpoint = await async_client.webhooks.v1.endpoints.test(
            id="id",
            event_type="eventType",
            payload={},
        )
        assert endpoint is None

    @parametrize
    async def test_raw_response_test(self, async_client: AsyncCasedev) -> None:
        response = await async_client.webhooks.v1.endpoints.with_raw_response.test(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = await response.parse()
        assert endpoint is None

    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncCasedev) -> None:
        async with async_client.webhooks.v1.endpoints.with_streaming_response.test(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = await response.parse()
            assert endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_test(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.v1.endpoints.with_raw_response.test(
                id="",
            )
