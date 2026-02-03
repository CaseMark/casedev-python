# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        party = client.payments.v1.parties.create(
            name="name",
            type="individual",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        party = client.payments.v1.parties.create(
            name="name",
            type="individual",
            address_line1="address_line1",
            city="city",
            country="country",
            email="email",
            metadata={},
            phone="phone",
            postal_code="postal_code",
            role="client",
            state="state",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.payments.v1.parties.with_raw_response.create(
            name="name",
            type="individual",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = response.parse()
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.payments.v1.parties.with_streaming_response.create(
            name="name",
            type="individual",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        party = client.payments.v1.parties.retrieve(
            "id",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.payments.v1.parties.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = response.parse()
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.payments.v1.parties.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.v1.parties.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Casedev) -> None:
        party = client.payments.v1.parties.update(
            id="id",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Casedev) -> None:
        party = client.payments.v1.parties.update(
            id="id",
            address_line1="address_line1",
            address_line2="address_line2",
            city="city",
            country="country",
            email="email",
            is_active=True,
            metadata={},
            name="name",
            notes="notes",
            phone="phone",
            postal_code="postal_code",
            role="client",
            state="state",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Casedev) -> None:
        response = client.payments.v1.parties.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = response.parse()
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Casedev) -> None:
        with client.payments.v1.parties.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.v1.parties.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        party = client.payments.v1.parties.list()
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        party = client.payments.v1.parties.list(
            limit=0,
            offset=0,
            role="role",
            type="type",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.payments.v1.parties.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = response.parse()
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.payments.v1.parties.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_payment_methods(self, client: Casedev) -> None:
        party = client.payments.v1.parties.list_payment_methods(
            "id",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_payment_methods(self, client: Casedev) -> None:
        response = client.payments.v1.parties.with_raw_response.list_payment_methods(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = response.parse()
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_payment_methods(self, client: Casedev) -> None:
        with client.payments.v1.parties.with_streaming_response.list_payment_methods(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_payment_methods(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.v1.parties.with_raw_response.list_payment_methods(
                "",
            )


class TestAsyncParties:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        party = await async_client.payments.v1.parties.create(
            name="name",
            type="individual",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        party = await async_client.payments.v1.parties.create(
            name="name",
            type="individual",
            address_line1="address_line1",
            city="city",
            country="country",
            email="email",
            metadata={},
            phone="phone",
            postal_code="postal_code",
            role="client",
            state="state",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.parties.with_raw_response.create(
            name="name",
            type="individual",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = await response.parse()
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.parties.with_streaming_response.create(
            name="name",
            type="individual",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = await response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        party = await async_client.payments.v1.parties.retrieve(
            "id",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.parties.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = await response.parse()
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.parties.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = await response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.v1.parties.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCasedev) -> None:
        party = await async_client.payments.v1.parties.update(
            id="id",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCasedev) -> None:
        party = await async_client.payments.v1.parties.update(
            id="id",
            address_line1="address_line1",
            address_line2="address_line2",
            city="city",
            country="country",
            email="email",
            is_active=True,
            metadata={},
            name="name",
            notes="notes",
            phone="phone",
            postal_code="postal_code",
            role="client",
            state="state",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.parties.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = await response.parse()
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.parties.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = await response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.v1.parties.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        party = await async_client.payments.v1.parties.list()
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        party = await async_client.payments.v1.parties.list(
            limit=0,
            offset=0,
            role="role",
            type="type",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.parties.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = await response.parse()
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.parties.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = await response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_payment_methods(self, async_client: AsyncCasedev) -> None:
        party = await async_client.payments.v1.parties.list_payment_methods(
            "id",
        )
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_payment_methods(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.parties.with_raw_response.list_payment_methods(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = await response.parse()
        assert party is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_payment_methods(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.parties.with_streaming_response.list_payment_methods(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = await response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_payment_methods(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.v1.parties.with_raw_response.list_payment_methods(
                "",
            )
