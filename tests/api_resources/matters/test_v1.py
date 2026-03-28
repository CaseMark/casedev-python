# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from casedev._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        v1 = client.matters.v1.create(
            title="title",
        )
        assert v1 is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        v1 = client.matters.v1.create(
            title="title",
            billing={"foo": "bar"},
            client_name="client_name",
            client_party_id="client_party_id",
            custom_fields={"foo": "bar"},
            description="description",
            display_id="display_id",
            important_dates={"foo": "bar"},
            jurisdiction={"foo": "bar"},
            matter_type="matter_type",
            metadata={"foo": "bar"},
            practice_area="practice_area",
            responsible_attorney_id="responsible_attorney_id",
            status="intake",
            subtype="subtype",
            vault={
                "description": "description",
                "enable_graph": True,
                "enable_indexing": True,
                "metadata": {"foo": "bar"},
            },
        )
        assert v1 is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.matters.v1.with_raw_response.create(
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.matters.v1.with_streaming_response.create(
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        v1 = client.matters.v1.retrieve(
            "id",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.matters.v1.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.matters.v1.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Casedev) -> None:
        v1 = client.matters.v1.update(
            id="id",
        )
        assert v1 is None

    @parametrize
    def test_method_update_with_all_params(self, client: Casedev) -> None:
        v1 = client.matters.v1.update(
            id="id",
            archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            billing={"foo": "bar"},
            client_name="client_name",
            client_party_id="client_party_id",
            custom_fields={"foo": "bar"},
            description="description",
            display_id="display_id",
            important_dates={"foo": "bar"},
            jurisdiction={"foo": "bar"},
            matter_type="matter_type",
            metadata={"foo": "bar"},
            practice_area="practice_area",
            responsible_attorney_id="responsible_attorney_id",
            status="intake",
            subtype="subtype",
            title="title",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_update(self, client: Casedev) -> None:
        response = client.matters.v1.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_update(self, client: Casedev) -> None:
        with client.matters.v1.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        v1 = client.matters.v1.list()
        assert v1 is None

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        v1 = client.matters.v1.list(
            matter_type="matter_type",
            practice_area="practice_area",
            query="query",
            status="status",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.matters.v1.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.matters.v1.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.matters.v1.create(
            title="title",
        )
        assert v1 is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.matters.v1.create(
            title="title",
            billing={"foo": "bar"},
            client_name="client_name",
            client_party_id="client_party_id",
            custom_fields={"foo": "bar"},
            description="description",
            display_id="display_id",
            important_dates={"foo": "bar"},
            jurisdiction={"foo": "bar"},
            matter_type="matter_type",
            metadata={"foo": "bar"},
            practice_area="practice_area",
            responsible_attorney_id="responsible_attorney_id",
            status="intake",
            subtype="subtype",
            vault={
                "description": "description",
                "enable_graph": True,
                "enable_indexing": True,
                "metadata": {"foo": "bar"},
            },
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.with_raw_response.create(
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.with_streaming_response.create(
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.matters.v1.retrieve(
            "id",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.matters.v1.update(
            id="id",
        )
        assert v1 is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.matters.v1.update(
            id="id",
            archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            billing={"foo": "bar"},
            client_name="client_name",
            client_party_id="client_party_id",
            custom_fields={"foo": "bar"},
            description="description",
            display_id="display_id",
            important_dates={"foo": "bar"},
            jurisdiction={"foo": "bar"},
            matter_type="matter_type",
            metadata={"foo": "bar"},
            practice_area="practice_area",
            responsible_attorney_id="responsible_attorney_id",
            status="intake",
            subtype="subtype",
            title="title",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.matters.v1.list()
        assert v1 is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.matters.v1.list(
            matter_type="matter_type",
            practice_area="practice_area",
            query="query",
            status="status",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True
