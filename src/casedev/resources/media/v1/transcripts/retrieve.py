# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.media.v1.transcripts import retrieve_create_params
from .....types.media.v1.transcripts.retrieve_create_response import RetrieveCreateResponse

__all__ = ["RetrieveResource", "AsyncRetrieveResource"]


class RetrieveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetrieveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return RetrieveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetrieveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return RetrieveResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        object_id: str,
        vault_id: str,
        transcript: retrieve_create_params.Transcript | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrieveCreateResponse:
        """
        Retrieves the full transcript text for a vault transcript object or an
        audio/video source object with a completed transcription job. When object_id is
        a source media object, access to that source object grants access to its
        generated transcript artifact.

        Args:
          object_id: Object ID for either the source audio/video file or transcript artifact.

          vault_id: Vault ID containing the source media or transcript object.

          transcript: Alternative nested transcript object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/media/v1/transcripts/retrieve",
            body=maybe_transform(
                {
                    "object_id": object_id,
                    "vault_id": vault_id,
                    "transcript": transcript,
                },
                retrieve_create_params.RetrieveCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrieveCreateResponse,
        )


class AsyncRetrieveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetrieveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetrieveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetrieveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncRetrieveResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        object_id: str,
        vault_id: str,
        transcript: retrieve_create_params.Transcript | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrieveCreateResponse:
        """
        Retrieves the full transcript text for a vault transcript object or an
        audio/video source object with a completed transcription job. When object_id is
        a source media object, access to that source object grants access to its
        generated transcript artifact.

        Args:
          object_id: Object ID for either the source audio/video file or transcript artifact.

          vault_id: Vault ID containing the source media or transcript object.

          transcript: Alternative nested transcript object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/media/v1/transcripts/retrieve",
            body=await async_maybe_transform(
                {
                    "object_id": object_id,
                    "vault_id": vault_id,
                    "transcript": transcript,
                },
                retrieve_create_params.RetrieveCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrieveCreateResponse,
        )


class RetrieveResourceWithRawResponse:
    def __init__(self, retrieve: RetrieveResource) -> None:
        self._retrieve = retrieve

        self.create = to_raw_response_wrapper(
            retrieve.create,
        )


class AsyncRetrieveResourceWithRawResponse:
    def __init__(self, retrieve: AsyncRetrieveResource) -> None:
        self._retrieve = retrieve

        self.create = async_to_raw_response_wrapper(
            retrieve.create,
        )


class RetrieveResourceWithStreamingResponse:
    def __init__(self, retrieve: RetrieveResource) -> None:
        self._retrieve = retrieve

        self.create = to_streamed_response_wrapper(
            retrieve.create,
        )


class AsyncRetrieveResourceWithStreamingResponse:
    def __init__(self, retrieve: AsyncRetrieveResource) -> None:
        self._retrieve = retrieve

        self.create = async_to_streamed_response_wrapper(
            retrieve.create,
        )
