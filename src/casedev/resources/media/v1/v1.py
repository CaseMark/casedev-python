# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .clips import (
    ClipsResource,
    AsyncClipsResource,
    ClipsResourceWithRawResponse,
    AsyncClipsResourceWithRawResponse,
    ClipsResourceWithStreamingResponse,
    AsyncClipsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .transcripts.transcripts import (
    TranscriptsResource,
    AsyncTranscriptsResource,
    TranscriptsResourceWithRawResponse,
    AsyncTranscriptsResourceWithRawResponse,
    TranscriptsResourceWithStreamingResponse,
    AsyncTranscriptsResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def clips(self) -> ClipsResource:
        """Transcript retrieval and captioned media clip generation"""
        return ClipsResource(self._client)

    @cached_property
    def transcripts(self) -> TranscriptsResource:
        return TranscriptsResource(self._client)

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


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def clips(self) -> AsyncClipsResource:
        """Transcript retrieval and captioned media clip generation"""
        return AsyncClipsResource(self._client)

    @cached_property
    def transcripts(self) -> AsyncTranscriptsResource:
        return AsyncTranscriptsResource(self._client)

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


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def clips(self) -> ClipsResourceWithRawResponse:
        """Transcript retrieval and captioned media clip generation"""
        return ClipsResourceWithRawResponse(self._v1.clips)

    @cached_property
    def transcripts(self) -> TranscriptsResourceWithRawResponse:
        return TranscriptsResourceWithRawResponse(self._v1.transcripts)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def clips(self) -> AsyncClipsResourceWithRawResponse:
        """Transcript retrieval and captioned media clip generation"""
        return AsyncClipsResourceWithRawResponse(self._v1.clips)

    @cached_property
    def transcripts(self) -> AsyncTranscriptsResourceWithRawResponse:
        return AsyncTranscriptsResourceWithRawResponse(self._v1.transcripts)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def clips(self) -> ClipsResourceWithStreamingResponse:
        """Transcript retrieval and captioned media clip generation"""
        return ClipsResourceWithStreamingResponse(self._v1.clips)

    @cached_property
    def transcripts(self) -> TranscriptsResourceWithStreamingResponse:
        return TranscriptsResourceWithStreamingResponse(self._v1.transcripts)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def clips(self) -> AsyncClipsResourceWithStreamingResponse:
        """Transcript retrieval and captioned media clip generation"""
        return AsyncClipsResourceWithStreamingResponse(self._v1.clips)

    @cached_property
    def transcripts(self) -> AsyncTranscriptsResourceWithStreamingResponse:
        return AsyncTranscriptsResourceWithStreamingResponse(self._v1.transcripts)
