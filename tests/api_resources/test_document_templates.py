# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocumentTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        document_template = client.document_templates.create()
        assert document_template is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.document_templates.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document_template = response.parse()
        assert document_template is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.document_templates.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document_template = response.parse()
            assert document_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        document_template = client.document_templates.retrieve(
            "id",
        )
        assert document_template is None

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.document_templates.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document_template = response.parse()
        assert document_template is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.document_templates.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document_template = response.parse()
            assert document_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.document_templates.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Casedev) -> None:
        document_template = client.document_templates.update(
            "id",
        )
        assert document_template is None

    @parametrize
    def test_raw_response_update(self, client: Casedev) -> None:
        response = client.document_templates.with_raw_response.update(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document_template = response.parse()
        assert document_template is None

    @parametrize
    def test_streaming_response_update(self, client: Casedev) -> None:
        with client.document_templates.with_streaming_response.update(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document_template = response.parse()
            assert document_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.document_templates.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        document_template = client.document_templates.list()
        assert document_template is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.document_templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document_template = response.parse()
        assert document_template is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.document_templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document_template = response.parse()
            assert document_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        document_template = client.document_templates.delete(
            "id",
        )
        assert document_template is None

    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.document_templates.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document_template = response.parse()
        assert document_template is None

    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.document_templates.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document_template = response.parse()
            assert document_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.document_templates.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_confirm(self, client: Casedev) -> None:
        document_template = client.document_templates.confirm(
            "id",
        )
        assert document_template is None

    @parametrize
    def test_raw_response_confirm(self, client: Casedev) -> None:
        response = client.document_templates.with_raw_response.confirm(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document_template = response.parse()
        assert document_template is None

    @parametrize
    def test_streaming_response_confirm(self, client: Casedev) -> None:
        with client.document_templates.with_streaming_response.confirm(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document_template = response.parse()
            assert document_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_confirm(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.document_templates.with_raw_response.confirm(
                "",
            )


class TestAsyncDocumentTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        document_template = await async_client.document_templates.create()
        assert document_template is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.document_templates.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document_template = await response.parse()
        assert document_template is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.document_templates.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document_template = await response.parse()
            assert document_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        document_template = await async_client.document_templates.retrieve(
            "id",
        )
        assert document_template is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.document_templates.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document_template = await response.parse()
        assert document_template is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.document_templates.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document_template = await response.parse()
            assert document_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.document_templates.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCasedev) -> None:
        document_template = await async_client.document_templates.update(
            "id",
        )
        assert document_template is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCasedev) -> None:
        response = await async_client.document_templates.with_raw_response.update(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document_template = await response.parse()
        assert document_template is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCasedev) -> None:
        async with async_client.document_templates.with_streaming_response.update(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document_template = await response.parse()
            assert document_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.document_templates.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        document_template = await async_client.document_templates.list()
        assert document_template is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.document_templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document_template = await response.parse()
        assert document_template is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.document_templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document_template = await response.parse()
            assert document_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        document_template = await async_client.document_templates.delete(
            "id",
        )
        assert document_template is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.document_templates.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document_template = await response.parse()
        assert document_template is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.document_templates.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document_template = await response.parse()
            assert document_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.document_templates.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_confirm(self, async_client: AsyncCasedev) -> None:
        document_template = await async_client.document_templates.confirm(
            "id",
        )
        assert document_template is None

    @parametrize
    async def test_raw_response_confirm(self, async_client: AsyncCasedev) -> None:
        response = await async_client.document_templates.with_raw_response.confirm(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document_template = await response.parse()
        assert document_template is None

    @parametrize
    async def test_streaming_response_confirm(self, async_client: AsyncCasedev) -> None:
        async with async_client.document_templates.with_streaming_response.confirm(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document_template = await response.parse()
            assert document_template is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_confirm(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.document_templates.with_raw_response.confirm(
                "",
            )
