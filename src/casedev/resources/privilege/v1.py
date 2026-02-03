# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.privilege import v1_detect_params
from ...types.privilege.v1_detect_response import V1DetectResponse

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
        categories: List[Literal["attorney_client", "work_product", "common_interest", "litigation_hold"]]
        | Omit = omit,
        content: str | Omit = omit,
        document_id: str | Omit = omit,
        include_rationale: bool | Omit = omit,
        jurisdiction: Literal["US-Federal"] | Omit = omit,
        model: str | Omit = omit,
        vault_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1DetectResponse:
        """Analyzes text or vault documents for legal privilege.

        Detects attorney-client
        privilege, work product doctrine, common interest privilege, and litigation hold
        materials.

        Returns structured privilege flags with confidence scores and policy-friendly
        rationale suitable for discovery workflows and privilege logs.

        **Size Limit:** Maximum 200,000 characters (larger documents rejected).

        **Permissions:** Requires `chat` permission. When using `document_id`, also
        requires `vault` permission.

        **Note:** When analyzing vault documents, results are automatically stored in
        the document's `privilege_analysis` metadata field.

        Args:
          categories: Privilege categories to check. Defaults to all: attorney_client, work_product,
              common_interest, litigation_hold

          content: Text content to analyze (required if document_id not provided)

          document_id: Vault object ID to analyze (required if content not provided)

          include_rationale: Include detailed rationale for each category

          jurisdiction: Jurisdiction for privilege rules

          model: LLM model to use for analysis

          vault_id: Vault ID (required when using document_id)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/privilege/v1/detect",
            body=maybe_transform(
                {
                    "categories": categories,
                    "content": content,
                    "document_id": document_id,
                    "include_rationale": include_rationale,
                    "jurisdiction": jurisdiction,
                    "model": model,
                    "vault_id": vault_id,
                },
                v1_detect_params.V1DetectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1DetectResponse,
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
        categories: List[Literal["attorney_client", "work_product", "common_interest", "litigation_hold"]]
        | Omit = omit,
        content: str | Omit = omit,
        document_id: str | Omit = omit,
        include_rationale: bool | Omit = omit,
        jurisdiction: Literal["US-Federal"] | Omit = omit,
        model: str | Omit = omit,
        vault_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1DetectResponse:
        """Analyzes text or vault documents for legal privilege.

        Detects attorney-client
        privilege, work product doctrine, common interest privilege, and litigation hold
        materials.

        Returns structured privilege flags with confidence scores and policy-friendly
        rationale suitable for discovery workflows and privilege logs.

        **Size Limit:** Maximum 200,000 characters (larger documents rejected).

        **Permissions:** Requires `chat` permission. When using `document_id`, also
        requires `vault` permission.

        **Note:** When analyzing vault documents, results are automatically stored in
        the document's `privilege_analysis` metadata field.

        Args:
          categories: Privilege categories to check. Defaults to all: attorney_client, work_product,
              common_interest, litigation_hold

          content: Text content to analyze (required if document_id not provided)

          document_id: Vault object ID to analyze (required if content not provided)

          include_rationale: Include detailed rationale for each category

          jurisdiction: Jurisdiction for privilege rules

          model: LLM model to use for analysis

          vault_id: Vault ID (required when using document_id)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/privilege/v1/detect",
            body=await async_maybe_transform(
                {
                    "categories": categories,
                    "content": content,
                    "document_id": document_id,
                    "include_rationale": include_rationale,
                    "jurisdiction": jurisdiction,
                    "model": model,
                    "vault_id": vault_id,
                },
                v1_detect_params.V1DetectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1DetectResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.detect = to_raw_response_wrapper(
            v1.detect,
        )


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.detect = async_to_raw_response_wrapper(
            v1.detect,
        )


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.detect = to_streamed_response_wrapper(
            v1.detect,
        )


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.detect = async_to_streamed_response_wrapper(
            v1.detect,
        )
