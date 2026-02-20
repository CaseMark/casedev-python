# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        subscription = client.vault.events.subscriptions.create(
            id="id",
            callback_url="https://example.com",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        subscription = client.vault.events.subscriptions.create(
            id="id",
            callback_url="https://example.com",
            event_types=["string"],
            object_ids=["string"],
            signing_secret="signingSecret",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.vault.events.subscriptions.with_raw_response.create(
            id="id",
            callback_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.vault.events.subscriptions.with_streaming_response.create(
            id="id",
            callback_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.events.subscriptions.with_raw_response.create(
                id="",
                callback_url="https://example.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Casedev) -> None:
        subscription = client.vault.events.subscriptions.update(
            subscription_id="subscriptionId",
            id="id",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Casedev) -> None:
        subscription = client.vault.events.subscriptions.update(
            subscription_id="subscriptionId",
            id="id",
            callback_url="https://example.com",
            clear_signing_secret=True,
            event_types=["string"],
            is_active=True,
            object_ids=["string"],
            signing_secret="signingSecret",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Casedev) -> None:
        response = client.vault.events.subscriptions.with_raw_response.update(
            subscription_id="subscriptionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Casedev) -> None:
        with client.vault.events.subscriptions.with_streaming_response.update(
            subscription_id="subscriptionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.events.subscriptions.with_raw_response.update(
                subscription_id="subscriptionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.vault.events.subscriptions.with_raw_response.update(
                subscription_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        subscription = client.vault.events.subscriptions.list(
            "id",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.vault.events.subscriptions.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.vault.events.subscriptions.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.events.subscriptions.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        subscription = client.vault.events.subscriptions.delete(
            subscription_id="subscriptionId",
            id="id",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.vault.events.subscriptions.with_raw_response.delete(
            subscription_id="subscriptionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.vault.events.subscriptions.with_streaming_response.delete(
            subscription_id="subscriptionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.events.subscriptions.with_raw_response.delete(
                subscription_id="subscriptionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.vault.events.subscriptions.with_raw_response.delete(
                subscription_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test(self, client: Casedev) -> None:
        subscription = client.vault.events.subscriptions.test(
            subscription_id="subscriptionId",
            id="id",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_with_all_params(self, client: Casedev) -> None:
        subscription = client.vault.events.subscriptions.test(
            subscription_id="subscriptionId",
            id="id",
            event_type="eventType",
            object_id="objectId",
            payload={"foo": "bar"},
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: Casedev) -> None:
        response = client.vault.events.subscriptions.with_raw_response.test(
            subscription_id="subscriptionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: Casedev) -> None:
        with client.vault.events.subscriptions.with_streaming_response.test(
            subscription_id="subscriptionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.events.subscriptions.with_raw_response.test(
                subscription_id="subscriptionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.vault.events.subscriptions.with_raw_response.test(
                subscription_id="",
                id="id",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.vault.events.subscriptions.create(
            id="id",
            callback_url="https://example.com",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.vault.events.subscriptions.create(
            id="id",
            callback_url="https://example.com",
            event_types=["string"],
            object_ids=["string"],
            signing_secret="signingSecret",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.events.subscriptions.with_raw_response.create(
            id="id",
            callback_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.events.subscriptions.with_streaming_response.create(
            id="id",
            callback_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.events.subscriptions.with_raw_response.create(
                id="",
                callback_url="https://example.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.vault.events.subscriptions.update(
            subscription_id="subscriptionId",
            id="id",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.vault.events.subscriptions.update(
            subscription_id="subscriptionId",
            id="id",
            callback_url="https://example.com",
            clear_signing_secret=True,
            event_types=["string"],
            is_active=True,
            object_ids=["string"],
            signing_secret="signingSecret",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.events.subscriptions.with_raw_response.update(
            subscription_id="subscriptionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.events.subscriptions.with_streaming_response.update(
            subscription_id="subscriptionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.events.subscriptions.with_raw_response.update(
                subscription_id="subscriptionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.vault.events.subscriptions.with_raw_response.update(
                subscription_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.vault.events.subscriptions.list(
            "id",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.events.subscriptions.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.events.subscriptions.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.events.subscriptions.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.vault.events.subscriptions.delete(
            subscription_id="subscriptionId",
            id="id",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.events.subscriptions.with_raw_response.delete(
            subscription_id="subscriptionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.events.subscriptions.with_streaming_response.delete(
            subscription_id="subscriptionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.events.subscriptions.with_raw_response.delete(
                subscription_id="subscriptionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.vault.events.subscriptions.with_raw_response.delete(
                subscription_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.vault.events.subscriptions.test(
            subscription_id="subscriptionId",
            id="id",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_with_all_params(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.vault.events.subscriptions.test(
            subscription_id="subscriptionId",
            id="id",
            event_type="eventType",
            object_id="objectId",
            payload={"foo": "bar"},
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.events.subscriptions.with_raw_response.test(
            subscription_id="subscriptionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.events.subscriptions.with_streaming_response.test(
            subscription_id="subscriptionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.events.subscriptions.with_raw_response.test(
                subscription_id="subscriptionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.vault.events.subscriptions.with_raw_response.test(
                subscription_id="",
                id="id",
            )
