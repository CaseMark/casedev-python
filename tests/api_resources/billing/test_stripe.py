# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from router import Router, AsyncRouter
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStripe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_handle_webhook(self, client: Router) -> None:
        stripe = client.billing.stripe.handle_webhook(
            body={},
        )
        assert_matches_type(object, stripe, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_handle_webhook(self, client: Router) -> None:
        response = client.billing.stripe.with_raw_response.handle_webhook(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stripe = response.parse()
        assert_matches_type(object, stripe, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_handle_webhook(self, client: Router) -> None:
        with client.billing.stripe.with_streaming_response.handle_webhook(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stripe = response.parse()
            assert_matches_type(object, stripe, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStripe:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_handle_webhook(self, async_client: AsyncRouter) -> None:
        stripe = await async_client.billing.stripe.handle_webhook(
            body={},
        )
        assert_matches_type(object, stripe, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_handle_webhook(self, async_client: AsyncRouter) -> None:
        response = await async_client.billing.stripe.with_raw_response.handle_webhook(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stripe = await response.parse()
        assert_matches_type(object, stripe, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_handle_webhook(self, async_client: AsyncRouter) -> None:
        async with async_client.billing.stripe.with_streaming_response.handle_webhook(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stripe = await response.parse()
            assert_matches_type(object, stripe, path=["response"])

        assert cast(Any, response.is_closed) is True
