# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstallations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        installation = client.connectors.v1.installations.list()
        assert installation is None

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        installation = client.connectors.v1.installations.list(
            application="application",
            external_tenant_id="external_tenant_id",
        )
        assert installation is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.connectors.v1.installations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        installation = response.parse()
        assert installation is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.connectors.v1.installations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            installation = response.parse()
            assert installation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ensure(self, client: Casedev) -> None:
        installation = client.connectors.v1.installations.ensure(
            application="application",
            external_tenant_id="external_tenant_id",
        )
        assert installation is None

    @parametrize
    def test_raw_response_ensure(self, client: Casedev) -> None:
        response = client.connectors.v1.installations.with_raw_response.ensure(
            application="application",
            external_tenant_id="external_tenant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        installation = response.parse()
        assert installation is None

    @parametrize
    def test_streaming_response_ensure(self, client: Casedev) -> None:
        with client.connectors.v1.installations.with_streaming_response.ensure(
            application="application",
            external_tenant_id="external_tenant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            installation = response.parse()
            assert installation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncInstallations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        installation = await async_client.connectors.v1.installations.list()
        assert installation is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        installation = await async_client.connectors.v1.installations.list(
            application="application",
            external_tenant_id="external_tenant_id",
        )
        assert installation is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.installations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        installation = await response.parse()
        assert installation is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.installations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            installation = await response.parse()
            assert installation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ensure(self, async_client: AsyncCasedev) -> None:
        installation = await async_client.connectors.v1.installations.ensure(
            application="application",
            external_tenant_id="external_tenant_id",
        )
        assert installation is None

    @parametrize
    async def test_raw_response_ensure(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.installations.with_raw_response.ensure(
            application="application",
            external_tenant_id="external_tenant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        installation = await response.parse()
        assert installation is None

    @parametrize
    async def test_streaming_response_ensure(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.installations.with_streaming_response.ensure(
            application="application",
            external_tenant_id="external_tenant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            installation = await response.parse()
            assert installation is None

        assert cast(Any, response.is_closed) is True
