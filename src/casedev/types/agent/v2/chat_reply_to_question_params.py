# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ChatReplyToQuestionParams"]


class ChatReplyToQuestionParams(TypedDict, total=False):
    id: Required[str]

    answers: Required[Iterable[SequenceNotStr[str]]]
    """Answer selections for each prompt element in the pending question"""
