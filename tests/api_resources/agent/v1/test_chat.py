# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev.types.agent.v1 import (
    ChatCancelResponse,
    ChatCreateResponse,
    ChatDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        chat = client.agent.v1.chat.create()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        chat = client.agent.v1.chat.create(
            idle_timeout_ms=0,
            model="model",
            title="title",
            vault_ids=["string"],
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.agent.v1.chat.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.agent.v1.chat.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        chat = client.agent.v1.chat.delete(
            "id",
        )
        assert_matches_type(ChatDeleteResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.agent.v1.chat.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatDeleteResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.agent.v1.chat.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatDeleteResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.v1.chat.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: Casedev) -> None:
        chat = client.agent.v1.chat.cancel(
            "id",
        )
        assert_matches_type(ChatCancelResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Casedev) -> None:
        response = client.agent.v1.chat.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCancelResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Casedev) -> None:
        with client.agent.v1.chat.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCancelResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.v1.chat.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_reply_to_question(self, client: Casedev) -> None:
        chat = client.agent.v1.chat.reply_to_question(
            request_id="requestID",
            id="id",
            answers=[["string"]],
        )
        assert chat is None

    @parametrize
    def test_raw_response_reply_to_question(self, client: Casedev) -> None:
        response = client.agent.v1.chat.with_raw_response.reply_to_question(
            request_id="requestID",
            id="id",
            answers=[["string"]],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert chat is None

    @parametrize
    def test_streaming_response_reply_to_question(self, client: Casedev) -> None:
        with client.agent.v1.chat.with_streaming_response.reply_to_question(
            request_id="requestID",
            id="id",
            answers=[["string"]],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reply_to_question(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.v1.chat.with_raw_response.reply_to_question(
                request_id="requestID",
                id="",
                answers=[["string"]],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.agent.v1.chat.with_raw_response.reply_to_question(
                request_id="",
                id="id",
                answers=[["string"]],
            )

    @parametrize
    def test_method_respond(self, client: Casedev) -> None:
        chat_stream = client.agent.v1.chat.respond(
            id="id",
        )
        chat_stream.response.close()

    @parametrize
    def test_method_respond_with_all_params(self, client: Casedev) -> None:
        chat_stream = client.agent.v1.chat.respond(
            id="id",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        chat_stream.response.close()

    @parametrize
    def test_raw_response_respond(self, client: Casedev) -> None:
        response = client.agent.v1.chat.with_raw_response.respond(
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_respond(self, client: Casedev) -> None:
        with client.agent.v1.chat.with_streaming_response.respond(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_respond(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.v1.chat.with_raw_response.respond(
                id="",
            )

    @parametrize
    def test_method_send_message(self, client: Casedev) -> None:
        chat = client.agent.v1.chat.send_message(
            id="id",
        )
        assert chat is None

    @parametrize
    def test_method_send_message_with_all_params(self, client: Casedev) -> None:
        chat = client.agent.v1.chat.send_message(
            id="id",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        assert chat is None

    @parametrize
    def test_raw_response_send_message(self, client: Casedev) -> None:
        response = client.agent.v1.chat.with_raw_response.send_message(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert chat is None

    @parametrize
    def test_streaming_response_send_message(self, client: Casedev) -> None:
        with client.agent.v1.chat.with_streaming_response.send_message(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send_message(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.v1.chat.with_raw_response.send_message(
                id="",
            )

    @parametrize
    def test_method_stream(self, client: Casedev) -> None:
        chat_stream = client.agent.v1.chat.stream(
            id="id",
        )
        chat_stream.response.close()

    @parametrize
    def test_method_stream_with_all_params(self, client: Casedev) -> None:
        chat_stream = client.agent.v1.chat.stream(
            id="id",
            last_event_id=0,
        )
        chat_stream.response.close()

    @parametrize
    def test_raw_response_stream(self, client: Casedev) -> None:
        response = client.agent.v1.chat.with_raw_response.stream(
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_stream(self, client: Casedev) -> None:
        with client.agent.v1.chat.with_streaming_response.stream(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stream(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agent.v1.chat.with_raw_response.stream(
                id="",
            )


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        chat = await async_client.agent.v1.chat.create()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        chat = await async_client.agent.v1.chat.create(
            idle_timeout_ms=0,
            model="model",
            title="title",
            vault_ids=["string"],
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v1.chat.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v1.chat.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        chat = await async_client.agent.v1.chat.delete(
            "id",
        )
        assert_matches_type(ChatDeleteResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v1.chat.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatDeleteResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v1.chat.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatDeleteResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.v1.chat.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncCasedev) -> None:
        chat = await async_client.agent.v1.chat.cancel(
            "id",
        )
        assert_matches_type(ChatCancelResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v1.chat.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCancelResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v1.chat.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCancelResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.v1.chat.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_reply_to_question(self, async_client: AsyncCasedev) -> None:
        chat = await async_client.agent.v1.chat.reply_to_question(
            request_id="requestID",
            id="id",
            answers=[["string"]],
        )
        assert chat is None

    @parametrize
    async def test_raw_response_reply_to_question(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v1.chat.with_raw_response.reply_to_question(
            request_id="requestID",
            id="id",
            answers=[["string"]],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert chat is None

    @parametrize
    async def test_streaming_response_reply_to_question(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v1.chat.with_streaming_response.reply_to_question(
            request_id="requestID",
            id="id",
            answers=[["string"]],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reply_to_question(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.v1.chat.with_raw_response.reply_to_question(
                request_id="requestID",
                id="",
                answers=[["string"]],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.agent.v1.chat.with_raw_response.reply_to_question(
                request_id="",
                id="id",
                answers=[["string"]],
            )

    @parametrize
    async def test_method_respond(self, async_client: AsyncCasedev) -> None:
        chat_stream = await async_client.agent.v1.chat.respond(
            id="id",
        )
        await chat_stream.response.aclose()

    @parametrize
    async def test_method_respond_with_all_params(self, async_client: AsyncCasedev) -> None:
        chat_stream = await async_client.agent.v1.chat.respond(
            id="id",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        await chat_stream.response.aclose()

    @parametrize
    async def test_raw_response_respond(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v1.chat.with_raw_response.respond(
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_respond(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v1.chat.with_streaming_response.respond(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_respond(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.v1.chat.with_raw_response.respond(
                id="",
            )

    @parametrize
    async def test_method_send_message(self, async_client: AsyncCasedev) -> None:
        chat = await async_client.agent.v1.chat.send_message(
            id="id",
        )
        assert chat is None

    @parametrize
    async def test_method_send_message_with_all_params(self, async_client: AsyncCasedev) -> None:
        chat = await async_client.agent.v1.chat.send_message(
            id="id",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        assert chat is None

    @parametrize
    async def test_raw_response_send_message(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v1.chat.with_raw_response.send_message(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert chat is None

    @parametrize
    async def test_streaming_response_send_message(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v1.chat.with_streaming_response.send_message(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send_message(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.v1.chat.with_raw_response.send_message(
                id="",
            )

    @parametrize
    async def test_method_stream(self, async_client: AsyncCasedev) -> None:
        chat_stream = await async_client.agent.v1.chat.stream(
            id="id",
        )
        await chat_stream.response.aclose()

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncCasedev) -> None:
        chat_stream = await async_client.agent.v1.chat.stream(
            id="id",
            last_event_id=0,
        )
        await chat_stream.response.aclose()

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncCasedev) -> None:
        response = await async_client.agent.v1.chat.with_raw_response.stream(
            id="id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncCasedev) -> None:
        async with async_client.agent.v1.chat.with_streaming_response.stream(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stream(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agent.v1.chat.with_raw_response.stream(
                id="",
            )
