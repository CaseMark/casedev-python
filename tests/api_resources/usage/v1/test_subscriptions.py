# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        subscription = client.usage.v1.subscriptions.create(
            callback_url="https://example.com",
        )
        assert subscription is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        subscription = client.usage.v1.subscriptions.create(
            callback_url="https://example.com",
            event_types=["string"],
            signing_secret="signingSecret",
        )
        assert subscription is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.usage.v1.subscriptions.with_raw_response.create(
            callback_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.usage.v1.subscriptions.with_streaming_response.create(
            callback_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Casedev) -> None:
        subscription = client.usage.v1.subscriptions.update(
            subscription_id="subscriptionId",
        )
        assert subscription is None

    @parametrize
    def test_method_update_with_all_params(self, client: Casedev) -> None:
        subscription = client.usage.v1.subscriptions.update(
            subscription_id="subscriptionId",
            callback_url="https://example.com",
            clear_signing_secret=True,
            event_types=["string"],
            is_active=True,
            signing_secret="signingSecret",
        )
        assert subscription is None

    @parametrize
    def test_raw_response_update(self, client: Casedev) -> None:
        response = client.usage.v1.subscriptions.with_raw_response.update(
            subscription_id="subscriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    def test_streaming_response_update(self, client: Casedev) -> None:
        with client.usage.v1.subscriptions.with_streaming_response.update(
            subscription_id="subscriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.usage.v1.subscriptions.with_raw_response.update(
                subscription_id="",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        subscription = client.usage.v1.subscriptions.list()
        assert subscription is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.usage.v1.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.usage.v1.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        subscription = client.usage.v1.subscriptions.delete(
            "subscriptionId",
        )
        assert subscription is None

    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.usage.v1.subscriptions.with_raw_response.delete(
            "subscriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.usage.v1.subscriptions.with_streaming_response.delete(
            "subscriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.usage.v1.subscriptions.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_test(self, client: Casedev) -> None:
        subscription = client.usage.v1.subscriptions.test(
            subscription_id="subscriptionId",
        )
        assert subscription is None

    @parametrize
    def test_method_test_with_all_params(self, client: Casedev) -> None:
        subscription = client.usage.v1.subscriptions.test(
            subscription_id="subscriptionId",
            event_type="eventType",
            payload={"foo": "bar"},
        )
        assert subscription is None

    @parametrize
    def test_raw_response_test(self, client: Casedev) -> None:
        response = client.usage.v1.subscriptions.with_raw_response.test(
            subscription_id="subscriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    def test_streaming_response_test(self, client: Casedev) -> None:
        with client.usage.v1.subscriptions.with_streaming_response.test(
            subscription_id="subscriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_test(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.usage.v1.subscriptions.with_raw_response.test(
                subscription_id="",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.usage.v1.subscriptions.create(
            callback_url="https://example.com",
        )
        assert subscription is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.usage.v1.subscriptions.create(
            callback_url="https://example.com",
            event_types=["string"],
            signing_secret="signingSecret",
        )
        assert subscription is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.usage.v1.subscriptions.with_raw_response.create(
            callback_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.usage.v1.subscriptions.with_streaming_response.create(
            callback_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.usage.v1.subscriptions.update(
            subscription_id="subscriptionId",
        )
        assert subscription is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.usage.v1.subscriptions.update(
            subscription_id="subscriptionId",
            callback_url="https://example.com",
            clear_signing_secret=True,
            event_types=["string"],
            is_active=True,
            signing_secret="signingSecret",
        )
        assert subscription is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCasedev) -> None:
        response = await async_client.usage.v1.subscriptions.with_raw_response.update(
            subscription_id="subscriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCasedev) -> None:
        async with async_client.usage.v1.subscriptions.with_streaming_response.update(
            subscription_id="subscriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.usage.v1.subscriptions.with_raw_response.update(
                subscription_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.usage.v1.subscriptions.list()
        assert subscription is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.usage.v1.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.usage.v1.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.usage.v1.subscriptions.delete(
            "subscriptionId",
        )
        assert subscription is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.usage.v1.subscriptions.with_raw_response.delete(
            "subscriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.usage.v1.subscriptions.with_streaming_response.delete(
            "subscriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.usage.v1.subscriptions.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_test(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.usage.v1.subscriptions.test(
            subscription_id="subscriptionId",
        )
        assert subscription is None

    @parametrize
    async def test_method_test_with_all_params(self, async_client: AsyncCasedev) -> None:
        subscription = await async_client.usage.v1.subscriptions.test(
            subscription_id="subscriptionId",
            event_type="eventType",
            payload={"foo": "bar"},
        )
        assert subscription is None

    @parametrize
    async def test_raw_response_test(self, async_client: AsyncCasedev) -> None:
        response = await async_client.usage.v1.subscriptions.with_raw_response.test(
            subscription_id="subscriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncCasedev) -> None:
        async with async_client.usage.v1.subscriptions.with_streaming_response.test(
            subscription_id="subscriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_test(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.usage.v1.subscriptions.with_raw_response.test(
                subscription_id="",
            )
