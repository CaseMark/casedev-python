# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .holds import (
    HoldsResource,
    AsyncHoldsResource,
    HoldsResourceWithRawResponse,
    AsyncHoldsResourceWithRawResponse,
    HoldsResourceWithStreamingResponse,
    AsyncHoldsResourceWithStreamingResponse,
)
from .ledger import (
    LedgerResource,
    AsyncLedgerResource,
    LedgerResourceWithRawResponse,
    AsyncLedgerResourceWithRawResponse,
    LedgerResourceWithStreamingResponse,
    AsyncLedgerResourceWithStreamingResponse,
)
from .charges import (
    ChargesResource,
    AsyncChargesResource,
    ChargesResourceWithRawResponse,
    AsyncChargesResourceWithRawResponse,
    ChargesResourceWithStreamingResponse,
    AsyncChargesResourceWithStreamingResponse,
)
from .parties import (
    PartiesResource,
    AsyncPartiesResource,
    PartiesResourceWithRawResponse,
    AsyncPartiesResourceWithRawResponse,
    PartiesResourceWithStreamingResponse,
    AsyncPartiesResourceWithStreamingResponse,
)
from .payouts import (
    PayoutsResource,
    AsyncPayoutsResource,
    PayoutsResourceWithRawResponse,
    AsyncPayoutsResourceWithRawResponse,
    PayoutsResourceWithStreamingResponse,
    AsyncPayoutsResourceWithStreamingResponse,
)
from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from .transfers import (
    TransfersResource,
    AsyncTransfersResource,
    TransfersResourceWithRawResponse,
    AsyncTransfersResourceWithRawResponse,
    TransfersResourceWithStreamingResponse,
    AsyncTransfersResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def charges(self) -> ChargesResource:
        return ChargesResource(self._client)

    @cached_property
    def holds(self) -> HoldsResource:
        return HoldsResource(self._client)

    @cached_property
    def ledger(self) -> LedgerResource:
        return LedgerResource(self._client)

    @cached_property
    def parties(self) -> PartiesResource:
        return PartiesResource(self._client)

    @cached_property
    def payouts(self) -> PayoutsResource:
        return PayoutsResource(self._client)

    @cached_property
    def transfers(self) -> TransfersResource:
        return TransfersResource(self._client)

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
    def accounts(self) -> AsyncAccountsResource:
        return AsyncAccountsResource(self._client)

    @cached_property
    def charges(self) -> AsyncChargesResource:
        return AsyncChargesResource(self._client)

    @cached_property
    def holds(self) -> AsyncHoldsResource:
        return AsyncHoldsResource(self._client)

    @cached_property
    def ledger(self) -> AsyncLedgerResource:
        return AsyncLedgerResource(self._client)

    @cached_property
    def parties(self) -> AsyncPartiesResource:
        return AsyncPartiesResource(self._client)

    @cached_property
    def payouts(self) -> AsyncPayoutsResource:
        return AsyncPayoutsResource(self._client)

    @cached_property
    def transfers(self) -> AsyncTransfersResource:
        return AsyncTransfersResource(self._client)

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
    def accounts(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def charges(self) -> ChargesResourceWithRawResponse:
        return ChargesResourceWithRawResponse(self._v1.charges)

    @cached_property
    def holds(self) -> HoldsResourceWithRawResponse:
        return HoldsResourceWithRawResponse(self._v1.holds)

    @cached_property
    def ledger(self) -> LedgerResourceWithRawResponse:
        return LedgerResourceWithRawResponse(self._v1.ledger)

    @cached_property
    def parties(self) -> PartiesResourceWithRawResponse:
        return PartiesResourceWithRawResponse(self._v1.parties)

    @cached_property
    def payouts(self) -> PayoutsResourceWithRawResponse:
        return PayoutsResourceWithRawResponse(self._v1.payouts)

    @cached_property
    def transfers(self) -> TransfersResourceWithRawResponse:
        return TransfersResourceWithRawResponse(self._v1.transfers)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def charges(self) -> AsyncChargesResourceWithRawResponse:
        return AsyncChargesResourceWithRawResponse(self._v1.charges)

    @cached_property
    def holds(self) -> AsyncHoldsResourceWithRawResponse:
        return AsyncHoldsResourceWithRawResponse(self._v1.holds)

    @cached_property
    def ledger(self) -> AsyncLedgerResourceWithRawResponse:
        return AsyncLedgerResourceWithRawResponse(self._v1.ledger)

    @cached_property
    def parties(self) -> AsyncPartiesResourceWithRawResponse:
        return AsyncPartiesResourceWithRawResponse(self._v1.parties)

    @cached_property
    def payouts(self) -> AsyncPayoutsResourceWithRawResponse:
        return AsyncPayoutsResourceWithRawResponse(self._v1.payouts)

    @cached_property
    def transfers(self) -> AsyncTransfersResourceWithRawResponse:
        return AsyncTransfersResourceWithRawResponse(self._v1.transfers)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def charges(self) -> ChargesResourceWithStreamingResponse:
        return ChargesResourceWithStreamingResponse(self._v1.charges)

    @cached_property
    def holds(self) -> HoldsResourceWithStreamingResponse:
        return HoldsResourceWithStreamingResponse(self._v1.holds)

    @cached_property
    def ledger(self) -> LedgerResourceWithStreamingResponse:
        return LedgerResourceWithStreamingResponse(self._v1.ledger)

    @cached_property
    def parties(self) -> PartiesResourceWithStreamingResponse:
        return PartiesResourceWithStreamingResponse(self._v1.parties)

    @cached_property
    def payouts(self) -> PayoutsResourceWithStreamingResponse:
        return PayoutsResourceWithStreamingResponse(self._v1.payouts)

    @cached_property
    def transfers(self) -> TransfersResourceWithStreamingResponse:
        return TransfersResourceWithStreamingResponse(self._v1.transfers)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def charges(self) -> AsyncChargesResourceWithStreamingResponse:
        return AsyncChargesResourceWithStreamingResponse(self._v1.charges)

    @cached_property
    def holds(self) -> AsyncHoldsResourceWithStreamingResponse:
        return AsyncHoldsResourceWithStreamingResponse(self._v1.holds)

    @cached_property
    def ledger(self) -> AsyncLedgerResourceWithStreamingResponse:
        return AsyncLedgerResourceWithStreamingResponse(self._v1.ledger)

    @cached_property
    def parties(self) -> AsyncPartiesResourceWithStreamingResponse:
        return AsyncPartiesResourceWithStreamingResponse(self._v1.parties)

    @cached_property
    def payouts(self) -> AsyncPayoutsResourceWithStreamingResponse:
        return AsyncPayoutsResourceWithStreamingResponse(self._v1.payouts)

    @cached_property
    def transfers(self) -> AsyncTransfersResourceWithStreamingResponse:
        return AsyncTransfersResourceWithStreamingResponse(self._v1.transfers)
