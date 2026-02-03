# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayouts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        payout = client.payments.v1.payouts.create(
            amount=0,
            destination_type="bank_account",
            from_account_id="from_account_id",
        )
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        payout = client.payments.v1.payouts.create(
            amount=0,
            destination_type="bank_account",
            from_account_id="from_account_id",
            currency="currency",
            memo="memo",
            metadata={},
            party_id="party_id",
        )
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.payments.v1.payouts.with_raw_response.create(
            amount=0,
            destination_type="bank_account",
            from_account_id="from_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = response.parse()
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.payments.v1.payouts.with_streaming_response.create(
            amount=0,
            destination_type="bank_account",
            from_account_id="from_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = response.parse()
            assert payout is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        payout = client.payments.v1.payouts.retrieve(
            "id",
        )
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.payments.v1.payouts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = response.parse()
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.payments.v1.payouts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = response.parse()
            assert payout is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.v1.payouts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        payout = client.payments.v1.payouts.list()
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        payout = client.payments.v1.payouts.list(
            from_account_id="from_account_id",
            limit=0,
            offset=0,
            party_id="party_id",
            status="pending",
        )
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.payments.v1.payouts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = response.parse()
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.payments.v1.payouts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = response.parse()
            assert payout is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Casedev) -> None:
        payout = client.payments.v1.payouts.cancel(
            "id",
        )
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Casedev) -> None:
        response = client.payments.v1.payouts.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = response.parse()
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Casedev) -> None:
        with client.payments.v1.payouts.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = response.parse()
            assert payout is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.v1.payouts.with_raw_response.cancel(
                "",
            )


class TestAsyncPayouts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        payout = await async_client.payments.v1.payouts.create(
            amount=0,
            destination_type="bank_account",
            from_account_id="from_account_id",
        )
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        payout = await async_client.payments.v1.payouts.create(
            amount=0,
            destination_type="bank_account",
            from_account_id="from_account_id",
            currency="currency",
            memo="memo",
            metadata={},
            party_id="party_id",
        )
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.payouts.with_raw_response.create(
            amount=0,
            destination_type="bank_account",
            from_account_id="from_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = await response.parse()
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.payouts.with_streaming_response.create(
            amount=0,
            destination_type="bank_account",
            from_account_id="from_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = await response.parse()
            assert payout is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        payout = await async_client.payments.v1.payouts.retrieve(
            "id",
        )
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.payouts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = await response.parse()
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.payouts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = await response.parse()
            assert payout is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.v1.payouts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        payout = await async_client.payments.v1.payouts.list()
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        payout = await async_client.payments.v1.payouts.list(
            from_account_id="from_account_id",
            limit=0,
            offset=0,
            party_id="party_id",
            status="pending",
        )
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.payouts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = await response.parse()
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.payouts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = await response.parse()
            assert payout is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncCasedev) -> None:
        payout = await async_client.payments.v1.payouts.cancel(
            "id",
        )
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.payouts.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = await response.parse()
        assert payout is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.payouts.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = await response.parse()
            assert payout is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.v1.payouts.with_raw_response.cancel(
                "",
            )
