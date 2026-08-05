# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        session = client.linc.v1.sessions.create()
        assert session is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        session = client.linc.v1.sessions.create(
            document_template_slugs=["string"],
            idle_timeout_ms=0,
            include_document_templates=True,
            instructions="instructions",
            model="model",
            scoped_api_key="scopedApiKey",
            service_tier="default",
            skill_slugs=["string"],
            title="title",
            vault_ids=["string"],
        )
        assert session is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.linc.v1.sessions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.linc.v1.sessions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        session = client.linc.v1.sessions.delete(
            "id",
        )
        assert session is None

    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.linc.v1.sessions.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.linc.v1.sessions.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.linc.v1.sessions.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: Casedev) -> None:
        session = client.linc.v1.sessions.cancel(
            id="id",
        )
        assert session is None

    @parametrize
    def test_method_cancel_with_all_params(self, client: Casedev) -> None:
        session = client.linc.v1.sessions.cancel(
            id="id",
            clear_queue=True,
        )
        assert session is None

    @parametrize
    def test_raw_response_cancel(self, client: Casedev) -> None:
        response = client.linc.v1.sessions.with_raw_response.cancel(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_cancel(self, client: Casedev) -> None:
        with client.linc.v1.sessions.with_streaming_response.cancel(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.linc.v1.sessions.with_raw_response.cancel(
                id="",
            )

    @parametrize
    def test_method_ingest_events(self, client: Casedev) -> None:
        session = client.linc.v1.sessions.ingest_events(
            id="id",
            frames=[
                {
                    "event": {"foo": "bar"},
                    "seq": 1,
                    "type": "type",
                }
            ],
        )
        assert session is None

    @parametrize
    def test_raw_response_ingest_events(self, client: Casedev) -> None:
        response = client.linc.v1.sessions.with_raw_response.ingest_events(
            id="id",
            frames=[
                {
                    "event": {"foo": "bar"},
                    "seq": 1,
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_ingest_events(self, client: Casedev) -> None:
        with client.linc.v1.sessions.with_streaming_response.ingest_events(
            id="id",
            frames=[
                {
                    "event": {"foo": "bar"},
                    "seq": 1,
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_ingest_events(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.linc.v1.sessions.with_raw_response.ingest_events(
                id="",
                frames=[
                    {
                        "event": {"foo": "bar"},
                        "seq": 1,
                        "type": "type",
                    }
                ],
            )

    @parametrize
    def test_method_retrieve_events(self, client: Casedev) -> None:
        session = client.linc.v1.sessions.retrieve_events(
            id="id",
        )
        assert session is None

    @parametrize
    def test_method_retrieve_events_with_all_params(self, client: Casedev) -> None:
        session = client.linc.v1.sessions.retrieve_events(
            id="id",
            after_seq=0,
            cursor=0,
            exclude_event_types=["string"],
            limit=1,
        )
        assert session is None

    @parametrize
    def test_raw_response_retrieve_events(self, client: Casedev) -> None:
        response = client.linc.v1.sessions.with_raw_response.retrieve_events(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_retrieve_events(self, client: Casedev) -> None:
        with client.linc.v1.sessions.with_streaming_response.retrieve_events(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_events(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.linc.v1.sessions.with_raw_response.retrieve_events(
                id="",
            )

    @parametrize
    def test_method_retrieve_messages(self, client: Casedev) -> None:
        session = client.linc.v1.sessions.retrieve_messages(
            id="id",
        )
        assert session is None

    @parametrize
    def test_method_retrieve_messages_with_all_params(self, client: Casedev) -> None:
        session = client.linc.v1.sessions.retrieve_messages(
            id="id",
            after_seq=0,
            cursor=0,
            limit=1,
        )
        assert session is None

    @parametrize
    def test_raw_response_retrieve_messages(self, client: Casedev) -> None:
        response = client.linc.v1.sessions.with_raw_response.retrieve_messages(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_retrieve_messages(self, client: Casedev) -> None:
        with client.linc.v1.sessions.with_streaming_response.retrieve_messages(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_messages(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.linc.v1.sessions.with_raw_response.retrieve_messages(
                id="",
            )

    @parametrize
    def test_method_retrieve_state(self, client: Casedev) -> None:
        session = client.linc.v1.sessions.retrieve_state(
            "id",
        )
        assert session is None

    @parametrize
    def test_raw_response_retrieve_state(self, client: Casedev) -> None:
        response = client.linc.v1.sessions.with_raw_response.retrieve_state(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_retrieve_state(self, client: Casedev) -> None:
        with client.linc.v1.sessions.with_streaming_response.retrieve_state(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_state(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.linc.v1.sessions.with_raw_response.retrieve_state(
                "",
            )

    @parametrize
    def test_method_send_rpc(self, client: Casedev) -> None:
        session = client.linc.v1.sessions.send_rpc(
            path_id="id",
            type="type",
        )
        assert session is None

    @parametrize
    def test_method_send_rpc_with_all_params(self, client: Casedev) -> None:
        session = client.linc.v1.sessions.send_rpc(
            path_id="id",
            type="type",
            body_id="id",
        )
        assert session is None

    @parametrize
    def test_raw_response_send_rpc(self, client: Casedev) -> None:
        response = client.linc.v1.sessions.with_raw_response.send_rpc(
            path_id="id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_send_rpc(self, client: Casedev) -> None:
        with client.linc.v1.sessions.with_streaming_response.send_rpc(
            path_id="id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send_rpc(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.linc.v1.sessions.with_raw_response.send_rpc(
                path_id="",
                type="type",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        session = await async_client.linc.v1.sessions.create()
        assert session is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        session = await async_client.linc.v1.sessions.create(
            document_template_slugs=["string"],
            idle_timeout_ms=0,
            include_document_templates=True,
            instructions="instructions",
            model="model",
            scoped_api_key="scopedApiKey",
            service_tier="default",
            skill_slugs=["string"],
            title="title",
            vault_ids=["string"],
        )
        assert session is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.linc.v1.sessions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.linc.v1.sessions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        session = await async_client.linc.v1.sessions.delete(
            "id",
        )
        assert session is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.linc.v1.sessions.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.linc.v1.sessions.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.linc.v1.sessions.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncCasedev) -> None:
        session = await async_client.linc.v1.sessions.cancel(
            id="id",
        )
        assert session is None

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncCasedev) -> None:
        session = await async_client.linc.v1.sessions.cancel(
            id="id",
            clear_queue=True,
        )
        assert session is None

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncCasedev) -> None:
        response = await async_client.linc.v1.sessions.with_raw_response.cancel(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncCasedev) -> None:
        async with async_client.linc.v1.sessions.with_streaming_response.cancel(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.linc.v1.sessions.with_raw_response.cancel(
                id="",
            )

    @parametrize
    async def test_method_ingest_events(self, async_client: AsyncCasedev) -> None:
        session = await async_client.linc.v1.sessions.ingest_events(
            id="id",
            frames=[
                {
                    "event": {"foo": "bar"},
                    "seq": 1,
                    "type": "type",
                }
            ],
        )
        assert session is None

    @parametrize
    async def test_raw_response_ingest_events(self, async_client: AsyncCasedev) -> None:
        response = await async_client.linc.v1.sessions.with_raw_response.ingest_events(
            id="id",
            frames=[
                {
                    "event": {"foo": "bar"},
                    "seq": 1,
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_ingest_events(self, async_client: AsyncCasedev) -> None:
        async with async_client.linc.v1.sessions.with_streaming_response.ingest_events(
            id="id",
            frames=[
                {
                    "event": {"foo": "bar"},
                    "seq": 1,
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_ingest_events(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.linc.v1.sessions.with_raw_response.ingest_events(
                id="",
                frames=[
                    {
                        "event": {"foo": "bar"},
                        "seq": 1,
                        "type": "type",
                    }
                ],
            )

    @parametrize
    async def test_method_retrieve_events(self, async_client: AsyncCasedev) -> None:
        session = await async_client.linc.v1.sessions.retrieve_events(
            id="id",
        )
        assert session is None

    @parametrize
    async def test_method_retrieve_events_with_all_params(self, async_client: AsyncCasedev) -> None:
        session = await async_client.linc.v1.sessions.retrieve_events(
            id="id",
            after_seq=0,
            cursor=0,
            exclude_event_types=["string"],
            limit=1,
        )
        assert session is None

    @parametrize
    async def test_raw_response_retrieve_events(self, async_client: AsyncCasedev) -> None:
        response = await async_client.linc.v1.sessions.with_raw_response.retrieve_events(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_retrieve_events(self, async_client: AsyncCasedev) -> None:
        async with async_client.linc.v1.sessions.with_streaming_response.retrieve_events(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_events(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.linc.v1.sessions.with_raw_response.retrieve_events(
                id="",
            )

    @parametrize
    async def test_method_retrieve_messages(self, async_client: AsyncCasedev) -> None:
        session = await async_client.linc.v1.sessions.retrieve_messages(
            id="id",
        )
        assert session is None

    @parametrize
    async def test_method_retrieve_messages_with_all_params(self, async_client: AsyncCasedev) -> None:
        session = await async_client.linc.v1.sessions.retrieve_messages(
            id="id",
            after_seq=0,
            cursor=0,
            limit=1,
        )
        assert session is None

    @parametrize
    async def test_raw_response_retrieve_messages(self, async_client: AsyncCasedev) -> None:
        response = await async_client.linc.v1.sessions.with_raw_response.retrieve_messages(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_retrieve_messages(self, async_client: AsyncCasedev) -> None:
        async with async_client.linc.v1.sessions.with_streaming_response.retrieve_messages(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_messages(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.linc.v1.sessions.with_raw_response.retrieve_messages(
                id="",
            )

    @parametrize
    async def test_method_retrieve_state(self, async_client: AsyncCasedev) -> None:
        session = await async_client.linc.v1.sessions.retrieve_state(
            "id",
        )
        assert session is None

    @parametrize
    async def test_raw_response_retrieve_state(self, async_client: AsyncCasedev) -> None:
        response = await async_client.linc.v1.sessions.with_raw_response.retrieve_state(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_retrieve_state(self, async_client: AsyncCasedev) -> None:
        async with async_client.linc.v1.sessions.with_streaming_response.retrieve_state(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_state(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.linc.v1.sessions.with_raw_response.retrieve_state(
                "",
            )

    @parametrize
    async def test_method_send_rpc(self, async_client: AsyncCasedev) -> None:
        session = await async_client.linc.v1.sessions.send_rpc(
            path_id="id",
            type="type",
        )
        assert session is None

    @parametrize
    async def test_method_send_rpc_with_all_params(self, async_client: AsyncCasedev) -> None:
        session = await async_client.linc.v1.sessions.send_rpc(
            path_id="id",
            type="type",
            body_id="id",
        )
        assert session is None

    @parametrize
    async def test_raw_response_send_rpc(self, async_client: AsyncCasedev) -> None:
        response = await async_client.linc.v1.sessions.with_raw_response.send_rpc(
            path_id="id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_send_rpc(self, async_client: AsyncCasedev) -> None:
        async with async_client.linc.v1.sessions.with_streaming_response.send_rpc(
            path_id="id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send_rpc(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.linc.v1.sessions.with_raw_response.send_rpc(
                path_id="",
                type="type",
            )
