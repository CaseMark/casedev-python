# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from casedev._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHolds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        hold = client.payments.v1.holds.create(
            account_id="account_id",
            amount=0,
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        hold = client.payments.v1.holds.create(
            account_id="account_id",
            amount=0,
            currency="currency",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            memo="memo",
            metadata={},
            on_release_action="on_release_action",
            on_release_config={},
            release_conditions=[
                {
                    "approvers": ["string"],
                    "date": "date",
                    "document_id": "document_id",
                    "type": "manual_approval",
                }
            ],
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.payments.v1.holds.with_raw_response.create(
            account_id="account_id",
            amount=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.payments.v1.holds.with_streaming_response.create(
            account_id="account_id",
            amount=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert hold is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        hold = client.payments.v1.holds.retrieve(
            "id",
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.payments.v1.holds.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.payments.v1.holds.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert hold is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.v1.holds.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        hold = client.payments.v1.holds.list()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        hold = client.payments.v1.holds.list(
            account_id="account_id",
            limit=0,
            offset=0,
            status="status",
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.payments.v1.holds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.payments.v1.holds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert hold is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_approve(self, client: Casedev) -> None:
        hold = client.payments.v1.holds.approve(
            id="id",
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_approve_with_all_params(self, client: Casedev) -> None:
        hold = client.payments.v1.holds.approve(
            id="id",
            approver_id="approver_id",
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_approve(self, client: Casedev) -> None:
        response = client.payments.v1.holds.with_raw_response.approve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_approve(self, client: Casedev) -> None:
        with client.payments.v1.holds.with_streaming_response.approve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert hold is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_approve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.v1.holds.with_raw_response.approve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Casedev) -> None:
        hold = client.payments.v1.holds.cancel(
            "id",
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Casedev) -> None:
        response = client.payments.v1.holds.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Casedev) -> None:
        with client.payments.v1.holds.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert hold is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.v1.holds.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_release(self, client: Casedev) -> None:
        hold = client.payments.v1.holds.release(
            "id",
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_release(self, client: Casedev) -> None:
        response = client.payments.v1.holds.with_raw_response.release(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_release(self, client: Casedev) -> None:
        with client.payments.v1.holds.with_streaming_response.release(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert hold is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_release(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.v1.holds.with_raw_response.release(
                "",
            )


class TestAsyncHolds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        hold = await async_client.payments.v1.holds.create(
            account_id="account_id",
            amount=0,
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        hold = await async_client.payments.v1.holds.create(
            account_id="account_id",
            amount=0,
            currency="currency",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            memo="memo",
            metadata={},
            on_release_action="on_release_action",
            on_release_config={},
            release_conditions=[
                {
                    "approvers": ["string"],
                    "date": "date",
                    "document_id": "document_id",
                    "type": "manual_approval",
                }
            ],
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.holds.with_raw_response.create(
            account_id="account_id",
            amount=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = await response.parse()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.holds.with_streaming_response.create(
            account_id="account_id",
            amount=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert hold is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        hold = await async_client.payments.v1.holds.retrieve(
            "id",
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.holds.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = await response.parse()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.holds.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert hold is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.v1.holds.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        hold = await async_client.payments.v1.holds.list()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        hold = await async_client.payments.v1.holds.list(
            account_id="account_id",
            limit=0,
            offset=0,
            status="status",
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.holds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = await response.parse()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.holds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert hold is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_approve(self, async_client: AsyncCasedev) -> None:
        hold = await async_client.payments.v1.holds.approve(
            id="id",
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_approve_with_all_params(self, async_client: AsyncCasedev) -> None:
        hold = await async_client.payments.v1.holds.approve(
            id="id",
            approver_id="approver_id",
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.holds.with_raw_response.approve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = await response.parse()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.holds.with_streaming_response.approve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert hold is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_approve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.v1.holds.with_raw_response.approve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncCasedev) -> None:
        hold = await async_client.payments.v1.holds.cancel(
            "id",
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.holds.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = await response.parse()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.holds.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert hold is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.v1.holds.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_release(self, async_client: AsyncCasedev) -> None:
        hold = await async_client.payments.v1.holds.release(
            "id",
        )
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_release(self, async_client: AsyncCasedev) -> None:
        response = await async_client.payments.v1.holds.with_raw_response.release(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = await response.parse()
        assert hold is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_release(self, async_client: AsyncCasedev) -> None:
        async with async_client.payments.v1.holds.with_streaming_response.release(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert hold is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_release(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.v1.holds.with_raw_response.release(
                "",
            )
