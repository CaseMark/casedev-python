# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.connectors.v1.installations import vault_grant_params

__all__ = ["VaultsResource", "AsyncVaultsResource"]


class VaultsResource(SyncAPIResource):
    """Import and export between provider folders (Google Drive) and vaults"""

    @cached_property
    def with_raw_response(self) -> VaultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return VaultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VaultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return VaultsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List the vaults an installation may use, with capabilities and revocation state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/connectors/v1/installations/{id}/vaults", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def grant(
        self,
        vault_id: str,
        *,
        id: str,
        can_manage: bool | Omit = omit,
        can_read: bool | Omit = omit,
        can_write: bool | Omit = omit,
        relationship: Literal["owned", "shared"] | Omit = omit,
        source: Literal["provisioning", "lazy_reconcile", "explicit_share"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Grant (or update) an installation's access to a vault.

        Re-granting a revoked
        vault reactivates it. Import links need can_write; export links need can_read;
        mirror deletion and purge need can_manage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not vault_id:
            raise ValueError(f"Expected a non-empty value for `vault_id` but received {vault_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template("/connectors/v1/installations/{id}/vaults/{vault_id}", id=id, vault_id=vault_id),
            body=maybe_transform(
                {
                    "can_manage": can_manage,
                    "can_read": can_read,
                    "can_write": can_write,
                    "relationship": relationship,
                    "source": source,
                },
                vault_grant_params.VaultGrantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def revoke(
        self,
        vault_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revoke an installation's access to a vault.

        Links using the vault pause at their
        next run; nothing is deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not vault_id:
            raise ValueError(f"Expected a non-empty value for `vault_id` but received {vault_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/connectors/v1/installations/{id}/vaults/{vault_id}", id=id, vault_id=vault_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncVaultsResource(AsyncAPIResource):
    """Import and export between provider folders (Google Drive) and vaults"""

    @cached_property
    def with_raw_response(self) -> AsyncVaultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CaseMark/casedev-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVaultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVaultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CaseMark/casedev-python#with_streaming_response
        """
        return AsyncVaultsResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        List the vaults an installation may use, with capabilities and revocation state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/connectors/v1/installations/{id}/vaults", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def grant(
        self,
        vault_id: str,
        *,
        id: str,
        can_manage: bool | Omit = omit,
        can_read: bool | Omit = omit,
        can_write: bool | Omit = omit,
        relationship: Literal["owned", "shared"] | Omit = omit,
        source: Literal["provisioning", "lazy_reconcile", "explicit_share"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Grant (or update) an installation's access to a vault.

        Re-granting a revoked
        vault reactivates it. Import links need can_write; export links need can_read;
        mirror deletion and purge need can_manage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not vault_id:
            raise ValueError(f"Expected a non-empty value for `vault_id` but received {vault_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template("/connectors/v1/installations/{id}/vaults/{vault_id}", id=id, vault_id=vault_id),
            body=await async_maybe_transform(
                {
                    "can_manage": can_manage,
                    "can_read": can_read,
                    "can_write": can_write,
                    "relationship": relationship,
                    "source": source,
                },
                vault_grant_params.VaultGrantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def revoke(
        self,
        vault_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revoke an installation's access to a vault.

        Links using the vault pause at their
        next run; nothing is deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not vault_id:
            raise ValueError(f"Expected a non-empty value for `vault_id` but received {vault_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/connectors/v1/installations/{id}/vaults/{vault_id}", id=id, vault_id=vault_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class VaultsResourceWithRawResponse:
    def __init__(self, vaults: VaultsResource) -> None:
        self._vaults = vaults

        self.list = to_raw_response_wrapper(
            vaults.list,
        )
        self.grant = to_raw_response_wrapper(
            vaults.grant,
        )
        self.revoke = to_raw_response_wrapper(
            vaults.revoke,
        )


class AsyncVaultsResourceWithRawResponse:
    def __init__(self, vaults: AsyncVaultsResource) -> None:
        self._vaults = vaults

        self.list = async_to_raw_response_wrapper(
            vaults.list,
        )
        self.grant = async_to_raw_response_wrapper(
            vaults.grant,
        )
        self.revoke = async_to_raw_response_wrapper(
            vaults.revoke,
        )


class VaultsResourceWithStreamingResponse:
    def __init__(self, vaults: VaultsResource) -> None:
        self._vaults = vaults

        self.list = to_streamed_response_wrapper(
            vaults.list,
        )
        self.grant = to_streamed_response_wrapper(
            vaults.grant,
        )
        self.revoke = to_streamed_response_wrapper(
            vaults.revoke,
        )


class AsyncVaultsResourceWithStreamingResponse:
    def __init__(self, vaults: AsyncVaultsResource) -> None:
        self._vaults = vaults

        self.list = async_to_streamed_response_wrapper(
            vaults.list,
        )
        self.grant = async_to_streamed_response_wrapper(
            vaults.grant,
        )
        self.revoke = async_to_streamed_response_wrapper(
            vaults.revoke,
        )
