# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
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
from ...types.legal import (
    v1_find_params,
    v1_verify_params,
    v1_similar_params,
    v1_research_params,
    v1_get_citations_params,
    v1_get_full_text_params,
    v1_patent_search_params,
    v1_list_jurisdictions_params,
    v1_get_citations_from_url_params,
)
from ..._base_client import make_request_options
from ...types.legal.v1_find_response import V1FindResponse
from ...types.legal.v1_verify_response import V1VerifyResponse
from ...types.legal.v1_similar_response import V1SimilarResponse
from ...types.legal.v1_research_response import V1ResearchResponse
from ...types.legal.v1_get_citations_response import V1GetCitationsResponse
from ...types.legal.v1_get_full_text_response import V1GetFullTextResponse
from ...types.legal.v1_patent_search_response import V1PatentSearchResponse
from ...types.legal.v1_list_jurisdictions_response import V1ListJurisdictionsResponse
from ...types.legal.v1_get_citations_from_url_response import V1GetCitationsFromURLResponse

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

    def find(
        self,
        *,
        query: str,
        jurisdiction: str | Omit = omit,
        num_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1FindResponse:
        """
        Search for legal sources including cases, statutes, and regulations from
        authoritative legal databases. Returns ranked candidates. Always verify with
        legal.verify() before citing.

        Args:
          query: Search query (e.g., "fair use copyright", "Miranda rights")

          jurisdiction: Optional jurisdiction ID from resolveJurisdiction (e.g., "california",
              "us-federal")

          num_results: Number of results 1-25 (default: 10)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legal/v1/find",
            body=maybe_transform(
                {
                    "query": query,
                    "jurisdiction": jurisdiction,
                    "num_results": num_results,
                },
                v1_find_params.V1FindParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1FindResponse,
        )

    def get_citations(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetCitationsResponse:
        """
        Parses legal citations from text and returns structured Bluebook components
        (case name, reporter, volume, page, year, court). Accepts either a single
        citation or a full text block.

        Args:
          text: Text containing citations to extract. Can be a single citation (e.g., "531 U.S.
              98") or a full document with multiple citations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legal/v1/citations",
            body=maybe_transform({"text": text}, v1_get_citations_params.V1GetCitationsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetCitationsResponse,
        )

    def get_citations_from_url(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetCitationsFromURLResponse:
        """Extract all legal citations and references from a document URL.

        Returns
        structured citation data including case citations, statute references, and
        regulatory citations.

        Args:
          url: URL of the legal document to extract citations from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legal/v1/citations-from-url",
            body=maybe_transform({"url": url}, v1_get_citations_from_url_params.V1GetCitationsFromURLParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetCitationsFromURLResponse,
        )

    def get_full_text(
        self,
        *,
        url: str,
        highlight_query: str | Omit = omit,
        max_characters: int | Omit = omit,
        summary_query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetFullTextResponse:
        """Retrieve the full text content of a legal document.

        Use after verifying the
        source with legal.verify(). Returns complete text with optional highlights and
        AI summary.

        Args:
          url: URL of the verified legal document

          highlight_query: Optional query to extract relevant highlights (e.g., "What is the holding?")

          max_characters: Maximum characters to return (default: 10000, max: 50000)

          summary_query: Optional query for generating a summary (e.g., "Summarize the key ruling")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legal/v1/full-text",
            body=maybe_transform(
                {
                    "url": url,
                    "highlight_query": highlight_query,
                    "max_characters": max_characters,
                    "summary_query": summary_query,
                },
                v1_get_full_text_params.V1GetFullTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetFullTextResponse,
        )

    def list_jurisdictions(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ListJurisdictionsResponse:
        """Search for a jurisdiction by name.

        Returns matching jurisdictions with their IDs
        for use in legal.find() and other legal research endpoints.

        Args:
          name: Jurisdiction name (e.g., "California", "US Federal", "NY")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legal/v1/jurisdictions",
            body=maybe_transform({"name": name}, v1_list_jurisdictions_params.V1ListJurisdictionsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListJurisdictionsResponse,
        )

    def patent_search(
        self,
        *,
        query: str,
        application_status: str | Omit = omit,
        application_type: Literal["Utility", "Design", "Plant", "Provisional", "Reissue"] | Omit = omit,
        assignee: str | Omit = omit,
        filing_date_from: Union[str, date] | Omit = omit,
        filing_date_to: Union[str, date] | Omit = omit,
        grant_date_from: Union[str, date] | Omit = omit,
        grant_date_to: Union[str, date] | Omit = omit,
        inventor: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: Literal["filingDate", "grantDate"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1PatentSearchResponse:
        """Search the USPTO Open Data Portal for US patent applications and granted
        patents.

        Supports free-text queries, field-specific search, filters by
        assignee/inventor/status/type, date ranges, and pagination. Covers applications
        filed on or after January 1, 2001. Data is refreshed daily.

        Args:
          query: Free-text search across all patent fields, or field-specific query (e.g.
              "applicationMetaData.patentNumber:11234567"). Supports AND, OR, NOT operators.

          application_status: Filter by application status (e.g. "Patented Case", "Abandoned", "Pending")

          application_type: Filter by application type

          assignee: Filter by assignee/owner name (e.g. "Google LLC")

          filing_date_from: Start of filing date range (YYYY-MM-DD)

          filing_date_to: End of filing date range (YYYY-MM-DD)

          grant_date_from: Start of grant date range (YYYY-MM-DD)

          grant_date_to: End of grant date range (YYYY-MM-DD)

          inventor: Filter by inventor name

          limit: Number of results to return (default 25, max 100)

          offset: Starting position for pagination

          sort_by: Field to sort results by

          sort_order: Sort order (default desc, newest first)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legal/v1/patent-search",
            body=maybe_transform(
                {
                    "query": query,
                    "application_status": application_status,
                    "application_type": application_type,
                    "assignee": assignee,
                    "filing_date_from": filing_date_from,
                    "filing_date_to": filing_date_to,
                    "grant_date_from": grant_date_from,
                    "grant_date_to": grant_date_to,
                    "inventor": inventor,
                    "limit": limit,
                    "offset": offset,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                },
                v1_patent_search_params.V1PatentSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1PatentSearchResponse,
        )

    def research(
        self,
        *,
        query: str,
        additional_queries: SequenceNotStr[str] | Omit = omit,
        jurisdiction: str | Omit = omit,
        num_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ResearchResponse:
        """Perform comprehensive legal research with multiple query variations.

        Uses
        advanced deep search to find relevant sources across different phrasings of the
        legal issue.

        Args:
          query: Primary search query

          additional_queries: Additional query variations to search (e.g., different phrasings of the legal
              issue)

          jurisdiction: Optional jurisdiction ID from resolveJurisdiction

          num_results: Number of results 1-25 (default: 10)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legal/v1/research",
            body=maybe_transform(
                {
                    "query": query,
                    "additional_queries": additional_queries,
                    "jurisdiction": jurisdiction,
                    "num_results": num_results,
                },
                v1_research_params.V1ResearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ResearchResponse,
        )

    def similar(
        self,
        *,
        url: str,
        jurisdiction: str | Omit = omit,
        num_results: int | Omit = omit,
        start_published_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1SimilarResponse:
        """Find cases and documents similar to a given legal source.

        Useful for finding
        citing cases, related precedents, or similar statutes.

        Args:
          url: URL of a legal document to find similar sources for

          jurisdiction: Optional jurisdiction ID to filter results

          num_results: Number of results 1-25 (default: 10)

          start_published_date: Optional ISO date to find only newer documents (e.g., "2020-01-01")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legal/v1/similar",
            body=maybe_transform(
                {
                    "url": url,
                    "jurisdiction": jurisdiction,
                    "num_results": num_results,
                    "start_published_date": start_published_date,
                },
                v1_similar_params.V1SimilarParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1SimilarResponse,
        )

    def verify(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1VerifyResponse:
        """
        Validates legal citations against authoritative case law sources (CourtListener
        database of ~10M cases). Returns verification status and case metadata for each
        citation found in the input text. Accepts either a single citation or a full
        text block containing multiple citations.

        Args:
          text: Text containing citations to verify. Can be a single citation (e.g., "531 U.S.
              98") or a full document with multiple citations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legal/v1/verify",
            body=maybe_transform({"text": text}, v1_verify_params.V1VerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1VerifyResponse,
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

    async def find(
        self,
        *,
        query: str,
        jurisdiction: str | Omit = omit,
        num_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1FindResponse:
        """
        Search for legal sources including cases, statutes, and regulations from
        authoritative legal databases. Returns ranked candidates. Always verify with
        legal.verify() before citing.

        Args:
          query: Search query (e.g., "fair use copyright", "Miranda rights")

          jurisdiction: Optional jurisdiction ID from resolveJurisdiction (e.g., "california",
              "us-federal")

          num_results: Number of results 1-25 (default: 10)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legal/v1/find",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "jurisdiction": jurisdiction,
                    "num_results": num_results,
                },
                v1_find_params.V1FindParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1FindResponse,
        )

    async def get_citations(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetCitationsResponse:
        """
        Parses legal citations from text and returns structured Bluebook components
        (case name, reporter, volume, page, year, court). Accepts either a single
        citation or a full text block.

        Args:
          text: Text containing citations to extract. Can be a single citation (e.g., "531 U.S.
              98") or a full document with multiple citations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legal/v1/citations",
            body=await async_maybe_transform({"text": text}, v1_get_citations_params.V1GetCitationsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetCitationsResponse,
        )

    async def get_citations_from_url(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetCitationsFromURLResponse:
        """Extract all legal citations and references from a document URL.

        Returns
        structured citation data including case citations, statute references, and
        regulatory citations.

        Args:
          url: URL of the legal document to extract citations from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legal/v1/citations-from-url",
            body=await async_maybe_transform(
                {"url": url}, v1_get_citations_from_url_params.V1GetCitationsFromURLParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetCitationsFromURLResponse,
        )

    async def get_full_text(
        self,
        *,
        url: str,
        highlight_query: str | Omit = omit,
        max_characters: int | Omit = omit,
        summary_query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetFullTextResponse:
        """Retrieve the full text content of a legal document.

        Use after verifying the
        source with legal.verify(). Returns complete text with optional highlights and
        AI summary.

        Args:
          url: URL of the verified legal document

          highlight_query: Optional query to extract relevant highlights (e.g., "What is the holding?")

          max_characters: Maximum characters to return (default: 10000, max: 50000)

          summary_query: Optional query for generating a summary (e.g., "Summarize the key ruling")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legal/v1/full-text",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "highlight_query": highlight_query,
                    "max_characters": max_characters,
                    "summary_query": summary_query,
                },
                v1_get_full_text_params.V1GetFullTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetFullTextResponse,
        )

    async def list_jurisdictions(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ListJurisdictionsResponse:
        """Search for a jurisdiction by name.

        Returns matching jurisdictions with their IDs
        for use in legal.find() and other legal research endpoints.

        Args:
          name: Jurisdiction name (e.g., "California", "US Federal", "NY")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legal/v1/jurisdictions",
            body=await async_maybe_transform({"name": name}, v1_list_jurisdictions_params.V1ListJurisdictionsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListJurisdictionsResponse,
        )

    async def patent_search(
        self,
        *,
        query: str,
        application_status: str | Omit = omit,
        application_type: Literal["Utility", "Design", "Plant", "Provisional", "Reissue"] | Omit = omit,
        assignee: str | Omit = omit,
        filing_date_from: Union[str, date] | Omit = omit,
        filing_date_to: Union[str, date] | Omit = omit,
        grant_date_from: Union[str, date] | Omit = omit,
        grant_date_to: Union[str, date] | Omit = omit,
        inventor: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: Literal["filingDate", "grantDate"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1PatentSearchResponse:
        """Search the USPTO Open Data Portal for US patent applications and granted
        patents.

        Supports free-text queries, field-specific search, filters by
        assignee/inventor/status/type, date ranges, and pagination. Covers applications
        filed on or after January 1, 2001. Data is refreshed daily.

        Args:
          query: Free-text search across all patent fields, or field-specific query (e.g.
              "applicationMetaData.patentNumber:11234567"). Supports AND, OR, NOT operators.

          application_status: Filter by application status (e.g. "Patented Case", "Abandoned", "Pending")

          application_type: Filter by application type

          assignee: Filter by assignee/owner name (e.g. "Google LLC")

          filing_date_from: Start of filing date range (YYYY-MM-DD)

          filing_date_to: End of filing date range (YYYY-MM-DD)

          grant_date_from: Start of grant date range (YYYY-MM-DD)

          grant_date_to: End of grant date range (YYYY-MM-DD)

          inventor: Filter by inventor name

          limit: Number of results to return (default 25, max 100)

          offset: Starting position for pagination

          sort_by: Field to sort results by

          sort_order: Sort order (default desc, newest first)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legal/v1/patent-search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "application_status": application_status,
                    "application_type": application_type,
                    "assignee": assignee,
                    "filing_date_from": filing_date_from,
                    "filing_date_to": filing_date_to,
                    "grant_date_from": grant_date_from,
                    "grant_date_to": grant_date_to,
                    "inventor": inventor,
                    "limit": limit,
                    "offset": offset,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                },
                v1_patent_search_params.V1PatentSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1PatentSearchResponse,
        )

    async def research(
        self,
        *,
        query: str,
        additional_queries: SequenceNotStr[str] | Omit = omit,
        jurisdiction: str | Omit = omit,
        num_results: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ResearchResponse:
        """Perform comprehensive legal research with multiple query variations.

        Uses
        advanced deep search to find relevant sources across different phrasings of the
        legal issue.

        Args:
          query: Primary search query

          additional_queries: Additional query variations to search (e.g., different phrasings of the legal
              issue)

          jurisdiction: Optional jurisdiction ID from resolveJurisdiction

          num_results: Number of results 1-25 (default: 10)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legal/v1/research",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "additional_queries": additional_queries,
                    "jurisdiction": jurisdiction,
                    "num_results": num_results,
                },
                v1_research_params.V1ResearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ResearchResponse,
        )

    async def similar(
        self,
        *,
        url: str,
        jurisdiction: str | Omit = omit,
        num_results: int | Omit = omit,
        start_published_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1SimilarResponse:
        """Find cases and documents similar to a given legal source.

        Useful for finding
        citing cases, related precedents, or similar statutes.

        Args:
          url: URL of a legal document to find similar sources for

          jurisdiction: Optional jurisdiction ID to filter results

          num_results: Number of results 1-25 (default: 10)

          start_published_date: Optional ISO date to find only newer documents (e.g., "2020-01-01")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legal/v1/similar",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "jurisdiction": jurisdiction,
                    "num_results": num_results,
                    "start_published_date": start_published_date,
                },
                v1_similar_params.V1SimilarParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1SimilarResponse,
        )

    async def verify(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1VerifyResponse:
        """
        Validates legal citations against authoritative case law sources (CourtListener
        database of ~10M cases). Returns verification status and case metadata for each
        citation found in the input text. Accepts either a single citation or a full
        text block containing multiple citations.

        Args:
          text: Text containing citations to verify. Can be a single citation (e.g., "531 U.S.
              98") or a full document with multiple citations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legal/v1/verify",
            body=await async_maybe_transform({"text": text}, v1_verify_params.V1VerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1VerifyResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.find = to_raw_response_wrapper(
            v1.find,
        )
        self.get_citations = to_raw_response_wrapper(
            v1.get_citations,
        )
        self.get_citations_from_url = to_raw_response_wrapper(
            v1.get_citations_from_url,
        )
        self.get_full_text = to_raw_response_wrapper(
            v1.get_full_text,
        )
        self.list_jurisdictions = to_raw_response_wrapper(
            v1.list_jurisdictions,
        )
        self.patent_search = to_raw_response_wrapper(
            v1.patent_search,
        )
        self.research = to_raw_response_wrapper(
            v1.research,
        )
        self.similar = to_raw_response_wrapper(
            v1.similar,
        )
        self.verify = to_raw_response_wrapper(
            v1.verify,
        )


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.find = async_to_raw_response_wrapper(
            v1.find,
        )
        self.get_citations = async_to_raw_response_wrapper(
            v1.get_citations,
        )
        self.get_citations_from_url = async_to_raw_response_wrapper(
            v1.get_citations_from_url,
        )
        self.get_full_text = async_to_raw_response_wrapper(
            v1.get_full_text,
        )
        self.list_jurisdictions = async_to_raw_response_wrapper(
            v1.list_jurisdictions,
        )
        self.patent_search = async_to_raw_response_wrapper(
            v1.patent_search,
        )
        self.research = async_to_raw_response_wrapper(
            v1.research,
        )
        self.similar = async_to_raw_response_wrapper(
            v1.similar,
        )
        self.verify = async_to_raw_response_wrapper(
            v1.verify,
        )


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.find = to_streamed_response_wrapper(
            v1.find,
        )
        self.get_citations = to_streamed_response_wrapper(
            v1.get_citations,
        )
        self.get_citations_from_url = to_streamed_response_wrapper(
            v1.get_citations_from_url,
        )
        self.get_full_text = to_streamed_response_wrapper(
            v1.get_full_text,
        )
        self.list_jurisdictions = to_streamed_response_wrapper(
            v1.list_jurisdictions,
        )
        self.patent_search = to_streamed_response_wrapper(
            v1.patent_search,
        )
        self.research = to_streamed_response_wrapper(
            v1.research,
        )
        self.similar = to_streamed_response_wrapper(
            v1.similar,
        )
        self.verify = to_streamed_response_wrapper(
            v1.verify,
        )


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.find = async_to_streamed_response_wrapper(
            v1.find,
        )
        self.get_citations = async_to_streamed_response_wrapper(
            v1.get_citations,
        )
        self.get_citations_from_url = async_to_streamed_response_wrapper(
            v1.get_citations_from_url,
        )
        self.get_full_text = async_to_streamed_response_wrapper(
            v1.get_full_text,
        )
        self.list_jurisdictions = async_to_streamed_response_wrapper(
            v1.list_jurisdictions,
        )
        self.patent_search = async_to_streamed_response_wrapper(
            v1.patent_search,
        )
        self.research = async_to_streamed_response_wrapper(
            v1.research,
        )
        self.similar = async_to_streamed_response_wrapper(
            v1.similar,
        )
        self.verify = async_to_streamed_response_wrapper(
            v1.verify,
        )
