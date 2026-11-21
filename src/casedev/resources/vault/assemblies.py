# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.vault import assembly_create_params
from ..._base_client import make_request_options
from ...types.vault.assembly_create_response import AssemblyCreateResponse
from ...types.vault.assembly_retrieve_response import AssemblyRetrieveResponse

__all__ = ["AssembliesResource", "AsyncAssembliesResource"]


class AssembliesResource(SyncAPIResource):
    """Vault object management, content access, and document operations"""

    @cached_property
    def with_raw_response(self) -> AssembliesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AssembliesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssembliesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AssembliesResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        sources: Iterable[assembly_create_params.Source],
        volumes: Iterable[assembly_create_params.Volume],
        idempotency_key: str,
        bates: assembly_create_params.Bates | Omit = omit,
        client_reference: str | Omit = omit,
        compression: assembly_create_params.Compression | Omit = omit,
        linearize: bool | Omit = omit,
        page_size: Literal["letter"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssemblyCreateResponse:
        """Starts an asynchronous, deterministic PDF assembly.

        The manifest selects page
        ranges from source PDFs in output order, adds an outline, an optional linked
        contents page and optional Bates numbering, and splits the result into volumes.
        Optional compression downsamples oversized scans. Each volume becomes a new
        vault object. Source bookmarks, form fields and page labels are not carried
        over. Outputs are not indexed automatically. Completion is reported through
        vault.assembly webhooks.

        Args:
          sources: Source PDFs, or ingested office files (spreadsheets, CSV/TSV, Word), which are
              assembled from the PDF version ingestion saved for them. A source can also be a
              PDF you made, such as a cover or notice letter, sent inline. Page ranges refer
              to a source by its index in this list.

          bates: Bates numbering that continues across every volume without its own series. Text
              must be printable ASCII.

          compression: Downsamples colour and grayscale scans above maxDpi and re-encodes them. Images
              already stored as 1-bit, JPEG 2000, indexed or CMYK keep their bytes.

          linearize: Optimize volumes for web viewing

          page_size: Put every page upright on a US Letter sheet: portrait pages on a portrait sheet,
              landscape pages on a landscape sheet, other sizes scaled to fit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return self._post(
            path_template("/vault/{id}/assemblies", id=id),
            body=maybe_transform(
                {
                    "sources": sources,
                    "volumes": volumes,
                    "bates": bates,
                    "client_reference": client_reference,
                    "compression": compression,
                    "linearize": linearize,
                    "page_size": page_size,
                },
                assembly_create_params.AssemblyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssemblyCreateResponse,
        )

    def retrieve(
        self,
        assembly_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssemblyRetrieveResponse:
        """Returns the status of a PDF assembly.

        Completed volumes include their page
        count, size, SHA-256 and Bates range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not assembly_id:
            raise ValueError(f"Expected a non-empty value for `assembly_id` but received {assembly_id!r}")
        return self._get(
            path_template("/vault/{id}/assemblies/{assembly_id}", id=id, assembly_id=assembly_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssemblyRetrieveResponse,
        )


class AsyncAssembliesResource(AsyncAPIResource):
    """Vault object management, content access, and document operations"""

    @cached_property
    def with_raw_response(self) -> AsyncAssembliesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssembliesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssembliesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncAssembliesResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        sources: Iterable[assembly_create_params.Source],
        volumes: Iterable[assembly_create_params.Volume],
        idempotency_key: str,
        bates: assembly_create_params.Bates | Omit = omit,
        client_reference: str | Omit = omit,
        compression: assembly_create_params.Compression | Omit = omit,
        linearize: bool | Omit = omit,
        page_size: Literal["letter"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssemblyCreateResponse:
        """Starts an asynchronous, deterministic PDF assembly.

        The manifest selects page
        ranges from source PDFs in output order, adds an outline, an optional linked
        contents page and optional Bates numbering, and splits the result into volumes.
        Optional compression downsamples oversized scans. Each volume becomes a new
        vault object. Source bookmarks, form fields and page labels are not carried
        over. Outputs are not indexed automatically. Completion is reported through
        vault.assembly webhooks.

        Args:
          sources: Source PDFs, or ingested office files (spreadsheets, CSV/TSV, Word), which are
              assembled from the PDF version ingestion saved for them. A source can also be a
              PDF you made, such as a cover or notice letter, sent inline. Page ranges refer
              to a source by its index in this list.

          bates: Bates numbering that continues across every volume without its own series. Text
              must be printable ASCII.

          compression: Downsamples colour and grayscale scans above maxDpi and re-encodes them. Images
              already stored as 1-bit, JPEG 2000, indexed or CMYK keep their bytes.

          linearize: Optimize volumes for web viewing

          page_size: Put every page upright on a US Letter sheet: portrait pages on a portrait sheet,
              landscape pages on a landscape sheet, other sizes scaled to fit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return await self._post(
            path_template("/vault/{id}/assemblies", id=id),
            body=await async_maybe_transform(
                {
                    "sources": sources,
                    "volumes": volumes,
                    "bates": bates,
                    "client_reference": client_reference,
                    "compression": compression,
                    "linearize": linearize,
                    "page_size": page_size,
                },
                assembly_create_params.AssemblyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssemblyCreateResponse,
        )

    async def retrieve(
        self,
        assembly_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssemblyRetrieveResponse:
        """Returns the status of a PDF assembly.

        Completed volumes include their page
        count, size, SHA-256 and Bates range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not assembly_id:
            raise ValueError(f"Expected a non-empty value for `assembly_id` but received {assembly_id!r}")
        return await self._get(
            path_template("/vault/{id}/assemblies/{assembly_id}", id=id, assembly_id=assembly_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssemblyRetrieveResponse,
        )


class AssembliesResourceWithRawResponse:
    def __init__(self, assemblies: AssembliesResource) -> None:
        self._assemblies = assemblies

        self.create = to_raw_response_wrapper(
            assemblies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            assemblies.retrieve,
        )


class AsyncAssembliesResourceWithRawResponse:
    def __init__(self, assemblies: AsyncAssembliesResource) -> None:
        self._assemblies = assemblies

        self.create = async_to_raw_response_wrapper(
            assemblies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            assemblies.retrieve,
        )


class AssembliesResourceWithStreamingResponse:
    def __init__(self, assemblies: AssembliesResource) -> None:
        self._assemblies = assemblies

        self.create = to_streamed_response_wrapper(
            assemblies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            assemblies.retrieve,
        )


class AsyncAssembliesResourceWithStreamingResponse:
    def __init__(self, assemblies: AsyncAssembliesResource) -> None:
        self._assemblies = assemblies

        self.create = async_to_streamed_response_wrapper(
            assemblies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            assemblies.retrieve,
        )
