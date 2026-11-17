# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.vault import AssemblyCreateResponse, AssemblyRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssemblies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        assembly = client.vault.assemblies.create(
            id="id",
            sources=[{"object_id": "objectId"}],
            volumes=[
                {
                    "filename": "filename",
                    "pages": [
                        {
                            "end": 1,
                            "source": 0,
                            "start": 1,
                        }
                    ],
                }
            ],
            idempotency_key="x",
        )
        assert_matches_type(AssemblyCreateResponse, assembly, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        assembly = client.vault.assemblies.create(
            id="id",
            sources=[
                {
                    "object_id": "objectId",
                    "rendition": "searchable_pdf",
                }
            ],
            volumes=[
                {
                    "filename": "filename",
                    "pages": [
                        {
                            "end": 1,
                            "source": 0,
                            "start": 1,
                            "bates": True,
                        }
                    ],
                    "bates": {
                        "font_size": 6,
                        "legend": "legend",
                        "margin_bottom": 0,
                        "margin_side": 0,
                        "pad_to": 0,
                        "position": "bottom_right",
                        "prefix": "prefix",
                        "shrink": True,
                        "start": 1,
                        "suffix": "suffix",
                    },
                    "contents": {
                        "depth": 1,
                        "title": "title",
                    },
                    "outline": [
                        {
                            "page": 1,
                            "title": "title",
                            "children": [{}],
                        }
                    ],
                    "title": "title",
                }
            ],
            idempotency_key="x",
            bates={
                "font_size": 6,
                "legend": "legend",
                "margin_bottom": 0,
                "margin_side": 0,
                "pad_to": 0,
                "position": "bottom_right",
                "prefix": "prefix",
                "shrink": True,
                "start": 1,
                "suffix": "suffix",
            },
            client_reference="clientReference",
            compression={
                "bitonal": True,
                "clean_scans": True,
                "encoding": "jpeg2000",
                "max_dpi": 72,
                "quality": "high",
            },
            linearize=True,
            page_size="letter",
        )
        assert_matches_type(AssemblyCreateResponse, assembly, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.vault.assemblies.with_raw_response.create(
            id="id",
            sources=[{"object_id": "objectId"}],
            volumes=[
                {
                    "filename": "filename",
                    "pages": [
                        {
                            "end": 1,
                            "source": 0,
                            "start": 1,
                        }
                    ],
                }
            ],
            idempotency_key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assembly = response.parse()
        assert_matches_type(AssemblyCreateResponse, assembly, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.vault.assemblies.with_streaming_response.create(
            id="id",
            sources=[{"object_id": "objectId"}],
            volumes=[
                {
                    "filename": "filename",
                    "pages": [
                        {
                            "end": 1,
                            "source": 0,
                            "start": 1,
                        }
                    ],
                }
            ],
            idempotency_key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assembly = response.parse()
            assert_matches_type(AssemblyCreateResponse, assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.assemblies.with_raw_response.create(
                id="",
                sources=[{"object_id": "objectId"}],
                volumes=[
                    {
                        "filename": "filename",
                        "pages": [
                            {
                                "end": 1,
                                "source": 0,
                                "start": 1,
                            }
                        ],
                    }
                ],
                idempotency_key="x",
            )

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        assembly = client.vault.assemblies.retrieve(
            assembly_id="assemblyId",
            id="id",
        )
        assert_matches_type(AssemblyRetrieveResponse, assembly, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.vault.assemblies.with_raw_response.retrieve(
            assembly_id="assemblyId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assembly = response.parse()
        assert_matches_type(AssemblyRetrieveResponse, assembly, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.vault.assemblies.with_streaming_response.retrieve(
            assembly_id="assemblyId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assembly = response.parse()
            assert_matches_type(AssemblyRetrieveResponse, assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.vault.assemblies.with_raw_response.retrieve(
                assembly_id="assemblyId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assembly_id` but received ''"):
            client.vault.assemblies.with_raw_response.retrieve(
                assembly_id="",
                id="id",
            )


class TestAsyncAssemblies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        assembly = await async_client.vault.assemblies.create(
            id="id",
            sources=[{"object_id": "objectId"}],
            volumes=[
                {
                    "filename": "filename",
                    "pages": [
                        {
                            "end": 1,
                            "source": 0,
                            "start": 1,
                        }
                    ],
                }
            ],
            idempotency_key="x",
        )
        assert_matches_type(AssemblyCreateResponse, assembly, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        assembly = await async_client.vault.assemblies.create(
            id="id",
            sources=[
                {
                    "object_id": "objectId",
                    "rendition": "searchable_pdf",
                }
            ],
            volumes=[
                {
                    "filename": "filename",
                    "pages": [
                        {
                            "end": 1,
                            "source": 0,
                            "start": 1,
                            "bates": True,
                        }
                    ],
                    "bates": {
                        "font_size": 6,
                        "legend": "legend",
                        "margin_bottom": 0,
                        "margin_side": 0,
                        "pad_to": 0,
                        "position": "bottom_right",
                        "prefix": "prefix",
                        "shrink": True,
                        "start": 1,
                        "suffix": "suffix",
                    },
                    "contents": {
                        "depth": 1,
                        "title": "title",
                    },
                    "outline": [
                        {
                            "page": 1,
                            "title": "title",
                            "children": [{}],
                        }
                    ],
                    "title": "title",
                }
            ],
            idempotency_key="x",
            bates={
                "font_size": 6,
                "legend": "legend",
                "margin_bottom": 0,
                "margin_side": 0,
                "pad_to": 0,
                "position": "bottom_right",
                "prefix": "prefix",
                "shrink": True,
                "start": 1,
                "suffix": "suffix",
            },
            client_reference="clientReference",
            compression={
                "bitonal": True,
                "clean_scans": True,
                "encoding": "jpeg2000",
                "max_dpi": 72,
                "quality": "high",
            },
            linearize=True,
            page_size="letter",
        )
        assert_matches_type(AssemblyCreateResponse, assembly, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.assemblies.with_raw_response.create(
            id="id",
            sources=[{"object_id": "objectId"}],
            volumes=[
                {
                    "filename": "filename",
                    "pages": [
                        {
                            "end": 1,
                            "source": 0,
                            "start": 1,
                        }
                    ],
                }
            ],
            idempotency_key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assembly = await response.parse()
        assert_matches_type(AssemblyCreateResponse, assembly, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.assemblies.with_streaming_response.create(
            id="id",
            sources=[{"object_id": "objectId"}],
            volumes=[
                {
                    "filename": "filename",
                    "pages": [
                        {
                            "end": 1,
                            "source": 0,
                            "start": 1,
                        }
                    ],
                }
            ],
            idempotency_key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assembly = await response.parse()
            assert_matches_type(AssemblyCreateResponse, assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.assemblies.with_raw_response.create(
                id="",
                sources=[{"object_id": "objectId"}],
                volumes=[
                    {
                        "filename": "filename",
                        "pages": [
                            {
                                "end": 1,
                                "source": 0,
                                "start": 1,
                            }
                        ],
                    }
                ],
                idempotency_key="x",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        assembly = await async_client.vault.assemblies.retrieve(
            assembly_id="assemblyId",
            id="id",
        )
        assert_matches_type(AssemblyRetrieveResponse, assembly, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.vault.assemblies.with_raw_response.retrieve(
            assembly_id="assemblyId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assembly = await response.parse()
        assert_matches_type(AssemblyRetrieveResponse, assembly, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.vault.assemblies.with_streaming_response.retrieve(
            assembly_id="assemblyId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assembly = await response.parse()
            assert_matches_type(AssemblyRetrieveResponse, assembly, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.vault.assemblies.with_raw_response.retrieve(
                assembly_id="assemblyId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assembly_id` but received ''"):
            await async_client.vault.assemblies.with_raw_response.retrieve(
                assembly_id="",
                id="id",
            )
