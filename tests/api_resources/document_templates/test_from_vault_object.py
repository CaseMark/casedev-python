# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFromVaultObject:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        from_vault_object = client.document_templates.from_vault_object.create()
        assert from_vault_object is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.document_templates.from_vault_object.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        from_vault_object = response.parse()
        assert from_vault_object is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.document_templates.from_vault_object.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            from_vault_object = response.parse()
            assert from_vault_object is None

        assert cast(Any, response.is_closed) is True


class TestAsyncFromVaultObject:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        from_vault_object = await async_client.document_templates.from_vault_object.create()
        assert from_vault_object is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.document_templates.from_vault_object.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        from_vault_object = await response.parse()
        assert from_vault_object is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.document_templates.from_vault_object.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            from_vault_object = await response.parse()
            assert from_vault_object is None

        assert cast(Any, response.is_closed) is True
