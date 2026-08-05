# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["RetrieveCreateResponse"]


class RetrieveCreateResponse(BaseModel):
    object_id: str
    """Requested object ID."""

    status: Literal["completed"]

    text: str
    """Full transcript text."""

    vault_id: str

    audio_duration: Optional[int] = None

    confidence: Optional[int] = None

    filename: Optional[str] = None

    source_object_id: Optional[str] = None
    """Source media object ID when known."""

    transcript_object_id: Optional[str] = None
    """Transcript object ID when known."""

    transcription_job_id: Optional[str] = None
    """Transcription job ID when known."""

    word_count: Optional[int] = None
