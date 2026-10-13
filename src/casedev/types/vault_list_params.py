# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VaultListParams"]


class VaultListParams(TypedDict, total=False):
    cursor: str
    """Opaque continuation cursor from `pagination.next_cursor` of the previous page.

    Must be replayed with the same API key scope and `query` that produced it.
    """

    include_totals: bool
    """
    When `true`, adds `totals` covering every vault matching the filters, not just
    this page. Scans all objects in those vaults, so request it once per filter
    change rather than on every page.
    """

    limit: int
    """Vaults per page (1-200).

    Omit to receive every vault. Supplying a cursor without a limit uses 50.
    """

    query: str
    """Case-insensitive substring match on the vault name."""
