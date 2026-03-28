# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        party = client.matters.v1.parties.create(
            name="name",
        )
        assert party is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        party = client.matters.v1.parties.create(
            name="name",
            addresses=[{"foo": "bar"}],
            custom_fields={"foo": "bar"},
            email="email",
            metadata={"foo": "bar"},
            notes="notes",
            phone="phone",
            type="person",
        )
        assert party is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.matters.v1.parties.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = response.parse()
        assert party is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.matters.v1.parties.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        party = client.matters.v1.parties.retrieve(
            "partyId",
        )
        assert party is None

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.matters.v1.parties.with_raw_response.retrieve(
            "partyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = response.parse()
        assert party is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.matters.v1.parties.with_streaming_response.retrieve(
            "partyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `party_id` but received ''"):
            client.matters.v1.parties.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Casedev) -> None:
        party = client.matters.v1.parties.update(
            "partyId",
        )
        assert party is None

    @parametrize
    def test_raw_response_update(self, client: Casedev) -> None:
        response = client.matters.v1.parties.with_raw_response.update(
            "partyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = response.parse()
        assert party is None

    @parametrize
    def test_streaming_response_update(self, client: Casedev) -> None:
        with client.matters.v1.parties.with_streaming_response.update(
            "partyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `party_id` but received ''"):
            client.matters.v1.parties.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        party = client.matters.v1.parties.list()
        assert party is None

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        party = client.matters.v1.parties.list(
            email="email",
            query="query",
            type="person",
        )
        assert party is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.matters.v1.parties.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = response.parse()
        assert party is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.matters.v1.parties.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True


class TestAsyncParties:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        party = await async_client.matters.v1.parties.create(
            name="name",
        )
        assert party is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        party = await async_client.matters.v1.parties.create(
            name="name",
            addresses=[{"foo": "bar"}],
            custom_fields={"foo": "bar"},
            email="email",
            metadata={"foo": "bar"},
            notes="notes",
            phone="phone",
            type="person",
        )
        assert party is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.parties.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = await response.parse()
        assert party is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.parties.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = await response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        party = await async_client.matters.v1.parties.retrieve(
            "partyId",
        )
        assert party is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.parties.with_raw_response.retrieve(
            "partyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = await response.parse()
        assert party is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.parties.with_streaming_response.retrieve(
            "partyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = await response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `party_id` but received ''"):
            await async_client.matters.v1.parties.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCasedev) -> None:
        party = await async_client.matters.v1.parties.update(
            "partyId",
        )
        assert party is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.parties.with_raw_response.update(
            "partyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = await response.parse()
        assert party is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.parties.with_streaming_response.update(
            "partyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = await response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `party_id` but received ''"):
            await async_client.matters.v1.parties.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        party = await async_client.matters.v1.parties.list()
        assert party is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        party = await async_client.matters.v1.parties.list(
            email="email",
            query="query",
            type="person",
        )
        assert party is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.parties.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = await response.parse()
        assert party is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.parties.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = await response.parse()
            assert party is None

        assert cast(Any, response.is_closed) is True
