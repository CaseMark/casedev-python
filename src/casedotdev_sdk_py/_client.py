# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import index
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, CasedotdevError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.llm import llm
from .resources.ocr import ocr
from .resources.vault import vault
from .resources.voice import voice
from .resources.format import format
from .resources.actions import actions
from .resources.billing import billing
from .resources.convert import convert
from .resources.webhooks import webhooks
from .resources.workflows import workflows

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Casedotdev",
    "AsyncCasedotdev",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.case.dev",
    "environment_1": "http://localhost:2728",
}


class Casedotdev(SyncAPIClient):
    actions: actions.ActionsResource
    billing: billing.BillingResource
    convert: convert.ConvertResource
    format: format.FormatResource
    index: index.IndexResource
    llm: llm.LlmResource
    ocr: ocr.OcrResource
    vault: vault.VaultResource
    voice: voice.VoiceResource
    webhooks: webhooks.WebhooksResource
    workflows: workflows.WorkflowsResource
    with_raw_response: CasedotdevWithRawResponse
    with_streaming_response: CasedotdevWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Casedotdev client instance.

        This automatically infers the `api_key` argument from the `ROUTER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ROUTER_API_KEY")
        if api_key is None:
            raise CasedotdevError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ROUTER_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("CASEDOTDEV_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `CASEDOTDEV_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.actions = actions.ActionsResource(self)
        self.billing = billing.BillingResource(self)
        self.convert = convert.ConvertResource(self)
        self.format = format.FormatResource(self)
        self.index = index.IndexResource(self)
        self.llm = llm.LlmResource(self)
        self.ocr = ocr.OcrResource(self)
        self.vault = vault.VaultResource(self)
        self.voice = voice.VoiceResource(self)
        self.webhooks = webhooks.WebhooksResource(self)
        self.workflows = workflows.WorkflowsResource(self)
        self.with_raw_response = CasedotdevWithRawResponse(self)
        self.with_streaming_response = CasedotdevWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCasedotdev(AsyncAPIClient):
    actions: actions.AsyncActionsResource
    billing: billing.AsyncBillingResource
    convert: convert.AsyncConvertResource
    format: format.AsyncFormatResource
    index: index.AsyncIndexResource
    llm: llm.AsyncLlmResource
    ocr: ocr.AsyncOcrResource
    vault: vault.AsyncVaultResource
    voice: voice.AsyncVoiceResource
    webhooks: webhooks.AsyncWebhooksResource
    workflows: workflows.AsyncWorkflowsResource
    with_raw_response: AsyncCasedotdevWithRawResponse
    with_streaming_response: AsyncCasedotdevWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncCasedotdev client instance.

        This automatically infers the `api_key` argument from the `ROUTER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ROUTER_API_KEY")
        if api_key is None:
            raise CasedotdevError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ROUTER_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("CASEDOTDEV_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `CASEDOTDEV_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.actions = actions.AsyncActionsResource(self)
        self.billing = billing.AsyncBillingResource(self)
        self.convert = convert.AsyncConvertResource(self)
        self.format = format.AsyncFormatResource(self)
        self.index = index.AsyncIndexResource(self)
        self.llm = llm.AsyncLlmResource(self)
        self.ocr = ocr.AsyncOcrResource(self)
        self.vault = vault.AsyncVaultResource(self)
        self.voice = voice.AsyncVoiceResource(self)
        self.webhooks = webhooks.AsyncWebhooksResource(self)
        self.workflows = workflows.AsyncWorkflowsResource(self)
        self.with_raw_response = AsyncCasedotdevWithRawResponse(self)
        self.with_streaming_response = AsyncCasedotdevWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CasedotdevWithRawResponse:
    def __init__(self, client: Casedotdev) -> None:
        self.actions = actions.ActionsResourceWithRawResponse(client.actions)
        self.billing = billing.BillingResourceWithRawResponse(client.billing)
        self.convert = convert.ConvertResourceWithRawResponse(client.convert)
        self.format = format.FormatResourceWithRawResponse(client.format)
        self.index = index.IndexResourceWithRawResponse(client.index)
        self.llm = llm.LlmResourceWithRawResponse(client.llm)
        self.ocr = ocr.OcrResourceWithRawResponse(client.ocr)
        self.vault = vault.VaultResourceWithRawResponse(client.vault)
        self.voice = voice.VoiceResourceWithRawResponse(client.voice)
        self.webhooks = webhooks.WebhooksResourceWithRawResponse(client.webhooks)
        self.workflows = workflows.WorkflowsResourceWithRawResponse(client.workflows)


class AsyncCasedotdevWithRawResponse:
    def __init__(self, client: AsyncCasedotdev) -> None:
        self.actions = actions.AsyncActionsResourceWithRawResponse(client.actions)
        self.billing = billing.AsyncBillingResourceWithRawResponse(client.billing)
        self.convert = convert.AsyncConvertResourceWithRawResponse(client.convert)
        self.format = format.AsyncFormatResourceWithRawResponse(client.format)
        self.index = index.AsyncIndexResourceWithRawResponse(client.index)
        self.llm = llm.AsyncLlmResourceWithRawResponse(client.llm)
        self.ocr = ocr.AsyncOcrResourceWithRawResponse(client.ocr)
        self.vault = vault.AsyncVaultResourceWithRawResponse(client.vault)
        self.voice = voice.AsyncVoiceResourceWithRawResponse(client.voice)
        self.webhooks = webhooks.AsyncWebhooksResourceWithRawResponse(client.webhooks)
        self.workflows = workflows.AsyncWorkflowsResourceWithRawResponse(client.workflows)


class CasedotdevWithStreamedResponse:
    def __init__(self, client: Casedotdev) -> None:
        self.actions = actions.ActionsResourceWithStreamingResponse(client.actions)
        self.billing = billing.BillingResourceWithStreamingResponse(client.billing)
        self.convert = convert.ConvertResourceWithStreamingResponse(client.convert)
        self.format = format.FormatResourceWithStreamingResponse(client.format)
        self.index = index.IndexResourceWithStreamingResponse(client.index)
        self.llm = llm.LlmResourceWithStreamingResponse(client.llm)
        self.ocr = ocr.OcrResourceWithStreamingResponse(client.ocr)
        self.vault = vault.VaultResourceWithStreamingResponse(client.vault)
        self.voice = voice.VoiceResourceWithStreamingResponse(client.voice)
        self.webhooks = webhooks.WebhooksResourceWithStreamingResponse(client.webhooks)
        self.workflows = workflows.WorkflowsResourceWithStreamingResponse(client.workflows)


class AsyncCasedotdevWithStreamedResponse:
    def __init__(self, client: AsyncCasedotdev) -> None:
        self.actions = actions.AsyncActionsResourceWithStreamingResponse(client.actions)
        self.billing = billing.AsyncBillingResourceWithStreamingResponse(client.billing)
        self.convert = convert.AsyncConvertResourceWithStreamingResponse(client.convert)
        self.format = format.AsyncFormatResourceWithStreamingResponse(client.format)
        self.index = index.AsyncIndexResourceWithStreamingResponse(client.index)
        self.llm = llm.AsyncLlmResourceWithStreamingResponse(client.llm)
        self.ocr = ocr.AsyncOcrResourceWithStreamingResponse(client.ocr)
        self.vault = vault.AsyncVaultResourceWithStreamingResponse(client.vault)
        self.voice = voice.AsyncVoiceResourceWithStreamingResponse(client.voice)
        self.webhooks = webhooks.AsyncWebhooksResourceWithStreamingResponse(client.webhooks)
        self.workflows = workflows.AsyncWorkflowsResourceWithStreamingResponse(client.workflows)


Client = Casedotdev

AsyncClient = AsyncCasedotdev
