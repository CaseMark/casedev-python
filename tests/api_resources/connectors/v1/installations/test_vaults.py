# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVaults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        vault = client.connectors.v1.installations.vaults.list(
            "id",
        )
        assert vault is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.connectors.v1.installations.vaults.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = response.parse()
        assert vault is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.connectors.v1.installations.vaults.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = response.parse()
            assert vault is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.installations.vaults.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_grant(self, client: Casedev) -> None:
        vault = client.connectors.v1.installations.vaults.grant(
            vault_id="vaultId",
            id="id",
        )
        assert vault is None

    @parametrize
    def test_method_grant_with_all_params(self, client: Casedev) -> None:
        vault = client.connectors.v1.installations.vaults.grant(
            vault_id="vaultId",
            id="id",
            can_manage=True,
            can_read=True,
            can_write=True,
            relationship="owned",
            source="provisioning",
        )
        assert vault is None

    @parametrize
    def test_raw_response_grant(self, client: Casedev) -> None:
        response = client.connectors.v1.installations.vaults.with_raw_response.grant(
            vault_id="vaultId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = response.parse()
        assert vault is None

    @parametrize
    def test_streaming_response_grant(self, client: Casedev) -> None:
        with client.connectors.v1.installations.vaults.with_streaming_response.grant(
            vault_id="vaultId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = response.parse()
            assert vault is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_grant(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.installations.vaults.with_raw_response.grant(
                vault_id="vaultId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vault_id` but received ''"):
            client.connectors.v1.installations.vaults.with_raw_response.grant(
                vault_id="",
                id="id",
            )

    @parametrize
    def test_method_revoke(self, client: Casedev) -> None:
        vault = client.connectors.v1.installations.vaults.revoke(
            vault_id="vaultId",
            id="id",
        )
        assert vault is None

    @parametrize
    def test_raw_response_revoke(self, client: Casedev) -> None:
        response = client.connectors.v1.installations.vaults.with_raw_response.revoke(
            vault_id="vaultId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = response.parse()
        assert vault is None

    @parametrize
    def test_streaming_response_revoke(self, client: Casedev) -> None:
        with client.connectors.v1.installations.vaults.with_streaming_response.revoke(
            vault_id="vaultId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = response.parse()
            assert vault is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revoke(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connectors.v1.installations.vaults.with_raw_response.revoke(
                vault_id="vaultId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vault_id` but received ''"):
            client.connectors.v1.installations.vaults.with_raw_response.revoke(
                vault_id="",
                id="id",
            )


class TestAsyncVaults:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        vault = await async_client.connectors.v1.installations.vaults.list(
            "id",
        )
        assert vault is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.installations.vaults.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = await response.parse()
        assert vault is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.installations.vaults.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = await response.parse()
            assert vault is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.installations.vaults.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_grant(self, async_client: AsyncCasedev) -> None:
        vault = await async_client.connectors.v1.installations.vaults.grant(
            vault_id="vaultId",
            id="id",
        )
        assert vault is None

    @parametrize
    async def test_method_grant_with_all_params(self, async_client: AsyncCasedev) -> None:
        vault = await async_client.connectors.v1.installations.vaults.grant(
            vault_id="vaultId",
            id="id",
            can_manage=True,
            can_read=True,
            can_write=True,
            relationship="owned",
            source="provisioning",
        )
        assert vault is None

    @parametrize
    async def test_raw_response_grant(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.installations.vaults.with_raw_response.grant(
            vault_id="vaultId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = await response.parse()
        assert vault is None

    @parametrize
    async def test_streaming_response_grant(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.installations.vaults.with_streaming_response.grant(
            vault_id="vaultId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = await response.parse()
            assert vault is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_grant(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.installations.vaults.with_raw_response.grant(
                vault_id="vaultId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vault_id` but received ''"):
            await async_client.connectors.v1.installations.vaults.with_raw_response.grant(
                vault_id="",
                id="id",
            )

    @parametrize
    async def test_method_revoke(self, async_client: AsyncCasedev) -> None:
        vault = await async_client.connectors.v1.installations.vaults.revoke(
            vault_id="vaultId",
            id="id",
        )
        assert vault is None

    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncCasedev) -> None:
        response = await async_client.connectors.v1.installations.vaults.with_raw_response.revoke(
            vault_id="vaultId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = await response.parse()
        assert vault is None

    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncCasedev) -> None:
        async with async_client.connectors.v1.installations.vaults.with_streaming_response.revoke(
            vault_id="vaultId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = await response.parse()
            assert vault is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connectors.v1.installations.vaults.with_raw_response.revoke(
                vault_id="vaultId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vault_id` but received ''"):
            await async_client.connectors.v1.installations.vaults.with_raw_response.revoke(
                vault_id="",
                id="id",
            )
