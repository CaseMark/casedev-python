# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNamespaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        namespace = client.agent.skills.namespaces.create(
            namespace_id="namespaceId",
        )
        assert namespace is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        namespace = client.agent.skills.namespaces.create(
            namespace_id="namespaceId",
            description="description",
            label="label",
            metadata={},
        )
        assert namespace is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.agent.skills.namespaces.with_raw_response.create(
            namespace_id="namespaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert namespace is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.agent.skills.namespaces.with_streaming_response.create(
            namespace_id="namespaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        namespace = client.agent.skills.namespaces.retrieve(
            "id",
        )
        assert namespace is None

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.agent.skills.namespaces.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert namespace is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.agent.skills.namespaces.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.skills.namespaces.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        namespace = client.agent.skills.namespaces.list()
        assert namespace is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.agent.skills.namespaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert namespace is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.agent.skills.namespaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        namespace = client.agent.skills.namespaces.delete(
            "id",
        )
        assert namespace is None

    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.agent.skills.namespaces.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert namespace is None

    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.agent.skills.namespaces.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.skills.namespaces.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_publish(self, client: Casedev) -> None:
        namespace = client.agent.skills.namespaces.publish(
            id="id",
            files=[
                {
                    "content": "content",
                    "encoding": "utf8",
                    "path": "path",
                }
            ],
        )
        assert namespace is None

    @parametrize
    def test_raw_response_publish(self, client: Casedev) -> None:
        response = client.agent.skills.namespaces.with_raw_response.publish(
            id="id",
            files=[
                {
                    "content": "content",
                    "encoding": "utf8",
                    "path": "path",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert namespace is None

    @parametrize
    def test_streaming_response_publish(self, client: Casedev) -> None:
        with client.agent.skills.namespaces.with_streaming_response.publish(
            id="id",
            files=[
                {
                    "content": "content",
                    "encoding": "utf8",
                    "path": "path",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_publish(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.skills.namespaces.with_raw_response.publish(
                id="",
                files=[
                    {
                        "content": "content",
                        "encoding": "utf8",
                        "path": "path",
                    }
                ],
            )

    @parametrize
    def test_method_pull(self, client: Casedev) -> None:
        namespace = client.agent.skills.namespaces.pull(
            "id",
        )
        assert namespace is None

    @parametrize
    def test_raw_response_pull(self, client: Casedev) -> None:
        response = client.agent.skills.namespaces.with_raw_response.pull(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert namespace is None

    @parametrize
    def test_streaming_response_pull(self, client: Casedev) -> None:
        with client.agent.skills.namespaces.with_streaming_response.pull(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_pull(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.skills.namespaces.with_raw_response.pull(
                "",
            )

    @parametrize
    def test_method_rotate_token(self, client: Casedev) -> None:
        namespace = client.agent.skills.namespaces.rotate_token(
            "id",
        )
        assert namespace is None

    @parametrize
    def test_raw_response_rotate_token(self, client: Casedev) -> None:
        response = client.agent.skills.namespaces.with_raw_response.rotate_token(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert namespace is None

    @parametrize
    def test_streaming_response_rotate_token(self, client: Casedev) -> None:
        with client.agent.skills.namespaces.with_streaming_response.rotate_token(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rotate_token(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.skills.namespaces.with_raw_response.rotate_token(
                "",
            )


class TestAsyncNamespaces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        namespace = await async_client.agent.skills.namespaces.create(
            namespace_id="namespaceId",
        )
        assert namespace is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        namespace = await async_client.agent.skills.namespaces.create(
            namespace_id="namespaceId",
            description="description",
            label="label",
            metadata={},
        )
        assert namespace is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.skills.namespaces.with_raw_response.create(
            namespace_id="namespaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert namespace is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.skills.namespaces.with_streaming_response.create(
            namespace_id="namespaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        namespace = await async_client.agent.skills.namespaces.retrieve(
            "id",
        )
        assert namespace is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.skills.namespaces.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert namespace is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.skills.namespaces.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.skills.namespaces.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        namespace = await async_client.agent.skills.namespaces.list()
        assert namespace is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.skills.namespaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert namespace is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.skills.namespaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        namespace = await async_client.agent.skills.namespaces.delete(
            "id",
        )
        assert namespace is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.skills.namespaces.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert namespace is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.skills.namespaces.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.skills.namespaces.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_publish(self, async_client: AsyncCasedev) -> None:
        namespace = await async_client.agent.skills.namespaces.publish(
            id="id",
            files=[
                {
                    "content": "content",
                    "encoding": "utf8",
                    "path": "path",
                }
            ],
        )
        assert namespace is None

    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.skills.namespaces.with_raw_response.publish(
            id="id",
            files=[
                {
                    "content": "content",
                    "encoding": "utf8",
                    "path": "path",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert namespace is None

    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.skills.namespaces.with_streaming_response.publish(
            id="id",
            files=[
                {
                    "content": "content",
                    "encoding": "utf8",
                    "path": "path",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_publish(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.skills.namespaces.with_raw_response.publish(
                id="",
                files=[
                    {
                        "content": "content",
                        "encoding": "utf8",
                        "path": "path",
                    }
                ],
            )

    @parametrize
    async def test_method_pull(self, async_client: AsyncCasedev) -> None:
        namespace = await async_client.agent.skills.namespaces.pull(
            "id",
        )
        assert namespace is None

    @parametrize
    async def test_raw_response_pull(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.skills.namespaces.with_raw_response.pull(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert namespace is None

    @parametrize
    async def test_streaming_response_pull(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.skills.namespaces.with_streaming_response.pull(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_pull(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.skills.namespaces.with_raw_response.pull(
                "",
            )

    @parametrize
    async def test_method_rotate_token(self, async_client: AsyncCasedev) -> None:
        namespace = await async_client.agent.skills.namespaces.rotate_token(
            "id",
        )
        assert namespace is None

    @parametrize
    async def test_raw_response_rotate_token(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.skills.namespaces.with_raw_response.rotate_token(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert namespace is None

    @parametrize
    async def test_streaming_response_rotate_token(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.skills.namespaces.with_streaming_response.rotate_token(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert namespace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rotate_token(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.skills.namespaces.with_raw_response.rotate_token(
                "",
            )
