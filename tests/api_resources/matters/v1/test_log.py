# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev._utils import parse_datetime
from casedev.types.matters.v1 import LogExportResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLog:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        log = client.matters.v1.log.create(
            id="id",
            summary="summary",
        )
        assert log is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        log = client.matters.v1.log.create(
            id="id",
            summary="summary",
            details={"foo": "bar"},
            event_type="event_type",
            work_item_id="work_item_id",
        )
        assert log is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.matters.v1.log.with_raw_response.create(
            id="id",
            summary="summary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert log is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.matters.v1.log.with_streaming_response.create(
            id="id",
            summary="summary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert log is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.log.with_raw_response.create(
                id="",
                summary="summary",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        log = client.matters.v1.log.list(
            id="id",
        )
        assert log is None

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        log = client.matters.v1.log.list(
            id="id",
            actor_id="actor_id",
            actor_type="actor_type",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="event_type",
            limit=200,
            offset=0,
            scope="string",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            work_item_id="work_item_id",
        )
        assert log is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.matters.v1.log.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert log is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.matters.v1.log.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert log is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.log.with_raw_response.list(
                id="",
            )

    @parametrize
    def test_method_export(self, client: Casedev) -> None:
        log = client.matters.v1.log.export(
            id="id",
        )
        assert_matches_type(LogExportResponse, log, path=["response"])

    @parametrize
    def test_method_export_with_all_params(self, client: Casedev) -> None:
        log = client.matters.v1.log.export(
            id="id",
            actor_id="actor_id",
            actor_type="actor_type",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="event_type",
            format="json",
            scope="string",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            work_item_id="work_item_id",
        )
        assert_matches_type(LogExportResponse, log, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Casedev) -> None:
        response = client.matters.v1.log.with_raw_response.export(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogExportResponse, log, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Casedev) -> None:
        with client.matters.v1.log.with_streaming_response.export(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogExportResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_export(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.log.with_raw_response.export(
                id="",
            )


class TestAsyncLog:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        log = await async_client.matters.v1.log.create(
            id="id",
            summary="summary",
        )
        assert log is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        log = await async_client.matters.v1.log.create(
            id="id",
            summary="summary",
            details={"foo": "bar"},
            event_type="event_type",
            work_item_id="work_item_id",
        )
        assert log is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.log.with_raw_response.create(
            id="id",
            summary="summary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert log is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.log.with_streaming_response.create(
            id="id",
            summary="summary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert log is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.log.with_raw_response.create(
                id="",
                summary="summary",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        log = await async_client.matters.v1.log.list(
            id="id",
        )
        assert log is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        log = await async_client.matters.v1.log.list(
            id="id",
            actor_id="actor_id",
            actor_type="actor_type",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="event_type",
            limit=200,
            offset=0,
            scope="string",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            work_item_id="work_item_id",
        )
        assert log is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.log.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert log is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.log.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert log is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.log.with_raw_response.list(
                id="",
            )

    @parametrize
    async def test_method_export(self, async_client: AsyncCasedev) -> None:
        log = await async_client.matters.v1.log.export(
            id="id",
        )
        assert_matches_type(LogExportResponse, log, path=["response"])

    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncCasedev) -> None:
        log = await async_client.matters.v1.log.export(
            id="id",
            actor_id="actor_id",
            actor_type="actor_type",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_type="event_type",
            format="json",
            scope="string",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            work_item_id="work_item_id",
        )
        assert_matches_type(LogExportResponse, log, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.log.with_raw_response.export(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogExportResponse, log, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.log.with_streaming_response.export(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogExportResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_export(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.log.with_raw_response.export(
                id="",
            )
