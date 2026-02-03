# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from casedev import Casedev, AsyncCasedev
from casedev._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_annotate(self, client: Casedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/annotate").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = client.superdoc.v1.annotate(
            document={},
            fields=[
                {
                    "type": "text",
                    "value": "string",
                }
            ],
        )
        assert v1.is_closed
        assert v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_annotate_with_all_params(self, client: Casedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/annotate").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = client.superdoc.v1.annotate(
            document={
                "base64": "base64",
                "url": "url",
            },
            fields=[
                {
                    "type": "text",
                    "value": "string",
                    "id": "id",
                    "group": "group",
                    "options": {
                        "height": 0,
                        "width": 0,
                    },
                }
            ],
            output_format="docx",
        )
        assert v1.is_closed
        assert v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_annotate(self, client: Casedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/annotate").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        v1 = client.superdoc.v1.with_raw_response.annotate(
            document={},
            fields=[
                {
                    "type": "text",
                    "value": "string",
                }
            ],
        )

        assert v1.is_closed is True
        assert v1.http_request.headers.get("X-Stainless-Lang") == "python"
        assert v1.json() == {"foo": "bar"}
        assert isinstance(v1, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_annotate(self, client: Casedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/annotate").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.superdoc.v1.with_streaming_response.annotate(
            document={},
            fields=[
                {
                    "type": "text",
                    "value": "string",
                }
            ],
        ) as v1:
            assert not v1.is_closed
            assert v1.http_request.headers.get("X-Stainless-Lang") == "python"

            assert v1.json() == {"foo": "bar"}
            assert cast(Any, v1.is_closed) is True
            assert isinstance(v1, StreamedBinaryAPIResponse)

        assert cast(Any, v1.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_convert(self, client: Casedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = client.superdoc.v1.convert(
            from_="docx",
        )
        assert v1.is_closed
        assert v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_convert_with_all_params(self, client: Casedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = client.superdoc.v1.convert(
            from_="docx",
            document_base64="document_base64",
            document_url="document_url",
            to="pdf",
        )
        assert v1.is_closed
        assert v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_convert(self, client: Casedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        v1 = client.superdoc.v1.with_raw_response.convert(
            from_="docx",
        )

        assert v1.is_closed is True
        assert v1.http_request.headers.get("X-Stainless-Lang") == "python"
        assert v1.json() == {"foo": "bar"}
        assert isinstance(v1, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_convert(self, client: Casedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.superdoc.v1.with_streaming_response.convert(
            from_="docx",
        ) as v1:
            assert not v1.is_closed
            assert v1.http_request.headers.get("X-Stainless-Lang") == "python"

            assert v1.json() == {"foo": "bar"}
            assert cast(Any, v1.is_closed) is True
            assert isinstance(v1, StreamedBinaryAPIResponse)

        assert cast(Any, v1.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_annotate(self, async_client: AsyncCasedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/annotate").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = await async_client.superdoc.v1.annotate(
            document={},
            fields=[
                {
                    "type": "text",
                    "value": "string",
                }
            ],
        )
        assert v1.is_closed
        assert await v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_annotate_with_all_params(self, async_client: AsyncCasedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/annotate").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = await async_client.superdoc.v1.annotate(
            document={
                "base64": "base64",
                "url": "url",
            },
            fields=[
                {
                    "type": "text",
                    "value": "string",
                    "id": "id",
                    "group": "group",
                    "options": {
                        "height": 0,
                        "width": 0,
                    },
                }
            ],
            output_format="docx",
        )
        assert v1.is_closed
        assert await v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_annotate(self, async_client: AsyncCasedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/annotate").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        v1 = await async_client.superdoc.v1.with_raw_response.annotate(
            document={},
            fields=[
                {
                    "type": "text",
                    "value": "string",
                }
            ],
        )

        assert v1.is_closed is True
        assert v1.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await v1.json() == {"foo": "bar"}
        assert isinstance(v1, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_annotate(self, async_client: AsyncCasedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/annotate").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.superdoc.v1.with_streaming_response.annotate(
            document={},
            fields=[
                {
                    "type": "text",
                    "value": "string",
                }
            ],
        ) as v1:
            assert not v1.is_closed
            assert v1.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await v1.json() == {"foo": "bar"}
            assert cast(Any, v1.is_closed) is True
            assert isinstance(v1, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, v1.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_convert(self, async_client: AsyncCasedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = await async_client.superdoc.v1.convert(
            from_="docx",
        )
        assert v1.is_closed
        assert await v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_convert_with_all_params(self, async_client: AsyncCasedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = await async_client.superdoc.v1.convert(
            from_="docx",
            document_base64="document_base64",
            document_url="document_url",
            to="pdf",
        )
        assert v1.is_closed
        assert await v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_convert(self, async_client: AsyncCasedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        v1 = await async_client.superdoc.v1.with_raw_response.convert(
            from_="docx",
        )

        assert v1.is_closed is True
        assert v1.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await v1.json() == {"foo": "bar"}
        assert isinstance(v1, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_convert(self, async_client: AsyncCasedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/superdoc/v1/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.superdoc.v1.with_streaming_response.convert(
            from_="docx",
        ) as v1:
            assert not v1.is_closed
            assert v1.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await v1.json() == {"foo": "bar"}
            assert cast(Any, v1.is_closed) is True
            assert isinstance(v1, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, v1.is_closed) is True
