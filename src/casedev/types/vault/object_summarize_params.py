# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ObjectSummarizeParams"]


class ObjectSummarizeParams(TypedDict, total=False):
    id: Required[str]

    output_format: Annotated[Literal["PDF", "WORD"], PropertyInfo(alias="outputFormat")]
    """Output format for the summary document"""

    workflow_type: Annotated[str, PropertyInfo(alias="workflowType")]
    """Type of CaseMark workflow to run"""
