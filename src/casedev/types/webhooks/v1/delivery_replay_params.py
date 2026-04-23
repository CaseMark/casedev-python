# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DeliveryReplayParams"]


class DeliveryReplayParams(TypedDict, total=False):
    payload: object
    """Override payload to deliver.

    Must only be supplied when the delivery record lacks enough context to
    reconstruct the original event (rare). Defaults to an empty data envelope.
    """
