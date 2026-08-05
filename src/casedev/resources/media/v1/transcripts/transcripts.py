# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .search import (
    SearchResource,
    AsyncSearchResource,
    SearchResourceWithRawResponse,
    AsyncSearchResourceWithRawResponse,
    SearchResourceWithStreamingResponse,
    AsyncSearchResourceWithStreamingResponse,
)
from .retrieve import (
    RetrieveResource,
    AsyncRetrieveResource,
    RetrieveResourceWithRawResponse,
    AsyncRetrieveResourceWithRawResponse,
    RetrieveResourceWithStreamingResponse,
    AsyncRetrieveResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TranscriptsResource", "AsyncTranscriptsResource"]


class TranscriptsResource(SyncAPIResource):
    @cached_property
    def search(self) -> SearchResource:
        """Transcript retrieval and captioned media clip generation"""
        return SearchResource(self._client)

    @cached_property
    def retrieve(self) -> RetrieveResource:
        """Transcript retrieval and captioned media clip generation"""
        return RetrieveResource(self._client)

    @cached_property
    def with_raw_response(self) -> TranscriptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return TranscriptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranscriptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return TranscriptsResourceWithStreamingResponse(self)


class AsyncTranscriptsResource(AsyncAPIResource):
    @cached_property
    def search(self) -> AsyncSearchResource:
        """Transcript retrieval and captioned media clip generation"""
        return AsyncSearchResource(self._client)

    @cached_property
    def retrieve(self) -> AsyncRetrieveResource:
        """Transcript retrieval and captioned media clip generation"""
        return AsyncRetrieveResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTranscriptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTranscriptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranscriptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncTranscriptsResourceWithStreamingResponse(self)


class TranscriptsResourceWithRawResponse:
    def __init__(self, transcripts: TranscriptsResource) -> None:
        self._transcripts = transcripts

    @cached_property
    def search(self) -> SearchResourceWithRawResponse:
        """Transcript retrieval and captioned media clip generation"""
        return SearchResourceWithRawResponse(self._transcripts.search)

    @cached_property
    def retrieve(self) -> RetrieveResourceWithRawResponse:
        """Transcript retrieval and captioned media clip generation"""
        return RetrieveResourceWithRawResponse(self._transcripts.retrieve)


class AsyncTranscriptsResourceWithRawResponse:
    def __init__(self, transcripts: AsyncTranscriptsResource) -> None:
        self._transcripts = transcripts

    @cached_property
    def search(self) -> AsyncSearchResourceWithRawResponse:
        """Transcript retrieval and captioned media clip generation"""
        return AsyncSearchResourceWithRawResponse(self._transcripts.search)

    @cached_property
    def retrieve(self) -> AsyncRetrieveResourceWithRawResponse:
        """Transcript retrieval and captioned media clip generation"""
        return AsyncRetrieveResourceWithRawResponse(self._transcripts.retrieve)


class TranscriptsResourceWithStreamingResponse:
    def __init__(self, transcripts: TranscriptsResource) -> None:
        self._transcripts = transcripts

    @cached_property
    def search(self) -> SearchResourceWithStreamingResponse:
        """Transcript retrieval and captioned media clip generation"""
        return SearchResourceWithStreamingResponse(self._transcripts.search)

    @cached_property
    def retrieve(self) -> RetrieveResourceWithStreamingResponse:
        """Transcript retrieval and captioned media clip generation"""
        return RetrieveResourceWithStreamingResponse(self._transcripts.retrieve)


class AsyncTranscriptsResourceWithStreamingResponse:
    def __init__(self, transcripts: AsyncTranscriptsResource) -> None:
        self._transcripts = transcripts

    @cached_property
    def search(self) -> AsyncSearchResourceWithStreamingResponse:
        """Transcript retrieval and captioned media clip generation"""
        return AsyncSearchResourceWithStreamingResponse(self._transcripts.search)

    @cached_property
    def retrieve(self) -> AsyncRetrieveResourceWithStreamingResponse:
        """Transcript retrieval and captioned media clip generation"""
        return AsyncRetrieveResourceWithStreamingResponse(self._transcripts.retrieve)
