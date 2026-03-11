# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
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
from ...types.voice import boost_list_extract_params, boost_list_generate_params
from ..._base_client import make_request_options
from ...types.voice.boost_list_extract_response import BoostListExtractResponse
from ...types.voice.boost_list_generate_response import BoostListGenerateResponse

__all__ = ["BoostListResource", "AsyncBoostListResource"]


class BoostListResource(SyncAPIResource):
    """Audio transcription and text-to-speech"""

    @cached_property
    def with_raw_response(self) -> BoostListResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return BoostListResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BoostListResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return BoostListResourceWithStreamingResponse(self)

    def extract(
        self,
        *,
        categories: List[Literal["person", "organization", "legal_term", "medical", "citation", "email"]] | Omit = omit,
        object_ids: SequenceNotStr[str] | Omit = omit,
        text: str | Omit = omit,
        vault_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BoostListExtractResponse:
        """
        Extracts a categorized word boost list from vault documents or raw text using
        LLM entity extraction. The resulting list can be passed as `word_boost` to the
        transcription endpoint for improved accuracy.

        Args:
          categories: Optional filter for entity categories to extract

          object_ids: Object IDs of documents to extract entities from (PDFs, text files)

          text: Raw text input for entity extraction (alternative to vault documents)

          vault_id: Vault ID containing the source documents (use with object_ids)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/voice/boost-list/extract",
            body=maybe_transform(
                {
                    "categories": categories,
                    "object_ids": object_ids,
                    "text": text,
                    "vault_id": vault_id,
                },
                boost_list_extract_params.BoostListExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BoostListExtractResponse,
        )

    def generate(
        self,
        *,
        transcription_job_id: str,
        categories: List[Literal["person", "organization", "legal_term", "medical", "citation", "email"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BoostListGenerateResponse:
        """
        Generates a categorized word boost list from a completed transcription job.
        Extracts entities from the pass-1 transcript for use as `word_boost` in a second
        transcription pass.

        Args:
          transcription_job_id: Completed pass-1 transcription job ID (tr\\__...)

          categories: Optional filter for entity categories to extract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/voice/boost-list/generate",
            body=maybe_transform(
                {
                    "transcription_job_id": transcription_job_id,
                    "categories": categories,
                },
                boost_list_generate_params.BoostListGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BoostListGenerateResponse,
        )


class AsyncBoostListResource(AsyncAPIResource):
    """Audio transcription and text-to-speech"""

    @cached_property
    def with_raw_response(self) -> AsyncBoostListResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBoostListResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBoostListResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncBoostListResourceWithStreamingResponse(self)

    async def extract(
        self,
        *,
        categories: List[Literal["person", "organization", "legal_term", "medical", "citation", "email"]] | Omit = omit,
        object_ids: SequenceNotStr[str] | Omit = omit,
        text: str | Omit = omit,
        vault_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BoostListExtractResponse:
        """
        Extracts a categorized word boost list from vault documents or raw text using
        LLM entity extraction. The resulting list can be passed as `word_boost` to the
        transcription endpoint for improved accuracy.

        Args:
          categories: Optional filter for entity categories to extract

          object_ids: Object IDs of documents to extract entities from (PDFs, text files)

          text: Raw text input for entity extraction (alternative to vault documents)

          vault_id: Vault ID containing the source documents (use with object_ids)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/voice/boost-list/extract",
            body=await async_maybe_transform(
                {
                    "categories": categories,
                    "object_ids": object_ids,
                    "text": text,
                    "vault_id": vault_id,
                },
                boost_list_extract_params.BoostListExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BoostListExtractResponse,
        )

    async def generate(
        self,
        *,
        transcription_job_id: str,
        categories: List[Literal["person", "organization", "legal_term", "medical", "citation", "email"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BoostListGenerateResponse:
        """
        Generates a categorized word boost list from a completed transcription job.
        Extracts entities from the pass-1 transcript for use as `word_boost` in a second
        transcription pass.

        Args:
          transcription_job_id: Completed pass-1 transcription job ID (tr\\__...)

          categories: Optional filter for entity categories to extract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/voice/boost-list/generate",
            body=await async_maybe_transform(
                {
                    "transcription_job_id": transcription_job_id,
                    "categories": categories,
                },
                boost_list_generate_params.BoostListGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BoostListGenerateResponse,
        )


class BoostListResourceWithRawResponse:
    def __init__(self, boost_list: BoostListResource) -> None:
        self._boost_list = boost_list

        self.extract = to_raw_response_wrapper(
            boost_list.extract,
        )
        self.generate = to_raw_response_wrapper(
            boost_list.generate,
        )


class AsyncBoostListResourceWithRawResponse:
    def __init__(self, boost_list: AsyncBoostListResource) -> None:
        self._boost_list = boost_list

        self.extract = async_to_raw_response_wrapper(
            boost_list.extract,
        )
        self.generate = async_to_raw_response_wrapper(
            boost_list.generate,
        )


class BoostListResourceWithStreamingResponse:
    def __init__(self, boost_list: BoostListResource) -> None:
        self._boost_list = boost_list

        self.extract = to_streamed_response_wrapper(
            boost_list.extract,
        )
        self.generate = to_streamed_response_wrapper(
            boost_list.generate,
        )


class AsyncBoostListResourceWithStreamingResponse:
    def __init__(self, boost_list: AsyncBoostListResource) -> None:
        self._boost_list = boost_list

        self.extract = async_to_streamed_response_wrapper(
            boost_list.extract,
        )
        self.generate = async_to_streamed_response_wrapper(
            boost_list.generate,
        )
