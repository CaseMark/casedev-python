# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMatterParties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        matter_party = client.matters.v1.matter_parties.create(
            id="id",
            party_id="party_id",
            role="client",
        )
        assert matter_party is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        matter_party = client.matters.v1.matter_parties.create(
            id="id",
            party_id="party_id",
            role="client",
            custom_fields={"foo": "bar"},
            is_primary=True,
            metadata={"foo": "bar"},
            notes="notes",
            set_as_client=True,
        )
        assert matter_party is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.matters.v1.matter_parties.with_raw_response.create(
            id="id",
            party_id="party_id",
            role="client",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        matter_party = response.parse()
        assert matter_party is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.matters.v1.matter_parties.with_streaming_response.create(
            id="id",
            party_id="party_id",
            role="client",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            matter_party = response.parse()
            assert matter_party is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.matter_parties.with_raw_response.create(
                id="",
                party_id="party_id",
                role="client",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        matter_party = client.matters.v1.matter_parties.list(
            "id",
        )
        assert matter_party is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.matters.v1.matter_parties.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        matter_party = response.parse()
        assert matter_party is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.matters.v1.matter_parties.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            matter_party = response.parse()
            assert matter_party is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.matter_parties.with_raw_response.list(
                "",
            )


class TestAsyncMatterParties:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        matter_party = await async_client.matters.v1.matter_parties.create(
            id="id",
            party_id="party_id",
            role="client",
        )
        assert matter_party is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        matter_party = await async_client.matters.v1.matter_parties.create(
            id="id",
            party_id="party_id",
            role="client",
            custom_fields={"foo": "bar"},
            is_primary=True,
            metadata={"foo": "bar"},
            notes="notes",
            set_as_client=True,
        )
        assert matter_party is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.matter_parties.with_raw_response.create(
            id="id",
            party_id="party_id",
            role="client",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        matter_party = await response.parse()
        assert matter_party is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.matter_parties.with_streaming_response.create(
            id="id",
            party_id="party_id",
            role="client",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            matter_party = await response.parse()
            assert matter_party is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.matter_parties.with_raw_response.create(
                id="",
                party_id="party_id",
                role="client",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        matter_party = await async_client.matters.v1.matter_parties.list(
            "id",
        )
        assert matter_party is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.matter_parties.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        matter_party = await response.parse()
        assert matter_party is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.matter_parties.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            matter_party = await response.parse()
            assert matter_party is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.matter_parties.with_raw_response.list(
                "",
            )
