# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from casedotdev_sdk_py import Casemark, AsyncCasemark
from casedotdev_sdk_py._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from casedotdev_sdk_py.types.convert import (
    V1CreateProcessResponse,
    V1CreateWebhookResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_process(self, client: Casemark) -> None:
        v1 = client.convert.v1.create_process(
            input_url="https://example.com",
        )
        assert_matches_type(V1CreateProcessResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_process_with_all_params(self, client: Casemark) -> None:
        v1 = client.convert.v1.create_process(
            input_url="https://example.com",
            callback_url="https://example.com",
        )
        assert_matches_type(V1CreateProcessResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_process(self, client: Casemark) -> None:
        response = client.convert.v1.with_raw_response.create_process(
            input_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1CreateProcessResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_process(self, client: Casemark) -> None:
        with client.convert.v1.with_streaming_response.create_process(
            input_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1CreateProcessResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_webhook(self, client: Casemark) -> None:
        v1 = client.convert.v1.create_webhook(
            job_id="job_id",
            status="completed",
        )
        assert_matches_type(V1CreateWebhookResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_webhook_with_all_params(self, client: Casemark) -> None:
        v1 = client.convert.v1.create_webhook(
            job_id="job_id",
            status="completed",
            error="error",
            result={
                "duration_seconds": 0,
                "file_size_bytes": 0,
                "stored_filename": "stored_filename",
            },
        )
        assert_matches_type(V1CreateWebhookResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_webhook(self, client: Casemark) -> None:
        response = client.convert.v1.with_raw_response.create_webhook(
            job_id="job_id",
            status="completed",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1CreateWebhookResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_webhook(self, client: Casemark) -> None:
        with client.convert.v1.with_streaming_response.create_webhook(
            job_id="job_id",
            status="completed",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1CreateWebhookResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Casemark, respx_mock: MockRouter) -> None:
        respx_mock.get("/convert/v1/download/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = client.convert.v1.download(
            "id",
        )
        assert v1.is_closed
        assert v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Casemark, respx_mock: MockRouter) -> None:
        respx_mock.get("/convert/v1/download/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        v1 = client.convert.v1.with_raw_response.download(
            "id",
        )

        assert v1.is_closed is True
        assert v1.http_request.headers.get("X-Stainless-Lang") == "python"
        assert v1.json() == {"foo": "bar"}
        assert isinstance(v1, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Casemark, respx_mock: MockRouter) -> None:
        respx_mock.get("/convert/v1/download/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.convert.v1.with_streaming_response.download(
            "id",
        ) as v1:
            assert not v1.is_closed
            assert v1.http_request.headers.get("X-Stainless-Lang") == "python"

            assert v1.json() == {"foo": "bar"}
            assert cast(Any, v1.is_closed) is True
            assert isinstance(v1, StreamedBinaryAPIResponse)

        assert cast(Any, v1.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Casemark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.convert.v1.with_raw_response.download(
                "",
            )


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_process(self, async_client: AsyncCasemark) -> None:
        v1 = await async_client.convert.v1.create_process(
            input_url="https://example.com",
        )
        assert_matches_type(V1CreateProcessResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_process_with_all_params(self, async_client: AsyncCasemark) -> None:
        v1 = await async_client.convert.v1.create_process(
            input_url="https://example.com",
            callback_url="https://example.com",
        )
        assert_matches_type(V1CreateProcessResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_process(self, async_client: AsyncCasemark) -> None:
        response = await async_client.convert.v1.with_raw_response.create_process(
            input_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1CreateProcessResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_process(self, async_client: AsyncCasemark) -> None:
        async with async_client.convert.v1.with_streaming_response.create_process(
            input_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1CreateProcessResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_webhook(self, async_client: AsyncCasemark) -> None:
        v1 = await async_client.convert.v1.create_webhook(
            job_id="job_id",
            status="completed",
        )
        assert_matches_type(V1CreateWebhookResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_webhook_with_all_params(self, async_client: AsyncCasemark) -> None:
        v1 = await async_client.convert.v1.create_webhook(
            job_id="job_id",
            status="completed",
            error="error",
            result={
                "duration_seconds": 0,
                "file_size_bytes": 0,
                "stored_filename": "stored_filename",
            },
        )
        assert_matches_type(V1CreateWebhookResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_webhook(self, async_client: AsyncCasemark) -> None:
        response = await async_client.convert.v1.with_raw_response.create_webhook(
            job_id="job_id",
            status="completed",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1CreateWebhookResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_webhook(self, async_client: AsyncCasemark) -> None:
        async with async_client.convert.v1.with_streaming_response.create_webhook(
            job_id="job_id",
            status="completed",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1CreateWebhookResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncCasemark, respx_mock: MockRouter) -> None:
        respx_mock.get("/convert/v1/download/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = await async_client.convert.v1.download(
            "id",
        )
        assert v1.is_closed
        assert await v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncCasemark, respx_mock: MockRouter) -> None:
        respx_mock.get("/convert/v1/download/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        v1 = await async_client.convert.v1.with_raw_response.download(
            "id",
        )

        assert v1.is_closed is True
        assert v1.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await v1.json() == {"foo": "bar"}
        assert isinstance(v1, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncCasemark, respx_mock: MockRouter) -> None:
        respx_mock.get("/convert/v1/download/id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.convert.v1.with_streaming_response.download(
            "id",
        ) as v1:
            assert not v1.is_closed
            assert v1.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await v1.json() == {"foo": "bar"}
            assert cast(Any, v1.is_closed) is True
            assert isinstance(v1, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, v1.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncCasemark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.convert.v1.with_raw_response.download(
                "",
            )
