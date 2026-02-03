# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.translate import v1_detect_params, v1_translate_params, v1_list_languages_params
from ...types.translate.v1_detect_response import V1DetectResponse
from ...types.translate.v1_translate_response import V1TranslateResponse
from ...types.translate.v1_list_languages_response import V1ListLanguagesResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def detect(
        self,
        *,
        q: Union[str, SequenceNotStr[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1DetectResponse:
        """Detect the language of text.

        Returns the most likely language code and
        confidence score. Supports batch detection for multiple texts.

        Args:
          q: Text to detect language for. Can be a single string or an array for batch
              detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/translate/v1/detect",
            body=maybe_transform({"q": q}, v1_detect_params.V1DetectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1DetectResponse,
        )

    def list_languages(
        self,
        *,
        model: Literal["nmt", "base"] | Omit = omit,
        target: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ListLanguagesResponse:
        """Get the list of languages supported for translation.

        Optionally specify a target
        language to get translated language names.

        Args:
          model: Translation model to check language support for

          target: Target language code for translating language names (e.g., 'es' for Spanish
              names)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/translate/v1/languages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "model": model,
                        "target": target,
                    },
                    v1_list_languages_params.V1ListLanguagesParams,
                ),
            ),
            cast_to=V1ListLanguagesResponse,
        )

    def translate(
        self,
        *,
        q: Union[str, SequenceNotStr[str]],
        target: str,
        format: Literal["text", "html"] | Omit = omit,
        model: Literal["nmt", "base"] | Omit = omit,
        source: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1TranslateResponse:
        """Translate text between languages using Google Cloud Translation API.

        Supports
        100+ languages, automatic language detection, HTML preservation, and batch
        translation.

        Args:
          q: Text to translate. Can be a single string or an array for batch translation.

          target: Target language code (ISO 639-1)

          format: Format of the source text. Use 'html' to preserve HTML tags.

          model: Translation model. 'nmt' (Neural Machine Translation) is recommended for
              quality.

          source: Source language code (ISO 639-1). If not specified, language is auto-detected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/translate/v1/translate",
            body=maybe_transform(
                {
                    "q": q,
                    "target": target,
                    "format": format,
                    "model": model,
                    "source": source,
                },
                v1_translate_params.V1TranslateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1TranslateResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def detect(
        self,
        *,
        q: Union[str, SequenceNotStr[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1DetectResponse:
        """Detect the language of text.

        Returns the most likely language code and
        confidence score. Supports batch detection for multiple texts.

        Args:
          q: Text to detect language for. Can be a single string or an array for batch
              detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/translate/v1/detect",
            body=await async_maybe_transform({"q": q}, v1_detect_params.V1DetectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1DetectResponse,
        )

    async def list_languages(
        self,
        *,
        model: Literal["nmt", "base"] | Omit = omit,
        target: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ListLanguagesResponse:
        """Get the list of languages supported for translation.

        Optionally specify a target
        language to get translated language names.

        Args:
          model: Translation model to check language support for

          target: Target language code for translating language names (e.g., 'es' for Spanish
              names)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/translate/v1/languages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "model": model,
                        "target": target,
                    },
                    v1_list_languages_params.V1ListLanguagesParams,
                ),
            ),
            cast_to=V1ListLanguagesResponse,
        )

    async def translate(
        self,
        *,
        q: Union[str, SequenceNotStr[str]],
        target: str,
        format: Literal["text", "html"] | Omit = omit,
        model: Literal["nmt", "base"] | Omit = omit,
        source: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1TranslateResponse:
        """Translate text between languages using Google Cloud Translation API.

        Supports
        100+ languages, automatic language detection, HTML preservation, and batch
        translation.

        Args:
          q: Text to translate. Can be a single string or an array for batch translation.

          target: Target language code (ISO 639-1)

          format: Format of the source text. Use 'html' to preserve HTML tags.

          model: Translation model. 'nmt' (Neural Machine Translation) is recommended for
              quality.

          source: Source language code (ISO 639-1). If not specified, language is auto-detected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/translate/v1/translate",
            body=await async_maybe_transform(
                {
                    "q": q,
                    "target": target,
                    "format": format,
                    "model": model,
                    "source": source,
                },
                v1_translate_params.V1TranslateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1TranslateResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.detect = to_raw_response_wrapper(
            v1.detect,
        )
        self.list_languages = to_raw_response_wrapper(
            v1.list_languages,
        )
        self.translate = to_raw_response_wrapper(
            v1.translate,
        )


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.detect = async_to_raw_response_wrapper(
            v1.detect,
        )
        self.list_languages = async_to_raw_response_wrapper(
            v1.list_languages,
        )
        self.translate = async_to_raw_response_wrapper(
            v1.translate,
        )


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.detect = to_streamed_response_wrapper(
            v1.detect,
        )
        self.list_languages = to_streamed_response_wrapper(
            v1.list_languages,
        )
        self.translate = to_streamed_response_wrapper(
            v1.translate,
        )


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.detect = async_to_streamed_response_wrapper(
            v1.detect,
        )
        self.list_languages = async_to_streamed_response_wrapper(
            v1.list_languages,
        )
        self.translate = async_to_streamed_response_wrapper(
            v1.translate,
        )
