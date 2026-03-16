# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboxes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Casedev) -> None:
        inbox = client.mail.v1.inboxes.create()
        assert inbox is None

    @parametrize
    def test_method_create_with_all_params(self, client: Casedev) -> None:
        inbox = client.mail.v1.inboxes.create(
            address="address",
            display_name="displayName",
        )
        assert inbox is None

    @parametrize
    def test_raw_response_create(self, client: Casedev) -> None:
        response = client.mail.v1.inboxes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert inbox is None

    @parametrize
    def test_streaming_response_create(self, client: Casedev) -> None:
        with client.mail.v1.inboxes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Casedev) -> None:
        inbox = client.mail.v1.inboxes.retrieve(
            "inboxId",
        )
        assert inbox is None

    @parametrize
    def test_raw_response_retrieve(self, client: Casedev) -> None:
        response = client.mail.v1.inboxes.with_raw_response.retrieve(
            "inboxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert inbox is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Casedev) -> None:
        with client.mail.v1.inboxes.with_streaming_response.retrieve(
            "inboxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.mail.v1.inboxes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Casedev) -> None:
        inbox = client.mail.v1.inboxes.list()
        assert inbox is None

    @parametrize
    def test_raw_response_list(self, client: Casedev) -> None:
        response = client.mail.v1.inboxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert inbox is None

    @parametrize
    def test_streaming_response_list(self, client: Casedev) -> None:
        with client.mail.v1.inboxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Casedev) -> None:
        inbox = client.mail.v1.inboxes.delete(
            "inboxId",
        )
        assert inbox is None

    @parametrize
    def test_raw_response_delete(self, client: Casedev) -> None:
        response = client.mail.v1.inboxes.with_raw_response.delete(
            "inboxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert inbox is None

    @parametrize
    def test_streaming_response_delete(self, client: Casedev) -> None:
        with client.mail.v1.inboxes.with_streaming_response.delete(
            "inboxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.mail.v1.inboxes.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get_attachment(self, client: Casedev) -> None:
        inbox = client.mail.v1.inboxes.get_attachment(
            attachment_id="attachmentId",
            inbox_id="inboxId",
            message_id="messageId",
        )
        assert inbox is None

    @parametrize
    def test_raw_response_get_attachment(self, client: Casedev) -> None:
        response = client.mail.v1.inboxes.with_raw_response.get_attachment(
            attachment_id="attachmentId",
            inbox_id="inboxId",
            message_id="messageId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert inbox is None

    @parametrize
    def test_streaming_response_get_attachment(self, client: Casedev) -> None:
        with client.mail.v1.inboxes.with_streaming_response.get_attachment(
            attachment_id="attachmentId",
            inbox_id="inboxId",
            message_id="messageId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_attachment(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.mail.v1.inboxes.with_raw_response.get_attachment(
                attachment_id="attachmentId",
                inbox_id="",
                message_id="messageId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.mail.v1.inboxes.with_raw_response.get_attachment(
                attachment_id="attachmentId",
                inbox_id="inboxId",
                message_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attachment_id` but received ''"):
            client.mail.v1.inboxes.with_raw_response.get_attachment(
                attachment_id="",
                inbox_id="inboxId",
                message_id="messageId",
            )

    @parametrize
    def test_method_get_message(self, client: Casedev) -> None:
        inbox = client.mail.v1.inboxes.get_message(
            message_id="messageId",
            inbox_id="inboxId",
        )
        assert inbox is None

    @parametrize
    def test_raw_response_get_message(self, client: Casedev) -> None:
        response = client.mail.v1.inboxes.with_raw_response.get_message(
            message_id="messageId",
            inbox_id="inboxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert inbox is None

    @parametrize
    def test_streaming_response_get_message(self, client: Casedev) -> None:
        with client.mail.v1.inboxes.with_streaming_response.get_message(
            message_id="messageId",
            inbox_id="inboxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_message(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.mail.v1.inboxes.with_raw_response.get_message(
                message_id="messageId",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.mail.v1.inboxes.with_raw_response.get_message(
                message_id="",
                inbox_id="inboxId",
            )

    @parametrize
    def test_method_list_messages(self, client: Casedev) -> None:
        inbox = client.mail.v1.inboxes.list_messages(
            "inboxId",
        )
        assert inbox is None

    @parametrize
    def test_raw_response_list_messages(self, client: Casedev) -> None:
        response = client.mail.v1.inboxes.with_raw_response.list_messages(
            "inboxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert inbox is None

    @parametrize
    def test_streaming_response_list_messages(self, client: Casedev) -> None:
        with client.mail.v1.inboxes.with_streaming_response.list_messages(
            "inboxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_messages(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.mail.v1.inboxes.with_raw_response.list_messages(
                "",
            )

    @parametrize
    def test_method_reply(self, client: Casedev) -> None:
        inbox = client.mail.v1.inboxes.reply(
            message_id="messageId",
            inbox_id="inboxId",
        )
        assert inbox is None

    @parametrize
    def test_raw_response_reply(self, client: Casedev) -> None:
        response = client.mail.v1.inboxes.with_raw_response.reply(
            message_id="messageId",
            inbox_id="inboxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert inbox is None

    @parametrize
    def test_streaming_response_reply(self, client: Casedev) -> None:
        with client.mail.v1.inboxes.with_streaming_response.reply(
            message_id="messageId",
            inbox_id="inboxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reply(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.mail.v1.inboxes.with_raw_response.reply(
                message_id="messageId",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.mail.v1.inboxes.with_raw_response.reply(
                message_id="",
                inbox_id="inboxId",
            )

    @parametrize
    def test_method_send(self, client: Casedev) -> None:
        inbox = client.mail.v1.inboxes.send(
            "inboxId",
        )
        assert inbox is None

    @parametrize
    def test_raw_response_send(self, client: Casedev) -> None:
        response = client.mail.v1.inboxes.with_raw_response.send(
            "inboxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert inbox is None

    @parametrize
    def test_streaming_response_send(self, client: Casedev) -> None:
        with client.mail.v1.inboxes.with_streaming_response.send(
            "inboxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send(self, client: Casedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.mail.v1.inboxes.with_raw_response.send(
                "",
            )


class TestAsyncInboxes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCasedev) -> None:
        inbox = await async_client.mail.v1.inboxes.create()
        assert inbox is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCasedev) -> None:
        inbox = await async_client.mail.v1.inboxes.create(
            address="address",
            display_name="displayName",
        )
        assert inbox is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCasedev) -> None:
        response = await async_client.mail.v1.inboxes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert inbox is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCasedev) -> None:
        async with async_client.mail.v1.inboxes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCasedev) -> None:
        inbox = await async_client.mail.v1.inboxes.retrieve(
            "inboxId",
        )
        assert inbox is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCasedev) -> None:
        response = await async_client.mail.v1.inboxes.with_raw_response.retrieve(
            "inboxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert inbox is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCasedev) -> None:
        async with async_client.mail.v1.inboxes.with_streaming_response.retrieve(
            "inboxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.mail.v1.inboxes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCasedev) -> None:
        inbox = await async_client.mail.v1.inboxes.list()
        assert inbox is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCasedev) -> None:
        response = await async_client.mail.v1.inboxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert inbox is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCasedev) -> None:
        async with async_client.mail.v1.inboxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncCasedev) -> None:
        inbox = await async_client.mail.v1.inboxes.delete(
            "inboxId",
        )
        assert inbox is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCasedev) -> None:
        response = await async_client.mail.v1.inboxes.with_raw_response.delete(
            "inboxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert inbox is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCasedev) -> None:
        async with async_client.mail.v1.inboxes.with_streaming_response.delete(
            "inboxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.mail.v1.inboxes.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get_attachment(self, async_client: AsyncCasedev) -> None:
        inbox = await async_client.mail.v1.inboxes.get_attachment(
            attachment_id="attachmentId",
            inbox_id="inboxId",
            message_id="messageId",
        )
        assert inbox is None

    @parametrize
    async def test_raw_response_get_attachment(self, async_client: AsyncCasedev) -> None:
        response = await async_client.mail.v1.inboxes.with_raw_response.get_attachment(
            attachment_id="attachmentId",
            inbox_id="inboxId",
            message_id="messageId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert inbox is None

    @parametrize
    async def test_streaming_response_get_attachment(self, async_client: AsyncCasedev) -> None:
        async with async_client.mail.v1.inboxes.with_streaming_response.get_attachment(
            attachment_id="attachmentId",
            inbox_id="inboxId",
            message_id="messageId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_attachment(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.mail.v1.inboxes.with_raw_response.get_attachment(
                attachment_id="attachmentId",
                inbox_id="",
                message_id="messageId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.mail.v1.inboxes.with_raw_response.get_attachment(
                attachment_id="attachmentId",
                inbox_id="inboxId",
                message_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attachment_id` but received ''"):
            await async_client.mail.v1.inboxes.with_raw_response.get_attachment(
                attachment_id="",
                inbox_id="inboxId",
                message_id="messageId",
            )

    @parametrize
    async def test_method_get_message(self, async_client: AsyncCasedev) -> None:
        inbox = await async_client.mail.v1.inboxes.get_message(
            message_id="messageId",
            inbox_id="inboxId",
        )
        assert inbox is None

    @parametrize
    async def test_raw_response_get_message(self, async_client: AsyncCasedev) -> None:
        response = await async_client.mail.v1.inboxes.with_raw_response.get_message(
            message_id="messageId",
            inbox_id="inboxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert inbox is None

    @parametrize
    async def test_streaming_response_get_message(self, async_client: AsyncCasedev) -> None:
        async with async_client.mail.v1.inboxes.with_streaming_response.get_message(
            message_id="messageId",
            inbox_id="inboxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_message(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.mail.v1.inboxes.with_raw_response.get_message(
                message_id="messageId",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.mail.v1.inboxes.with_raw_response.get_message(
                message_id="",
                inbox_id="inboxId",
            )

    @parametrize
    async def test_method_list_messages(self, async_client: AsyncCasedev) -> None:
        inbox = await async_client.mail.v1.inboxes.list_messages(
            "inboxId",
        )
        assert inbox is None

    @parametrize
    async def test_raw_response_list_messages(self, async_client: AsyncCasedev) -> None:
        response = await async_client.mail.v1.inboxes.with_raw_response.list_messages(
            "inboxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert inbox is None

    @parametrize
    async def test_streaming_response_list_messages(self, async_client: AsyncCasedev) -> None:
        async with async_client.mail.v1.inboxes.with_streaming_response.list_messages(
            "inboxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_messages(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.mail.v1.inboxes.with_raw_response.list_messages(
                "",
            )

    @parametrize
    async def test_method_reply(self, async_client: AsyncCasedev) -> None:
        inbox = await async_client.mail.v1.inboxes.reply(
            message_id="messageId",
            inbox_id="inboxId",
        )
        assert inbox is None

    @parametrize
    async def test_raw_response_reply(self, async_client: AsyncCasedev) -> None:
        response = await async_client.mail.v1.inboxes.with_raw_response.reply(
            message_id="messageId",
            inbox_id="inboxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert inbox is None

    @parametrize
    async def test_streaming_response_reply(self, async_client: AsyncCasedev) -> None:
        async with async_client.mail.v1.inboxes.with_streaming_response.reply(
            message_id="messageId",
            inbox_id="inboxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reply(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.mail.v1.inboxes.with_raw_response.reply(
                message_id="messageId",
                inbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.mail.v1.inboxes.with_raw_response.reply(
                message_id="",
                inbox_id="inboxId",
            )

    @parametrize
    async def test_method_send(self, async_client: AsyncCasedev) -> None:
        inbox = await async_client.mail.v1.inboxes.send(
            "inboxId",
        )
        assert inbox is None

    @parametrize
    async def test_raw_response_send(self, async_client: AsyncCasedev) -> None:
        response = await async_client.mail.v1.inboxes.with_raw_response.send(
            "inboxId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert inbox is None

    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncCasedev) -> None:
        async with async_client.mail.v1.inboxes.with_streaming_response.send(
            "inboxId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send(self, async_client: AsyncCasedev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.mail.v1.inboxes.with_raw_response.send(
                "",
            )
