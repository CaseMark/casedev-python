# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from casedev import Casedev, AsyncCasedev
from tests.utils import assert_matches_type
from casedev._utils import parse_date
from casedev.types.legal import (
    V1FindResponse,
    V1VerifyResponse,
    V1SimilarResponse,
    V1ResearchResponse,
    V1GetFullTextResponse,
    V1GetCitationsResponse,
    V1PatentSearchResponse,
    V1ListJurisdictionsResponse,
    V1GetCitationsFromURLResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find(self, client: Casedev) -> None:
        v1 = client.legal.v1.find(
            query="xxx",
        )
        assert_matches_type(V1FindResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_with_all_params(self, client: Casedev) -> None:
        v1 = client.legal.v1.find(
            query="xxx",
            jurisdiction="jurisdiction",
            num_results=1,
        )
        assert_matches_type(V1FindResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find(self, client: Casedev) -> None:
        response = client.legal.v1.with_raw_response.find(
            query="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1FindResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find(self, client: Casedev) -> None:
        with client.legal.v1.with_streaming_response.find(
            query="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1FindResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_citations(self, client: Casedev) -> None:
        v1 = client.legal.v1.get_citations(
            text="text",
        )
        assert_matches_type(V1GetCitationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_citations(self, client: Casedev) -> None:
        response = client.legal.v1.with_raw_response.get_citations(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetCitationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_citations(self, client: Casedev) -> None:
        with client.legal.v1.with_streaming_response.get_citations(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetCitationsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_citations_from_url(self, client: Casedev) -> None:
        v1 = client.legal.v1.get_citations_from_url(
            url="https://example.com",
        )
        assert_matches_type(V1GetCitationsFromURLResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_citations_from_url(self, client: Casedev) -> None:
        response = client.legal.v1.with_raw_response.get_citations_from_url(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetCitationsFromURLResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_citations_from_url(self, client: Casedev) -> None:
        with client.legal.v1.with_streaming_response.get_citations_from_url(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetCitationsFromURLResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_full_text(self, client: Casedev) -> None:
        v1 = client.legal.v1.get_full_text(
            url="https://example.com",
        )
        assert_matches_type(V1GetFullTextResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_full_text_with_all_params(self, client: Casedev) -> None:
        v1 = client.legal.v1.get_full_text(
            url="https://example.com",
            highlight_query="highlightQuery",
            max_characters=1000,
            summary_query="summaryQuery",
        )
        assert_matches_type(V1GetFullTextResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_full_text(self, client: Casedev) -> None:
        response = client.legal.v1.with_raw_response.get_full_text(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetFullTextResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_full_text(self, client: Casedev) -> None:
        with client.legal.v1.with_streaming_response.get_full_text(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetFullTextResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_jurisdictions(self, client: Casedev) -> None:
        v1 = client.legal.v1.list_jurisdictions(
            name="xx",
        )
        assert_matches_type(V1ListJurisdictionsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_jurisdictions(self, client: Casedev) -> None:
        response = client.legal.v1.with_raw_response.list_jurisdictions(
            name="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListJurisdictionsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_jurisdictions(self, client: Casedev) -> None:
        with client.legal.v1.with_streaming_response.list_jurisdictions(
            name="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListJurisdictionsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patent_search(self, client: Casedev) -> None:
        v1 = client.legal.v1.patent_search(
            query="x",
        )
        assert_matches_type(V1PatentSearchResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patent_search_with_all_params(self, client: Casedev) -> None:
        v1 = client.legal.v1.patent_search(
            query="x",
            application_status="applicationStatus",
            application_type="Utility",
            assignee="assignee",
            filing_date_from=parse_date("2019-12-27"),
            filing_date_to=parse_date("2019-12-27"),
            grant_date_from=parse_date("2019-12-27"),
            grant_date_to=parse_date("2019-12-27"),
            inventor="inventor",
            limit=1,
            offset=0,
            sort_by="filingDate",
            sort_order="asc",
        )
        assert_matches_type(V1PatentSearchResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_patent_search(self, client: Casedev) -> None:
        response = client.legal.v1.with_raw_response.patent_search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1PatentSearchResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_patent_search(self, client: Casedev) -> None:
        with client.legal.v1.with_streaming_response.patent_search(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1PatentSearchResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_research(self, client: Casedev) -> None:
        v1 = client.legal.v1.research(
            query="xxx",
        )
        assert_matches_type(V1ResearchResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_research_with_all_params(self, client: Casedev) -> None:
        v1 = client.legal.v1.research(
            query="xxx",
            additional_queries=["string"],
            jurisdiction="jurisdiction",
            num_results=1,
        )
        assert_matches_type(V1ResearchResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_research(self, client: Casedev) -> None:
        response = client.legal.v1.with_raw_response.research(
            query="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ResearchResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_research(self, client: Casedev) -> None:
        with client.legal.v1.with_streaming_response.research(
            query="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ResearchResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_similar(self, client: Casedev) -> None:
        v1 = client.legal.v1.similar(
            url="https://example.com",
        )
        assert_matches_type(V1SimilarResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_similar_with_all_params(self, client: Casedev) -> None:
        v1 = client.legal.v1.similar(
            url="https://example.com",
            jurisdiction="jurisdiction",
            num_results=1,
            start_published_date=parse_date("2019-12-27"),
        )
        assert_matches_type(V1SimilarResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_similar(self, client: Casedev) -> None:
        response = client.legal.v1.with_raw_response.similar(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1SimilarResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_similar(self, client: Casedev) -> None:
        with client.legal.v1.with_streaming_response.similar(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1SimilarResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify(self, client: Casedev) -> None:
        v1 = client.legal.v1.verify(
            text="text",
        )
        assert_matches_type(V1VerifyResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: Casedev) -> None:
        response = client.legal.v1.with_raw_response.verify(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1VerifyResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: Casedev) -> None:
        with client.legal.v1.with_streaming_response.verify(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1VerifyResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.find(
            query="xxx",
        )
        assert_matches_type(V1FindResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.find(
            query="xxx",
            jurisdiction="jurisdiction",
            num_results=1,
        )
        assert_matches_type(V1FindResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find(self, async_client: AsyncCasedev) -> None:
        response = await async_client.legal.v1.with_raw_response.find(
            query="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1FindResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find(self, async_client: AsyncCasedev) -> None:
        async with async_client.legal.v1.with_streaming_response.find(
            query="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1FindResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_citations(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.get_citations(
            text="text",
        )
        assert_matches_type(V1GetCitationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_citations(self, async_client: AsyncCasedev) -> None:
        response = await async_client.legal.v1.with_raw_response.get_citations(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetCitationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_citations(self, async_client: AsyncCasedev) -> None:
        async with async_client.legal.v1.with_streaming_response.get_citations(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetCitationsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_citations_from_url(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.get_citations_from_url(
            url="https://example.com",
        )
        assert_matches_type(V1GetCitationsFromURLResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_citations_from_url(self, async_client: AsyncCasedev) -> None:
        response = await async_client.legal.v1.with_raw_response.get_citations_from_url(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetCitationsFromURLResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_citations_from_url(self, async_client: AsyncCasedev) -> None:
        async with async_client.legal.v1.with_streaming_response.get_citations_from_url(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetCitationsFromURLResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_full_text(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.get_full_text(
            url="https://example.com",
        )
        assert_matches_type(V1GetFullTextResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_full_text_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.get_full_text(
            url="https://example.com",
            highlight_query="highlightQuery",
            max_characters=1000,
            summary_query="summaryQuery",
        )
        assert_matches_type(V1GetFullTextResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_full_text(self, async_client: AsyncCasedev) -> None:
        response = await async_client.legal.v1.with_raw_response.get_full_text(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetFullTextResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_full_text(self, async_client: AsyncCasedev) -> None:
        async with async_client.legal.v1.with_streaming_response.get_full_text(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetFullTextResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_jurisdictions(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.list_jurisdictions(
            name="xx",
        )
        assert_matches_type(V1ListJurisdictionsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_jurisdictions(self, async_client: AsyncCasedev) -> None:
        response = await async_client.legal.v1.with_raw_response.list_jurisdictions(
            name="xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListJurisdictionsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_jurisdictions(self, async_client: AsyncCasedev) -> None:
        async with async_client.legal.v1.with_streaming_response.list_jurisdictions(
            name="xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListJurisdictionsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patent_search(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.patent_search(
            query="x",
        )
        assert_matches_type(V1PatentSearchResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patent_search_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.patent_search(
            query="x",
            application_status="applicationStatus",
            application_type="Utility",
            assignee="assignee",
            filing_date_from=parse_date("2019-12-27"),
            filing_date_to=parse_date("2019-12-27"),
            grant_date_from=parse_date("2019-12-27"),
            grant_date_to=parse_date("2019-12-27"),
            inventor="inventor",
            limit=1,
            offset=0,
            sort_by="filingDate",
            sort_order="asc",
        )
        assert_matches_type(V1PatentSearchResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_patent_search(self, async_client: AsyncCasedev) -> None:
        response = await async_client.legal.v1.with_raw_response.patent_search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1PatentSearchResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_patent_search(self, async_client: AsyncCasedev) -> None:
        async with async_client.legal.v1.with_streaming_response.patent_search(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1PatentSearchResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_research(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.research(
            query="xxx",
        )
        assert_matches_type(V1ResearchResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_research_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.research(
            query="xxx",
            additional_queries=["string"],
            jurisdiction="jurisdiction",
            num_results=1,
        )
        assert_matches_type(V1ResearchResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_research(self, async_client: AsyncCasedev) -> None:
        response = await async_client.legal.v1.with_raw_response.research(
            query="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ResearchResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_research(self, async_client: AsyncCasedev) -> None:
        async with async_client.legal.v1.with_streaming_response.research(
            query="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ResearchResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_similar(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.similar(
            url="https://example.com",
        )
        assert_matches_type(V1SimilarResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_similar_with_all_params(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.similar(
            url="https://example.com",
            jurisdiction="jurisdiction",
            num_results=1,
            start_published_date=parse_date("2019-12-27"),
        )
        assert_matches_type(V1SimilarResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_similar(self, async_client: AsyncCasedev) -> None:
        response = await async_client.legal.v1.with_raw_response.similar(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1SimilarResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_similar(self, async_client: AsyncCasedev) -> None:
        async with async_client.legal.v1.with_streaming_response.similar(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1SimilarResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncCasedev) -> None:
        v1 = await async_client.legal.v1.verify(
            text="text",
        )
        assert_matches_type(V1VerifyResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncCasedev) -> None:
        response = await async_client.legal.v1.with_raw_response.verify(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1VerifyResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncCasedev) -> None:
        async with async_client.legal.v1.with_streaming_response.verify(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1VerifyResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
