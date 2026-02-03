# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Iterable, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.superdoc import v1_convert_params, v1_annotate_params

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

    def annotate(
        self,
        *,
        document: v1_annotate_params.Document,
        fields: Iterable[v1_annotate_params.Field],
        output_format: Literal["docx", "pdf"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Populate fields inside a DOCX template using SuperDoc annotations.

        Supports
        text, images, dates, and numbers. Can target individual fields by ID or multiple
        fields by group.

        Args:
          document: Document source - provide either URL or base64

          fields: Fields to populate in the template

          output_format: Output format for the annotated document

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._post(
            "/superdoc/v1/annotate",
            body=maybe_transform(
                {
                    "document": document,
                    "fields": fields,
                    "output_format": output_format,
                },
                v1_annotate_params.V1AnnotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def convert(
        self,
        *,
        from_: Literal["docx", "md", "html"],
        document_base64: str | Omit = omit,
        document_url: str | Omit = omit,
        to: Literal["pdf", "docx"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Convert documents between formats using SuperDoc.

        Supports DOCX to PDF, Markdown
        to DOCX, and HTML to DOCX conversions.

        Args:
          from_: Source format of the document

          document_base64: Base64-encoded document content

          document_url: URL to the document to convert

          to: Target format for conversion

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "from_": from_,
                "document_base64": document_base64,
                "document_url": document_url,
                "to": to,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/superdoc/v1/convert",
            body=maybe_transform(body, v1_convert_params.V1ConvertParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
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

    async def annotate(
        self,
        *,
        document: v1_annotate_params.Document,
        fields: Iterable[v1_annotate_params.Field],
        output_format: Literal["docx", "pdf"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Populate fields inside a DOCX template using SuperDoc annotations.

        Supports
        text, images, dates, and numbers. Can target individual fields by ID or multiple
        fields by group.

        Args:
          document: Document source - provide either URL or base64

          fields: Fields to populate in the template

          output_format: Output format for the annotated document

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._post(
            "/superdoc/v1/annotate",
            body=await async_maybe_transform(
                {
                    "document": document,
                    "fields": fields,
                    "output_format": output_format,
                },
                v1_annotate_params.V1AnnotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def convert(
        self,
        *,
        from_: Literal["docx", "md", "html"],
        document_base64: str | Omit = omit,
        document_url: str | Omit = omit,
        to: Literal["pdf", "docx"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Convert documents between formats using SuperDoc.

        Supports DOCX to PDF, Markdown
        to DOCX, and HTML to DOCX conversions.

        Args:
          from_: Source format of the document

          document_base64: Base64-encoded document content

          document_url: URL to the document to convert

          to: Target format for conversion

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "from_": from_,
                "document_base64": document_base64,
                "document_url": document_url,
                "to": to,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/superdoc/v1/convert",
            body=await async_maybe_transform(body, v1_convert_params.V1ConvertParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.annotate = to_custom_raw_response_wrapper(
            v1.annotate,
            BinaryAPIResponse,
        )
        self.convert = to_custom_raw_response_wrapper(
            v1.convert,
            BinaryAPIResponse,
        )


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.annotate = async_to_custom_raw_response_wrapper(
            v1.annotate,
            AsyncBinaryAPIResponse,
        )
        self.convert = async_to_custom_raw_response_wrapper(
            v1.convert,
            AsyncBinaryAPIResponse,
        )


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.annotate = to_custom_streamed_response_wrapper(
            v1.annotate,
            StreamedBinaryAPIResponse,
        )
        self.convert = to_custom_streamed_response_wrapper(
            v1.convert,
            StreamedBinaryAPIResponse,
        )


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.annotate = async_to_custom_streamed_response_wrapper(
            v1.annotate,
            AsyncStreamedBinaryAPIResponse,
        )
        self.convert = async_to_custom_streamed_response_wrapper(
            v1.convert,
            AsyncStreamedBinaryAPIResponse,
        )
