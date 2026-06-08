# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SkillExportParams"]


class SkillExportParams(TypedDict, total=False):
    target: str
    """Agent runtime skill directory convention to export for.

    Most callers should omit this and pass skillSlugs when creating a runtime.
    """
