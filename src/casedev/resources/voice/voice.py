# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v1.v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .streaming import (
    StreamingResource,
    AsyncStreamingResource,
    StreamingResourceWithRawResponse,
    AsyncStreamingResourceWithRawResponse,
    StreamingResourceWithStreamingResponse,
    AsyncStreamingResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .transcription import (
    TranscriptionResource,
    AsyncTranscriptionResource,
    TranscriptionResourceWithRawResponse,
    AsyncTranscriptionResourceWithRawResponse,
    TranscriptionResourceWithStreamingResponse,
    AsyncTranscriptionResourceWithStreamingResponse,
)

__all__ = ["VoiceResource", "AsyncVoiceResource"]


class VoiceResource(SyncAPIResource):
    @cached_property
    def streaming(self) -> StreamingResource:
        """Audio transcription and text-to-speech"""
        return StreamingResource(self._client)

    @cached_property
    def transcription(self) -> TranscriptionResource:
        """Audio transcription and text-to-speech"""
        return TranscriptionResource(self._client)

    @cached_property
    def v1(self) -> V1Resource:
        """Audio transcription and text-to-speech"""
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> VoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return VoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return VoiceResourceWithStreamingResponse(self)


class AsyncVoiceResource(AsyncAPIResource):
    @cached_property
    def streaming(self) -> AsyncStreamingResource:
        """Audio transcription and text-to-speech"""
        return AsyncStreamingResource(self._client)

    @cached_property
    def transcription(self) -> AsyncTranscriptionResource:
        """Audio transcription and text-to-speech"""
        return AsyncTranscriptionResource(self._client)

    @cached_property
    def v1(self) -> AsyncV1Resource:
        """Audio transcription and text-to-speech"""
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncVoiceResourceWithStreamingResponse(self)


class VoiceResourceWithRawResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

    @cached_property
    def streaming(self) -> StreamingResourceWithRawResponse:
        """Audio transcription and text-to-speech"""
        return StreamingResourceWithRawResponse(self._voice.streaming)

    @cached_property
    def transcription(self) -> TranscriptionResourceWithRawResponse:
        """Audio transcription and text-to-speech"""
        return TranscriptionResourceWithRawResponse(self._voice.transcription)

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        """Audio transcription and text-to-speech"""
        return V1ResourceWithRawResponse(self._voice.v1)


class AsyncVoiceResourceWithRawResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

    @cached_property
    def streaming(self) -> AsyncStreamingResourceWithRawResponse:
        """Audio transcription and text-to-speech"""
        return AsyncStreamingResourceWithRawResponse(self._voice.streaming)

    @cached_property
    def transcription(self) -> AsyncTranscriptionResourceWithRawResponse:
        """Audio transcription and text-to-speech"""
        return AsyncTranscriptionResourceWithRawResponse(self._voice.transcription)

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        """Audio transcription and text-to-speech"""
        return AsyncV1ResourceWithRawResponse(self._voice.v1)


class VoiceResourceWithStreamingResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

    @cached_property
    def streaming(self) -> StreamingResourceWithStreamingResponse:
        """Audio transcription and text-to-speech"""
        return StreamingResourceWithStreamingResponse(self._voice.streaming)

    @cached_property
    def transcription(self) -> TranscriptionResourceWithStreamingResponse:
        """Audio transcription and text-to-speech"""
        return TranscriptionResourceWithStreamingResponse(self._voice.transcription)

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        """Audio transcription and text-to-speech"""
        return V1ResourceWithStreamingResponse(self._voice.v1)


class AsyncVoiceResourceWithStreamingResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

    @cached_property
    def streaming(self) -> AsyncStreamingResourceWithStreamingResponse:
        """Audio transcription and text-to-speech"""
        return AsyncStreamingResourceWithStreamingResponse(self._voice.streaming)

    @cached_property
    def transcription(self) -> AsyncTranscriptionResourceWithStreamingResponse:
        """Audio transcription and text-to-speech"""
        return AsyncTranscriptionResourceWithStreamingResponse(self._voice.transcription)

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        """Audio transcription and text-to-speech"""
        return AsyncV1ResourceWithStreamingResponse(self._voice.v1)
