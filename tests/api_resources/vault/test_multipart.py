# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.vault import MultipartGetPartURLsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMultipart:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_abort(self, client: Casedev) -> None:
        multipart = client.vault.multipart.abort(
            id="id",
            object_id="objectId",
            upload_id="uploadId",
        )
        assert multipart is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_abort(self, client: Casedev) -> None:
        response = client.vault.multipart.with_raw_response.abort(
            id="id",
            object_id="objectId",
            upload_id="uploadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = response.parse()
        assert multipart is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_abort(self, client: Casedev) -> None:
        with client.vault.multipart.with_streaming_response.abort(
            id="id",
            object_id="objectId",
            upload_id="uploadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = response.parse()
            assert multipart is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_abort(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.multipart.with_raw_response.abort(
                id="",
                object_id="objectId",
                upload_id="uploadId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_part_urls(self, client: Casedev) -> None:
        multipart = client.vault.multipart.get_part_urls(
            id="id",
            object_id="objectId",
            parts=[
                {
                    "part_number": 1,
                    "size_bytes": 1,
                }
            ],
            upload_id="uploadId",
        )
        assert_matches_type(MultipartGetPartURLsResponse, multipart, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_part_urls(self, client: Casedev) -> None:
        response = client.vault.multipart.with_raw_response.get_part_urls(
            id="id",
            object_id="objectId",
            parts=[
                {
                    "part_number": 1,
                    "size_bytes": 1,
                }
            ],
            upload_id="uploadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = response.parse()
        assert_matches_type(MultipartGetPartURLsResponse, multipart, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_part_urls(self, client: Casedev) -> None:
        with client.vault.multipart.with_streaming_response.get_part_urls(
            id="id",
            object_id="objectId",
            parts=[
                {
                    "part_number": 1,
                    "size_bytes": 1,
                }
            ],
            upload_id="uploadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = response.parse()
            assert_matches_type(MultipartGetPartURLsResponse, multipart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_part_urls(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.multipart.with_raw_response.get_part_urls(
                id="",
                object_id="objectId",
                parts=[
                    {
                        "part_number": 1,
                        "size_bytes": 1,
                    }
                ],
                upload_id="uploadId",
            )


class TestAsyncMultipart:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_abort(self, async_client: AsyncCasedev) -> None:
        multipart = await async_client.vault.multipart.abort(
            id="id",
            object_id="objectId",
            upload_id="uploadId",
        )
        assert multipart is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_abort(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.multipart.with_raw_response.abort(
            id="id",
            object_id="objectId",
            upload_id="uploadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = await response.parse()
        assert multipart is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_abort(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.multipart.with_streaming_response.abort(
            id="id",
            object_id="objectId",
            upload_id="uploadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = await response.parse()
            assert multipart is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_abort(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.multipart.with_raw_response.abort(
                id="",
                object_id="objectId",
                upload_id="uploadId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_part_urls(self, async_client: AsyncCasedev) -> None:
        multipart = await async_client.vault.multipart.get_part_urls(
            id="id",
            object_id="objectId",
            parts=[
                {
                    "part_number": 1,
                    "size_bytes": 1,
                }
            ],
            upload_id="uploadId",
        )
        assert_matches_type(MultipartGetPartURLsResponse, multipart, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_part_urls(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.multipart.with_raw_response.get_part_urls(
            id="id",
            object_id="objectId",
            parts=[
                {
                    "part_number": 1,
                    "size_bytes": 1,
                }
            ],
            upload_id="uploadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = await response.parse()
        assert_matches_type(MultipartGetPartURLsResponse, multipart, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_part_urls(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.multipart.with_streaming_response.get_part_urls(
            id="id",
            object_id="objectId",
            parts=[
                {
                    "part_number": 1,
                    "size_bytes": 1,
                }
            ],
            upload_id="uploadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = await response.parse()
            assert_matches_type(MultipartGetPartURLsResponse, multipart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_part_urls(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.multipart.with_raw_response.get_part_urls(
                id="",
                object_id="objectId",
                parts=[
                    {
                        "part_number": 1,
                        "size_bytes": 1,
                    }
                ],
                upload_id="uploadId",
            )
