# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        v1 = client.worker.v1.create()
        assert v1 is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.worker.v1.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.worker.v1.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        v1 = client.worker.v1.retrieve(
            "id",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.worker.v1.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.worker.v1.with_streaming_response.retrieve(
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
            client.worker.v1.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        v1 = client.worker.v1.delete(
            "id",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.worker.v1.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.worker.v1.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.worker.v1.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_boot(self, client: Casedev) -> None:
        v1 = client.worker.v1.boot(
            "id",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_boot(self, client: Casedev) -> None:
        response = client.worker.v1.with_raw_response.boot(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_boot(self, client: Casedev) -> None:
        with client.worker.v1.with_streaming_response.boot(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_boot(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.worker.v1.with_raw_response.boot(
                "",
            )

    @parametrize
    def test_method_proxy_delete(self, client: Casedev) -> None:
        v1 = client.worker.v1.proxy_delete(
            worker_path="workerPath",
            id="id",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_proxy_delete(self, client: Casedev) -> None:
        response = client.worker.v1.with_raw_response.proxy_delete(
            worker_path="workerPath",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_proxy_delete(self, client: Casedev) -> None:
        with client.worker.v1.with_streaming_response.proxy_delete(
            worker_path="workerPath",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_proxy_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.worker.v1.with_raw_response.proxy_delete(
                worker_path="workerPath",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_path` but received ''"):
            client.worker.v1.with_raw_response.proxy_delete(
                worker_path="",
                id="id",
            )

    @parametrize
    def test_method_proxy_get(self, client: Casedev) -> None:
        v1 = client.worker.v1.proxy_get(
            worker_path="workerPath",
            id="id",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_proxy_get(self, client: Casedev) -> None:
        response = client.worker.v1.with_raw_response.proxy_get(
            worker_path="workerPath",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_proxy_get(self, client: Casedev) -> None:
        with client.worker.v1.with_streaming_response.proxy_get(
            worker_path="workerPath",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_proxy_get(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.worker.v1.with_raw_response.proxy_get(
                worker_path="workerPath",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_path` but received ''"):
            client.worker.v1.with_raw_response.proxy_get(
                worker_path="",
                id="id",
            )

    @parametrize
    def test_method_proxy_patch(self, client: Casedev) -> None:
        v1 = client.worker.v1.proxy_patch(
            worker_path="workerPath",
            id="id",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_proxy_patch(self, client: Casedev) -> None:
        response = client.worker.v1.with_raw_response.proxy_patch(
            worker_path="workerPath",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_proxy_patch(self, client: Casedev) -> None:
        with client.worker.v1.with_streaming_response.proxy_patch(
            worker_path="workerPath",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_proxy_patch(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.worker.v1.with_raw_response.proxy_patch(
                worker_path="workerPath",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_path` but received ''"):
            client.worker.v1.with_raw_response.proxy_patch(
                worker_path="",
                id="id",
            )

    @parametrize
    def test_method_proxy_post(self, client: Casedev) -> None:
        v1 = client.worker.v1.proxy_post(
            worker_path="workerPath",
            id="id",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_proxy_post(self, client: Casedev) -> None:
        response = client.worker.v1.with_raw_response.proxy_post(
            worker_path="workerPath",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_proxy_post(self, client: Casedev) -> None:
        with client.worker.v1.with_streaming_response.proxy_post(
            worker_path="workerPath",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_proxy_post(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.worker.v1.with_raw_response.proxy_post(
                worker_path="workerPath",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_path` but received ''"):
            client.worker.v1.with_raw_response.proxy_post(
                worker_path="",
                id="id",
            )

    @parametrize
    def test_method_proxy_put(self, client: Casedev) -> None:
        v1 = client.worker.v1.proxy_put(
            worker_path="workerPath",
            id="id",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_proxy_put(self, client: Casedev) -> None:
        response = client.worker.v1.with_raw_response.proxy_put(
            worker_path="workerPath",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_proxy_put(self, client: Casedev) -> None:
        with client.worker.v1.with_streaming_response.proxy_put(
            worker_path="workerPath",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_proxy_put(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.worker.v1.with_raw_response.proxy_put(
                worker_path="workerPath",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_path` but received ''"):
            client.worker.v1.with_raw_response.proxy_put(
                worker_path="",
                id="id",
            )


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.worker.v1.create()
        assert v1 is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.worker.v1.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.worker.v1.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.worker.v1.retrieve(
            "id",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.worker.v1.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.worker.v1.with_streaming_response.retrieve(
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
            await async_client.worker.v1.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.worker.v1.delete(
            "id",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.worker.v1.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.worker.v1.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.worker.v1.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_boot(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.worker.v1.boot(
            "id",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_boot(self, async_client: AsyncCasedev) -> None:
        response = await async_client.worker.v1.with_raw_response.boot(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_boot(self, async_client: AsyncCasedev) -> None:
        async with async_client.worker.v1.with_streaming_response.boot(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_boot(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.worker.v1.with_raw_response.boot(
                "",
            )

    @parametrize
    async def test_method_proxy_delete(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.worker.v1.proxy_delete(
            worker_path="workerPath",
            id="id",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_proxy_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.worker.v1.with_raw_response.proxy_delete(
            worker_path="workerPath",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_proxy_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.worker.v1.with_streaming_response.proxy_delete(
            worker_path="workerPath",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_proxy_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.worker.v1.with_raw_response.proxy_delete(
                worker_path="workerPath",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_path` but received ''"):
            await async_client.worker.v1.with_raw_response.proxy_delete(
                worker_path="",
                id="id",
            )

    @parametrize
    async def test_method_proxy_get(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.worker.v1.proxy_get(
            worker_path="workerPath",
            id="id",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_proxy_get(self, async_client: AsyncCasedev) -> None:
        response = await async_client.worker.v1.with_raw_response.proxy_get(
            worker_path="workerPath",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_proxy_get(self, async_client: AsyncCasedev) -> None:
        async with async_client.worker.v1.with_streaming_response.proxy_get(
            worker_path="workerPath",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_proxy_get(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.worker.v1.with_raw_response.proxy_get(
                worker_path="workerPath",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_path` but received ''"):
            await async_client.worker.v1.with_raw_response.proxy_get(
                worker_path="",
                id="id",
            )

    @parametrize
    async def test_method_proxy_patch(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.worker.v1.proxy_patch(
            worker_path="workerPath",
            id="id",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_proxy_patch(self, async_client: AsyncCasedev) -> None:
        response = await async_client.worker.v1.with_raw_response.proxy_patch(
            worker_path="workerPath",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_proxy_patch(self, async_client: AsyncCasedev) -> None:
        async with async_client.worker.v1.with_streaming_response.proxy_patch(
            worker_path="workerPath",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_proxy_patch(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.worker.v1.with_raw_response.proxy_patch(
                worker_path="workerPath",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_path` but received ''"):
            await async_client.worker.v1.with_raw_response.proxy_patch(
                worker_path="",
                id="id",
            )

    @parametrize
    async def test_method_proxy_post(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.worker.v1.proxy_post(
            worker_path="workerPath",
            id="id",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_proxy_post(self, async_client: AsyncCasedev) -> None:
        response = await async_client.worker.v1.with_raw_response.proxy_post(
            worker_path="workerPath",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_proxy_post(self, async_client: AsyncCasedev) -> None:
        async with async_client.worker.v1.with_streaming_response.proxy_post(
            worker_path="workerPath",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_proxy_post(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.worker.v1.with_raw_response.proxy_post(
                worker_path="workerPath",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_path` but received ''"):
            await async_client.worker.v1.with_raw_response.proxy_post(
                worker_path="",
                id="id",
            )

    @parametrize
    async def test_method_proxy_put(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.worker.v1.proxy_put(
            worker_path="workerPath",
            id="id",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_proxy_put(self, async_client: AsyncCasedev) -> None:
        response = await async_client.worker.v1.with_raw_response.proxy_put(
            worker_path="workerPath",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_proxy_put(self, async_client: AsyncCasedev) -> None:
        async with async_client.worker.v1.with_streaming_response.proxy_put(
            worker_path="workerPath",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_proxy_put(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.worker.v1.with_raw_response.proxy_put(
                worker_path="workerPath",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_path` but received ''"):
            await async_client.worker.v1.with_raw_response.proxy_put(
                worker_path="",
                id="id",
            )
