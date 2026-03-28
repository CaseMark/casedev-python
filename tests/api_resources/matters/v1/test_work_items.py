# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from casedev._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        work_item = client.matters.v1.work_items.create(
            id="id",
            title="title",
        )
        assert work_item is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        work_item = client.matters.v1.work_items.create(
            id="id",
            title="title",
            assignee_id="assignee_id",
            description="description",
            due_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            exit_criteria=["string"],
            instructions="instructions",
            metadata={"foo": "bar"},
            priority="low",
            type="task",
        )
        assert work_item is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.matters.v1.work_items.with_raw_response.create(
            id="id",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        work_item = response.parse()
        assert work_item is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.matters.v1.work_items.with_streaming_response.create(
            id="id",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            work_item = response.parse()
            assert work_item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.work_items.with_raw_response.create(
                id="",
                title="title",
            )

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        work_item = client.matters.v1.work_items.retrieve(
            work_item_id="workItemId",
            id="id",
        )
        assert work_item is None

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.matters.v1.work_items.with_raw_response.retrieve(
            work_item_id="workItemId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        work_item = response.parse()
        assert work_item is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.matters.v1.work_items.with_streaming_response.retrieve(
            work_item_id="workItemId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            work_item = response.parse()
            assert work_item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.work_items.with_raw_response.retrieve(
                work_item_id="workItemId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `work_item_id` but received ''"):
            client.matters.v1.work_items.with_raw_response.retrieve(
                work_item_id="",
                id="id",
            )

    @parametrize
    def test_method_update(self, client: Casedev) -> None:
        work_item = client.matters.v1.work_items.update(
            work_item_id="workItemId",
            id="id",
        )
        assert work_item is None

    @parametrize
    def test_method_update_with_all_params(self, client: Casedev) -> None:
        work_item = client.matters.v1.work_items.update(
            work_item_id="workItemId",
            id="id",
            assignee_id="assignee_id",
            completed_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            description="description",
            due_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            exit_criteria=["string"],
            instructions="instructions",
            metadata={"foo": "bar"},
            priority="low",
            started_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="draft",
            title="title",
            type="task",
        )
        assert work_item is None

    @parametrize
    def test_raw_response_update(self, client: Casedev) -> None:
        response = client.matters.v1.work_items.with_raw_response.update(
            work_item_id="workItemId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        work_item = response.parse()
        assert work_item is None

    @parametrize
    def test_streaming_response_update(self, client: Casedev) -> None:
        with client.matters.v1.work_items.with_streaming_response.update(
            work_item_id="workItemId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            work_item = response.parse()
            assert work_item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.work_items.with_raw_response.update(
                work_item_id="workItemId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `work_item_id` but received ''"):
            client.matters.v1.work_items.with_raw_response.update(
                work_item_id="",
                id="id",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        work_item = client.matters.v1.work_items.list(
            id="id",
        )
        assert work_item is None

    @parametrize
    def test_method_list_with_all_params(self, client: Casedev) -> None:
        work_item = client.matters.v1.work_items.list(
            id="id",
            assignee_id="assignee_id",
            status="status",
        )
        assert work_item is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.matters.v1.work_items.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        work_item = response.parse()
        assert work_item is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.matters.v1.work_items.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            work_item = response.parse()
            assert work_item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.work_items.with_raw_response.list(
                id="",
            )

    @parametrize
    def test_method_decide(self, client: Casedev) -> None:
        work_item = client.matters.v1.work_items.decide(
            work_item_id="workItemId",
            id="id",
            decision="approve",
        )
        assert work_item is None

    @parametrize
    def test_method_decide_with_all_params(self, client: Casedev) -> None:
        work_item = client.matters.v1.work_items.decide(
            work_item_id="workItemId",
            id="id",
            decision="approve",
            agent_type_id="agent_type_id",
            metadata={"foo": "bar"},
            reason="reason",
        )
        assert work_item is None

    @parametrize
    def test_raw_response_decide(self, client: Casedev) -> None:
        response = client.matters.v1.work_items.with_raw_response.decide(
            work_item_id="workItemId",
            id="id",
            decision="approve",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        work_item = response.parse()
        assert work_item is None

    @parametrize
    def test_streaming_response_decide(self, client: Casedev) -> None:
        with client.matters.v1.work_items.with_streaming_response.decide(
            work_item_id="workItemId",
            id="id",
            decision="approve",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            work_item = response.parse()
            assert work_item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_decide(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.work_items.with_raw_response.decide(
                work_item_id="workItemId",
                id="",
                decision="approve",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `work_item_id` but received ''"):
            client.matters.v1.work_items.with_raw_response.decide(
                work_item_id="",
                id="id",
                decision="approve",
            )

    @parametrize
    def test_method_list_executions(self, client: Casedev) -> None:
        work_item = client.matters.v1.work_items.list_executions(
            work_item_id="workItemId",
            id="id",
        )
        assert work_item is None

    @parametrize
    def test_raw_response_list_executions(self, client: Casedev) -> None:
        response = client.matters.v1.work_items.with_raw_response.list_executions(
            work_item_id="workItemId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        work_item = response.parse()
        assert work_item is None

    @parametrize
    def test_streaming_response_list_executions(self, client: Casedev) -> None:
        with client.matters.v1.work_items.with_streaming_response.list_executions(
            work_item_id="workItemId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            work_item = response.parse()
            assert work_item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_executions(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.matters.v1.work_items.with_raw_response.list_executions(
                work_item_id="workItemId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `work_item_id` but received ''"):
            client.matters.v1.work_items.with_raw_response.list_executions(
                work_item_id="",
                id="id",
            )


class TestAsyncWorkItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        work_item = await async_client.matters.v1.work_items.create(
            id="id",
            title="title",
        )
        assert work_item is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        work_item = await async_client.matters.v1.work_items.create(
            id="id",
            title="title",
            assignee_id="assignee_id",
            description="description",
            due_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            exit_criteria=["string"],
            instructions="instructions",
            metadata={"foo": "bar"},
            priority="low",
            type="task",
        )
        assert work_item is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.work_items.with_raw_response.create(
            id="id",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        work_item = await response.parse()
        assert work_item is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.work_items.with_streaming_response.create(
            id="id",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            work_item = await response.parse()
            assert work_item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.work_items.with_raw_response.create(
                id="",
                title="title",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        work_item = await async_client.matters.v1.work_items.retrieve(
            work_item_id="workItemId",
            id="id",
        )
        assert work_item is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.work_items.with_raw_response.retrieve(
            work_item_id="workItemId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        work_item = await response.parse()
        assert work_item is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.work_items.with_streaming_response.retrieve(
            work_item_id="workItemId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            work_item = await response.parse()
            assert work_item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.work_items.with_raw_response.retrieve(
                work_item_id="workItemId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `work_item_id` but received ''"):
            await async_client.matters.v1.work_items.with_raw_response.retrieve(
                work_item_id="",
                id="id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCasedev) -> None:
        work_item = await async_client.matters.v1.work_items.update(
            work_item_id="workItemId",
            id="id",
        )
        assert work_item is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCasedev) -> None:
        work_item = await async_client.matters.v1.work_items.update(
            work_item_id="workItemId",
            id="id",
            assignee_id="assignee_id",
            completed_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            description="description",
            due_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            exit_criteria=["string"],
            instructions="instructions",
            metadata={"foo": "bar"},
            priority="low",
            started_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="draft",
            title="title",
            type="task",
        )
        assert work_item is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.work_items.with_raw_response.update(
            work_item_id="workItemId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        work_item = await response.parse()
        assert work_item is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.work_items.with_streaming_response.update(
            work_item_id="workItemId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            work_item = await response.parse()
            assert work_item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.work_items.with_raw_response.update(
                work_item_id="workItemId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `work_item_id` but received ''"):
            await async_client.matters.v1.work_items.with_raw_response.update(
                work_item_id="",
                id="id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        work_item = await async_client.matters.v1.work_items.list(
            id="id",
        )
        assert work_item is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCasedev) -> None:
        work_item = await async_client.matters.v1.work_items.list(
            id="id",
            assignee_id="assignee_id",
            status="status",
        )
        assert work_item is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.work_items.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        work_item = await response.parse()
        assert work_item is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.work_items.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            work_item = await response.parse()
            assert work_item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.work_items.with_raw_response.list(
                id="",
            )

    @parametrize
    async def test_method_decide(self, async_client: AsyncCasedev) -> None:
        work_item = await async_client.matters.v1.work_items.decide(
            work_item_id="workItemId",
            id="id",
            decision="approve",
        )
        assert work_item is None

    @parametrize
    async def test_method_decide_with_all_params(self, async_client: AsyncCasedev) -> None:
        work_item = await async_client.matters.v1.work_items.decide(
            work_item_id="workItemId",
            id="id",
            decision="approve",
            agent_type_id="agent_type_id",
            metadata={"foo": "bar"},
            reason="reason",
        )
        assert work_item is None

    @parametrize
    async def test_raw_response_decide(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.work_items.with_raw_response.decide(
            work_item_id="workItemId",
            id="id",
            decision="approve",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        work_item = await response.parse()
        assert work_item is None

    @parametrize
    async def test_streaming_response_decide(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.work_items.with_streaming_response.decide(
            work_item_id="workItemId",
            id="id",
            decision="approve",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            work_item = await response.parse()
            assert work_item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_decide(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.work_items.with_raw_response.decide(
                work_item_id="workItemId",
                id="",
                decision="approve",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `work_item_id` but received ''"):
            await async_client.matters.v1.work_items.with_raw_response.decide(
                work_item_id="",
                id="id",
                decision="approve",
            )

    @parametrize
    async def test_method_list_executions(self, async_client: AsyncCasedev) -> None:
        work_item = await async_client.matters.v1.work_items.list_executions(
            work_item_id="workItemId",
            id="id",
        )
        assert work_item is None

    @parametrize
    async def test_raw_response_list_executions(self, async_client: AsyncCasedev) -> None:
        response = await async_client.matters.v1.work_items.with_raw_response.list_executions(
            work_item_id="workItemId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        work_item = await response.parse()
        assert work_item is None

    @parametrize
    async def test_streaming_response_list_executions(self, async_client: AsyncCasedev) -> None:
        async with async_client.matters.v1.work_items.with_streaming_response.list_executions(
            work_item_id="workItemId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            work_item = await response.parse()
            assert work_item is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_executions(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.matters.v1.work_items.with_raw_response.list_executions(
                work_item_id="workItemId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `work_item_id` but received ''"):
            await async_client.matters.v1.work_items.with_raw_response.list_executions(
                work_item_id="",
                id="id",
            )
