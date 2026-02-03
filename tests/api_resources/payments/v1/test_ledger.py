# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from casedev._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedger:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Casedev) -> None:
        ledger = client.payments.v1.ledger.get()
        assert ledger is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Casedev) -> None:
        ledger = client.payments.v1.ledger.get(
            account_id="account_id",
            limit=0,
            offset=0,
            transaction_id="transaction_id",
        )
        assert ledger is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Casedev) -> None:
        response = client.payments.v1.ledger.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert ledger is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Casedev) -> None:
        with client.payments.v1.ledger.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert ledger is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_transactions(self, client: Casedev) -> None:
        ledger = client.payments.v1.ledger.list_transactions()
        assert ledger is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_transactions_with_all_params(self, client: Casedev) -> None:
        ledger = client.payments.v1.ledger.list_transactions(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
            reference_id="reference_id",
            reference_type="reference_type",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert ledger is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_transactions(self, client: Casedev) -> None:
        response = client.payments.v1.ledger.with_raw_response.list_transactions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert ledger is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_transactions(self, client: Casedev) -> None:
        with client.payments.v1.ledger.with_streaming_response.list_transactions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert ledger is None

        assert cast(Any, response.is_closed) is True


class TestAsyncLedger:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncCasedev) -> None:
        ledger = await async_client.payments.v1.ledger.get()
        assert ledger is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCasedev) -> None:
        ledger = await async_client.payments.v1.ledger.get(
            account_id="account_id",
            limit=0,
            offset=0,
            transaction_id="transaction_id",
        )
        assert ledger is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.ledger.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = await response.parse()
        assert ledger is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.ledger.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert ledger is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_transactions(self, async_client: AsyncCasedev) -> None:
        ledger = await async_client.payments.v1.ledger.list_transactions()
        assert ledger is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_transactions_with_all_params(self, async_client: AsyncCasedev) -> None:
        ledger = await async_client.payments.v1.ledger.list_transactions(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            offset=0,
            reference_id="reference_id",
            reference_type="reference_type",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert ledger is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_transactions(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.ledger.with_raw_response.list_transactions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = await response.parse()
        assert ledger is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_transactions(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.ledger.with_streaming_response.list_transactions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert ledger is None

        assert cast(Any, response.is_closed) is True
