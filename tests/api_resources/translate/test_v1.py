# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from casedev.types.translate import (
    V1DetectResponse,
    V1TranslateResponse,
    V1ListLanguagesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_detect(self, client: Casedev) -> None:
        v1 = client.translate.v1.detect(
            q="string",
        )
        assert_matches_type(V1DetectResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_detect(self, client: Casedev) -> None:
        response = client.translate.v1.with_raw_response.detect(
            q="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1DetectResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_detect(self, client: Casedev) -> None:
        with client.translate.v1.with_streaming_response.detect(
            q="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1DetectResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_languages(self, client: Casedev) -> None:
        v1 = client.translate.v1.list_languages()
        assert_matches_type(V1ListLanguagesResponse, v1, path=["response"])

    @parametrize
    def test_method_list_languages_with_all_params(self, client: Casedev) -> None:
        v1 = client.translate.v1.list_languages(
            model="nmt",
            target="target",
        )
        assert_matches_type(V1ListLanguagesResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_list_languages(self, client: Casedev) -> None:
        response = client.translate.v1.with_raw_response.list_languages()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListLanguagesResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_list_languages(self, client: Casedev) -> None:
        with client.translate.v1.with_streaming_response.list_languages() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListLanguagesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_translate(self, client: Casedev) -> None:
        v1 = client.translate.v1.translate(
            q="string",
            target="es",
        )
        assert_matches_type(V1TranslateResponse, v1, path=["response"])

    @parametrize
    def test_method_translate_with_all_params(self, client: Casedev) -> None:
        v1 = client.translate.v1.translate(
            q="string",
            target="es",
            format="text",
            model="nmt",
            source="en",
        )
        assert_matches_type(V1TranslateResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_translate(self, client: Casedev) -> None:
        response = client.translate.v1.with_raw_response.translate(
            q="string",
            target="es",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1TranslateResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_translate(self, client: Casedev) -> None:
        with client.translate.v1.with_streaming_response.translate(
            q="string",
            target="es",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1TranslateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_translate_document(self, client: Casedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/translate/v1/document").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = client.translate.v1.translate_document(
            file=b"Example data",
            target="es",
        )
        assert v1.is_closed
        assert v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_translate_document_with_all_params(self, client: Casedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/translate/v1/document").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = client.translate.v1.translate_document(
            file=b"Example data",
            target="es",
            source="en",
        )
        assert v1.is_closed
        assert v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_translate_document(self, client: Casedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/translate/v1/document").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        v1 = client.translate.v1.with_raw_response.translate_document(
            file=b"Example data",
            target="es",
        )

        assert v1.is_closed is True
        assert v1.http_request.headers.get("X-Stainless-Lang") == "python"
        assert v1.json() == {"foo": "bar"}
        assert isinstance(v1, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_translate_document(self, client: Casedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/translate/v1/document").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.translate.v1.with_streaming_response.translate_document(
            file=b"Example data",
            target="es",
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
    async def test_method_detect(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.translate.v1.detect(
            q="string",
        )
        assert_matches_type(V1DetectResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_detect(self, async_client: AsyncCasedev) -> None:
        response = await async_client.translate.v1.with_raw_response.detect(
            q="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1DetectResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_detect(self, async_client: AsyncCasedev) -> None:
        async with async_client.translate.v1.with_streaming_response.detect(
            q="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1DetectResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_languages(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.translate.v1.list_languages()
        assert_matches_type(V1ListLanguagesResponse, v1, path=["response"])

    @parametrize
    async def test_method_list_languages_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.translate.v1.list_languages(
            model="nmt",
            target="target",
        )
        assert_matches_type(V1ListLanguagesResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_list_languages(self, async_client: AsyncCasedev) -> None:
        response = await async_client.translate.v1.with_raw_response.list_languages()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListLanguagesResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_list_languages(self, async_client: AsyncCasedev) -> None:
        async with async_client.translate.v1.with_streaming_response.list_languages() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListLanguagesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_translate(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.translate.v1.translate(
            q="string",
            target="es",
        )
        assert_matches_type(V1TranslateResponse, v1, path=["response"])

    @parametrize
    async def test_method_translate_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.translate.v1.translate(
            q="string",
            target="es",
            format="text",
            model="nmt",
            source="en",
        )
        assert_matches_type(V1TranslateResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_translate(self, async_client: AsyncCasedev) -> None:
        response = await async_client.translate.v1.with_raw_response.translate(
            q="string",
            target="es",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1TranslateResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_translate(self, async_client: AsyncCasedev) -> None:
        async with async_client.translate.v1.with_streaming_response.translate(
            q="string",
            target="es",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1TranslateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_translate_document(self, async_client: AsyncCasedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/translate/v1/document").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = await async_client.translate.v1.translate_document(
            file=b"Example data",
            target="es",
        )
        assert v1.is_closed
        assert await v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_translate_document_with_all_params(
        self, async_client: AsyncCasedev, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/translate/v1/document").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = await async_client.translate.v1.translate_document(
            file=b"Example data",
            target="es",
            source="en",
        )
        assert v1.is_closed
        assert await v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_translate_document(self, async_client: AsyncCasedev, respx_mock: MockRouter) -> None:
        respx_mock.post("/translate/v1/document").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        v1 = await async_client.translate.v1.with_raw_response.translate_document(
            file=b"Example data",
            target="es",
        )

        assert v1.is_closed is True
        assert v1.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await v1.json() == {"foo": "bar"}
        assert isinstance(v1, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_translate_document(
        self, async_client: AsyncCasedev, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/translate/v1/document").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.translate.v1.with_streaming_response.translate_document(
            file=b"Example data",
            target="es",
        ) as v1:
            assert not v1.is_closed
            assert v1.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await v1.json() == {"foo": "bar"}
            assert cast(Any, v1.is_closed) is True
            assert isinstance(v1, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, v1.is_closed) is True
