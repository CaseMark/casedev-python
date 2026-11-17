# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["TranscriptionCreateParams"]


class TranscriptionCreateParams(TypedDict, total=False):
    audio_url: str
    """URL of the audio file to transcribe (legacy mode, no auto-storage)"""

    auto_highlights: bool
    """Automatically extract key phrases and topics"""

    boost_param: Literal["low", "default", "high"]
    """
    Deprecated and ignored: current AssemblyAI models do not support boost strength.
    """

    content_safety: bool
    """Enable content moderation and safety labeling"""

    disfluencies: bool
    """Preserve filler words such as um and uh in English transcription"""

    format: Literal["json", "text"]
    """Output format for the transcript when using vault mode"""

    format_text: bool
    """Format text with proper capitalization"""

    keyterms_prompt: SequenceNotStr[str]
    """
    Domain-specific words or phrases (max 6 words each) to improve recognition
    accuracy. Up to 1000 on universal-3-5-pro, 200 on universal-2.
    """

    language_code: str
    """Language code (e.g., 'en_us', 'es', 'fr').

    If not specified, language will be auto-detected
    """

    language_detection: bool
    """Enable automatic language detection"""

    object_id: str
    """Object ID of the audio file in the vault (use with vault_id)"""

    punctuate: bool
    """Add punctuation to the transcript"""

    speaker_labels: bool
    """Enable speaker identification and labeling"""

    speakers_expected: int
    """Expected number of speakers (improves accuracy when known)"""

    speech_models: SequenceNotStr[str]
    """Priority-ordered speech models to use"""

    vault_id: str
    """Vault ID containing the audio file (use with object_id)"""

    word_boost: SequenceNotStr[str]
    """Legacy alias for `keyterms_prompt`.

    Entries are merged into `keyterms_prompt` before submission.
    """
