# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .links import (
    LinksResource,
    AsyncLinksResource,
    LinksResourceWithRawResponse,
    AsyncLinksResourceWithRawResponse,
    LinksResourceWithStreamingResponse,
    AsyncLinksResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from .connections import (
    ConnectionsResource,
    AsyncConnectionsResource,
    ConnectionsResourceWithRawResponse,
    AsyncConnectionsResourceWithRawResponse,
    ConnectionsResourceWithStreamingResponse,
    AsyncConnectionsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.connectors import v1_fetch_params, v1_transfer_params, v1_sync_link_params
from .applications.applications import (
    ApplicationsResource,
    AsyncApplicationsResource,
    ApplicationsResourceWithRawResponse,
    AsyncApplicationsResourceWithRawResponse,
    ApplicationsResourceWithStreamingResponse,
    AsyncApplicationsResourceWithStreamingResponse,
)
from .installations.installations import (
    InstallationsResource,
    AsyncInstallationsResource,
    InstallationsResourceWithRawResponse,
    AsyncInstallationsResourceWithRawResponse,
    InstallationsResourceWithStreamingResponse,
    AsyncInstallationsResourceWithStreamingResponse,
)
from ....types.connectors.v1_transfer_response import V1TransferResponse
from ....types.connectors.v1_sync_link_response import V1SyncLinkResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    """Import and export between provider folders and vaults"""

    @cached_property
    def applications(self) -> ApplicationsResource:
        return ApplicationsResource(self._client)

    @cached_property
    def installations(self) -> InstallationsResource:
        """Import and export between provider folders and vaults"""
        return InstallationsResource(self._client)

    @cached_property
    def connections(self) -> ConnectionsResource:
        """Import and export between provider folders and vaults"""
        return ConnectionsResource(self._client)

    @cached_property
    def links(self) -> LinksResource:
        """Import and export between provider folders and vaults"""
        return LinksResource(self._client)

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

    def fetch(
        self,
        *,
        open_ref: str,
        upload_url: str | Omit = omit,
        vault_id: str | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Copy one provider file, named by an open_ref from browse, into a Vault
        (vault_id) or to a presigned S3 PUT URL (upload_url). Runs synchronously; files
        over 100 MB return 413 and belong in a transfer. A repeat for an unchanged
        provider version returns the first copy with 200. Vault copies are stored as
        uploaded: call POST /vault/{id}/ingest/{objectId} to index them. Fetched copies
        are never exported by a link.

        Args:
          open_ref: From a browse item, exactly as received

          upload_url: Presigned HTTPS S3 PUT URL. Content-Type must not be a signed header. Exactly
              one destination.

          vault_id: Destination Vault. Exactly one destination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return self._post(
            "/connectors/v1/fetch",
            body=maybe_transform(
                {
                    "open_ref": open_ref,
                    "upload_url": upload_url,
                    "vault_id": vault_id,
                },
                v1_fetch_params.V1FetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def sync_link(
        self,
        *,
        connection_id: str,
        direction: Literal["import", "export", "both"],
        remote: v1_sync_link_params.Remote,
        vault_id: str,
        export_destination: v1_sync_link_params.ExportDestination | Omit = omit,
        matter_id: Optional[str] | Omit = omit,
        policy: v1_sync_link_params.Policy | Omit = omit,
        selection: v1_sync_link_params.Selection | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1SyncLinkResponse:
        """
        Standing promise: backfill now, then stay current (the sync sweeper re-runs
        synced links on a schedule). Direction both creates paired import/export links
        and defaults export to a CaseMark Output subfolder. Same body as /transfer minus
        run_mode. Upserts links by (connection_id, direction, remote, vault_id,
        selection); existing once-links are upgraded in place with their ledger and
        cursor preserved. Downgrade or pause via PATCH /links/{id}.

        Args:
          export_destination: Optional destination for direction both. Defaults to CaseMark Output under
              remote.

          selection: Export only part of the vault (direction export only; 400
              selection_requires_export otherwise). Provide object_ids, folder, or both (their
              intersection). The selection is part of link identity: each distinct selection
              to the same destination is its own link, and repeating a selection re-runs that
              link. Exported objects still exclude files still processing and
              connector-imported or fetched copies. Destination paths: with folder, paths are
              relative to that folder, so its contents land directly in remote; with
              object_ids only, each object keeps its full vault path. Omit to export the whole
              vault.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return self._post(
            "/connectors/v1/sync-link",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "direction": direction,
                    "remote": remote,
                    "vault_id": vault_id,
                    "export_destination": export_destination,
                    "matter_id": matter_id,
                    "policy": policy,
                    "selection": selection,
                },
                v1_sync_link_params.V1SyncLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1SyncLinkResponse,
        )

    def transfer(
        self,
        *,
        connection_id: str,
        direction: Literal["import", "export", "both"],
        remote: v1_transfer_params.Remote,
        vault_id: str,
        export_destination: v1_transfer_params.ExportDestination | Omit = omit,
        matter_id: Optional[str] | Omit = omit,
        policy: v1_transfer_params.Policy | Omit = omit,
        run_mode: Literal["auto", "full_reconcile"] | Omit = omit,
        selection: v1_transfer_params.Selection | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1TransferResponse:
        """
        One-shot import (provider folder → vault), export (vault → provider folder), or
        both. Direction both creates paired import/export links and defaults export to a
        CaseMark Output subfolder. Upserts links by (connection_id, direction, remote,
        vault_id, selection): first call backfills, later calls move only new/changed
        files via the ledger. Poll GET /links/{id} → active_run for progress.

        Args:
          export_destination: Optional destination for direction both. Defaults to CaseMark Output under
              remote.

          selection: Export only part of the vault (direction export only; 400
              selection_requires_export otherwise). Provide object_ids, folder, or both (their
              intersection). The selection is part of link identity: each distinct selection
              to the same destination is its own link, and repeating a selection re-runs that
              link. Exported objects still exclude files still processing and
              connector-imported or fetched copies. Destination paths: with folder, paths are
              relative to that folder, so its contents land directly in remote; with
              object_ids only, each object keeps its full vault path. Omit to export the whole
              vault.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return self._post(
            "/connectors/v1/transfer",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "direction": direction,
                    "remote": remote,
                    "vault_id": vault_id,
                    "export_destination": export_destination,
                    "matter_id": matter_id,
                    "policy": policy,
                    "run_mode": run_mode,
                    "selection": selection,
                },
                v1_transfer_params.V1TransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1TransferResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    """Import and export between provider folders and vaults"""

    @cached_property
    def applications(self) -> AsyncApplicationsResource:
        return AsyncApplicationsResource(self._client)

    @cached_property
    def installations(self) -> AsyncInstallationsResource:
        """Import and export between provider folders and vaults"""
        return AsyncInstallationsResource(self._client)

    @cached_property
    def connections(self) -> AsyncConnectionsResource:
        """Import and export between provider folders and vaults"""
        return AsyncConnectionsResource(self._client)

    @cached_property
    def links(self) -> AsyncLinksResource:
        """Import and export between provider folders and vaults"""
        return AsyncLinksResource(self._client)

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

    async def fetch(
        self,
        *,
        open_ref: str,
        upload_url: str | Omit = omit,
        vault_id: str | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Copy one provider file, named by an open_ref from browse, into a Vault
        (vault_id) or to a presigned S3 PUT URL (upload_url). Runs synchronously; files
        over 100 MB return 413 and belong in a transfer. A repeat for an unchanged
        provider version returns the first copy with 200. Vault copies are stored as
        uploaded: call POST /vault/{id}/ingest/{objectId} to index them. Fetched copies
        are never exported by a link.

        Args:
          open_ref: From a browse item, exactly as received

          upload_url: Presigned HTTPS S3 PUT URL. Content-Type must not be a signed header. Exactly
              one destination.

          vault_id: Destination Vault. Exactly one destination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/connectors/v1/fetch",
            body=await async_maybe_transform(
                {
                    "open_ref": open_ref,
                    "upload_url": upload_url,
                    "vault_id": vault_id,
                },
                v1_fetch_params.V1FetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def sync_link(
        self,
        *,
        connection_id: str,
        direction: Literal["import", "export", "both"],
        remote: v1_sync_link_params.Remote,
        vault_id: str,
        export_destination: v1_sync_link_params.ExportDestination | Omit = omit,
        matter_id: Optional[str] | Omit = omit,
        policy: v1_sync_link_params.Policy | Omit = omit,
        selection: v1_sync_link_params.Selection | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1SyncLinkResponse:
        """
        Standing promise: backfill now, then stay current (the sync sweeper re-runs
        synced links on a schedule). Direction both creates paired import/export links
        and defaults export to a CaseMark Output subfolder. Same body as /transfer minus
        run_mode. Upserts links by (connection_id, direction, remote, vault_id,
        selection); existing once-links are upgraded in place with their ledger and
        cursor preserved. Downgrade or pause via PATCH /links/{id}.

        Args:
          export_destination: Optional destination for direction both. Defaults to CaseMark Output under
              remote.

          selection: Export only part of the vault (direction export only; 400
              selection_requires_export otherwise). Provide object_ids, folder, or both (their
              intersection). The selection is part of link identity: each distinct selection
              to the same destination is its own link, and repeating a selection re-runs that
              link. Exported objects still exclude files still processing and
              connector-imported or fetched copies. Destination paths: with folder, paths are
              relative to that folder, so its contents land directly in remote; with
              object_ids only, each object keeps its full vault path. Omit to export the whole
              vault.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/connectors/v1/sync-link",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "direction": direction,
                    "remote": remote,
                    "vault_id": vault_id,
                    "export_destination": export_destination,
                    "matter_id": matter_id,
                    "policy": policy,
                    "selection": selection,
                },
                v1_sync_link_params.V1SyncLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1SyncLinkResponse,
        )

    async def transfer(
        self,
        *,
        connection_id: str,
        direction: Literal["import", "export", "both"],
        remote: v1_transfer_params.Remote,
        vault_id: str,
        export_destination: v1_transfer_params.ExportDestination | Omit = omit,
        matter_id: Optional[str] | Omit = omit,
        policy: v1_transfer_params.Policy | Omit = omit,
        run_mode: Literal["auto", "full_reconcile"] | Omit = omit,
        selection: v1_transfer_params.Selection | Omit = omit,
        x_case_connector_subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1TransferResponse:
        """
        One-shot import (provider folder → vault), export (vault → provider folder), or
        both. Direction both creates paired import/export links and defaults export to a
        CaseMark Output subfolder. Upserts links by (connection_id, direction, remote,
        vault_id, selection): first call backfills, later calls move only new/changed
        files via the ledger. Poll GET /links/{id} → active_run for progress.

        Args:
          export_destination: Optional destination for direction both. Defaults to CaseMark Output under
              remote.

          selection: Export only part of the vault (direction export only; 400
              selection_requires_export otherwise). Provide object_ids, folder, or both (their
              intersection). The selection is part of link identity: each distinct selection
              to the same destination is its own link, and repeating a selection re-runs that
              link. Exported objects still exclude files still processing and
              connector-imported or fetched copies. Destination paths: with folder, paths are
              relative to that folder, so its contents land directly in remote; with
              object_ids only, each object keeps its full vault path. Omit to export the whole
              vault.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"x-case-connector-subject": x_case_connector_subject}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/connectors/v1/transfer",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "direction": direction,
                    "remote": remote,
                    "vault_id": vault_id,
                    "export_destination": export_destination,
                    "matter_id": matter_id,
                    "policy": policy,
                    "run_mode": run_mode,
                    "selection": selection,
                },
                v1_transfer_params.V1TransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1TransferResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.fetch = to_raw_response_wrapper(
            v1.fetch,
        )
        self.sync_link = to_raw_response_wrapper(
            v1.sync_link,
        )
        self.transfer = to_raw_response_wrapper(
            v1.transfer,
        )

    @cached_property
    def applications(self) -> ApplicationsResourceWithRawResponse:
        return ApplicationsResourceWithRawResponse(self._v1.applications)

    @cached_property
    def installations(self) -> InstallationsResourceWithRawResponse:
        """Import and export between provider folders and vaults"""
        return InstallationsResourceWithRawResponse(self._v1.installations)

    @cached_property
    def connections(self) -> ConnectionsResourceWithRawResponse:
        """Import and export between provider folders and vaults"""
        return ConnectionsResourceWithRawResponse(self._v1.connections)

    @cached_property
    def links(self) -> LinksResourceWithRawResponse:
        """Import and export between provider folders and vaults"""
        return LinksResourceWithRawResponse(self._v1.links)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.fetch = async_to_raw_response_wrapper(
            v1.fetch,
        )
        self.sync_link = async_to_raw_response_wrapper(
            v1.sync_link,
        )
        self.transfer = async_to_raw_response_wrapper(
            v1.transfer,
        )

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithRawResponse:
        return AsyncApplicationsResourceWithRawResponse(self._v1.applications)

    @cached_property
    def installations(self) -> AsyncInstallationsResourceWithRawResponse:
        """Import and export between provider folders and vaults"""
        return AsyncInstallationsResourceWithRawResponse(self._v1.installations)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithRawResponse:
        """Import and export between provider folders and vaults"""
        return AsyncConnectionsResourceWithRawResponse(self._v1.connections)

    @cached_property
    def links(self) -> AsyncLinksResourceWithRawResponse:
        """Import and export between provider folders and vaults"""
        return AsyncLinksResourceWithRawResponse(self._v1.links)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.fetch = to_streamed_response_wrapper(
            v1.fetch,
        )
        self.sync_link = to_streamed_response_wrapper(
            v1.sync_link,
        )
        self.transfer = to_streamed_response_wrapper(
            v1.transfer,
        )

    @cached_property
    def applications(self) -> ApplicationsResourceWithStreamingResponse:
        return ApplicationsResourceWithStreamingResponse(self._v1.applications)

    @cached_property
    def installations(self) -> InstallationsResourceWithStreamingResponse:
        """Import and export between provider folders and vaults"""
        return InstallationsResourceWithStreamingResponse(self._v1.installations)

    @cached_property
    def connections(self) -> ConnectionsResourceWithStreamingResponse:
        """Import and export between provider folders and vaults"""
        return ConnectionsResourceWithStreamingResponse(self._v1.connections)

    @cached_property
    def links(self) -> LinksResourceWithStreamingResponse:
        """Import and export between provider folders and vaults"""
        return LinksResourceWithStreamingResponse(self._v1.links)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.fetch = async_to_streamed_response_wrapper(
            v1.fetch,
        )
        self.sync_link = async_to_streamed_response_wrapper(
            v1.sync_link,
        )
        self.transfer = async_to_streamed_response_wrapper(
            v1.transfer,
        )

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithStreamingResponse:
        return AsyncApplicationsResourceWithStreamingResponse(self._v1.applications)

    @cached_property
    def installations(self) -> AsyncInstallationsResourceWithStreamingResponse:
        """Import and export between provider folders and vaults"""
        return AsyncInstallationsResourceWithStreamingResponse(self._v1.installations)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithStreamingResponse:
        """Import and export between provider folders and vaults"""
        return AsyncConnectionsResourceWithStreamingResponse(self._v1.connections)

    @cached_property
    def links(self) -> AsyncLinksResourceWithStreamingResponse:
        """Import and export between provider folders and vaults"""
        return AsyncLinksResourceWithStreamingResponse(self._v1.links)
