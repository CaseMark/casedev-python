"""
Root-level pytest conftest that optionally removes "Prism tests are disabled"
skip markers when RUN_PRISM_TESTS=true is set.

Used by the SDK staging validation CI workflow to enable the full
Stainless-generated API test suite against the Prism mock server.

This file lives at the project root (outside tests/) and won't be
overwritten by Stainless SDK regeneration.
"""

from __future__ import annotations

import os


def pytest_collection_modifyitems(items: list) -> None:
    if os.environ.get("RUN_PRISM_TESTS", "").lower() != "true":
        return

    for item in items:
        # Remove skip markers whose reason is "Prism tests are disabled"
        markers_to_keep = []
        for marker in item.iter_markers("skip"):
            reason = marker.kwargs.get("reason", "") or (marker.args[0] if marker.args else "")
            if reason == "Prism tests are disabled":
                continue  # drop this skip marker
            markers_to_keep.append(marker)

        # Rebuild the item's markers without the Prism skip markers
        skip_markers = list(item.iter_markers("skip"))
        if len(skip_markers) != len(markers_to_keep):
            # There was at least one Prism skip marker removed
            item.own_markers = [m for m in item.own_markers if m.name != "skip" or m in markers_to_keep]
