# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.compute.v1 import (
    InstanceListResponse,
    InstanceCreateResponse,
    InstanceDeleteResponse,
    InstanceRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        instance = client.compute.v1.instances.create(
            instance_type="gpu_1x_a10",
            name="ocr-batch-job",
            region="us-west-1",
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        instance = client.compute.v1.instances.create(
            instance_type="gpu_1x_a10",
            name="ocr-batch-job",
            region="us-west-1",
            auto_shutdown_minutes=120,
            vault_ids=["vault_abc123"],
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.compute.v1.instances.with_raw_response.create(
            instance_type="gpu_1x_a10",
            name="ocr-batch-job",
            region="us-west-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.compute.v1.instances.with_streaming_response.create(
            instance_type="gpu_1x_a10",
            name="ocr-batch-job",
            region="us-west-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceCreateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        instance = client.compute.v1.instances.retrieve(
            "id",
        )
        assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.compute.v1.instances.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.compute.v1.instances.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.compute.v1.instances.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        instance = client.compute.v1.instances.list()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.compute.v1.instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.compute.v1.instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceListResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        instance = client.compute.v1.instances.delete(
            "id",
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.compute.v1.instances.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.compute.v1.instances.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.compute.v1.instances.with_raw_response.delete(
                "",
            )


class TestAsyncInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        instance = await async_client.compute.v1.instances.create(
            instance_type="gpu_1x_a10",
            name="ocr-batch-job",
            region="us-west-1",
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        instance = await async_client.compute.v1.instances.create(
            instance_type="gpu_1x_a10",
            name="ocr-batch-job",
            region="us-west-1",
            auto_shutdown_minutes=120,
            vault_ids=["vault_abc123"],
        )
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.compute.v1.instances.with_raw_response.create(
            instance_type="gpu_1x_a10",
            name="ocr-batch-job",
            region="us-west-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceCreateResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.compute.v1.instances.with_streaming_response.create(
            instance_type="gpu_1x_a10",
            name="ocr-batch-job",
            region="us-west-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceCreateResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        instance = await async_client.compute.v1.instances.retrieve(
            "id",
        )
        assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.compute.v1.instances.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.compute.v1.instances.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceRetrieveResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.compute.v1.instances.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        instance = await async_client.compute.v1.instances.list()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.compute.v1.instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceListResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.compute.v1.instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceListResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        instance = await async_client.compute.v1.instances.delete(
            "id",
        )
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.compute.v1.instances.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.compute.v1.instances.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceDeleteResponse, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.compute.v1.instances.with_raw_response.delete(
                "",
            )
