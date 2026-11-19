# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "AssemblyCreateParams",
    "Source",
    "Volume",
    "VolumePage",
    "VolumeBates",
    "VolumeContents",
    "VolumeOutline",
    "Bates",
    "Compression",
]


class AssemblyCreateParams(TypedDict, total=False):
    sources: Required[Iterable[Source]]
    """
    Source PDFs, or ingested office files (spreadsheets, CSV/TSV, Word), which are
    assembled from the PDF version ingestion saved for them. Page ranges refer to a
    source by its index in this list.
    """

    volumes: Required[Iterable[Volume]]

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    bates: Bates
    """Bates numbering that continues across every volume without its own series.

    Text must be printable ASCII.
    """

    client_reference: Annotated[str, PropertyInfo(alias="clientReference")]

    compression: Compression
    """Downsamples colour and grayscale scans above maxDpi and re-encodes them.

    Images already stored as 1-bit, JPEG 2000, indexed or CMYK keep their bytes.
    """

    linearize: bool
    """Optimize volumes for web viewing"""

    page_size: Annotated[Literal["letter"], PropertyInfo(alias="pageSize")]
    """
    Put every page upright on a US Letter portrait sheet: landscape pages turn a
    quarter turn, other sizes are scaled to fit
    """


class Source(TypedDict, total=False):
    object_id: Required[Annotated[str, PropertyInfo(alias="objectId")]]

    rendition: Literal["searchable_pdf", "original"]


class VolumePage(TypedDict, total=False):
    end: Required[int]

    source: Required[int]

    start: Required[int]

    bates: bool
    """false leaves these pages unstamped; they use up no Bates number"""


class VolumeBates(TypedDict, total=False):
    """This volume’s own Bates series, numbered from its own start.

    Same fields as the top-level bates.
    """

    font_size: Annotated[float, PropertyInfo(alias="fontSize")]

    legend: str

    margin_bottom: Annotated[float, PropertyInfo(alias="marginBottom")]
    """Points from the bottom edge to the label"""

    margin_side: Annotated[float, PropertyInfo(alias="marginSide")]
    """Points from the side edge to the label"""

    pad_to: Annotated[int, PropertyInfo(alias="padTo")]

    position: Literal["bottom_right", "bottom_center", "bottom_left"]

    prefix: str

    shrink: bool
    """
    Shrinks each stamped page slightly so the label sits in a clear strip below its
    content
    """

    start: int

    suffix: str


class VolumeContents(TypedDict, total=False):
    """Adds linked contents pages at the front of the volume, built from its outline.

    Outline pages stay numbered within the manifest pages.
    """

    depth: Literal[1, 2]
    """Outline levels listed"""

    title: str


class VolumeOutline(TypedDict, total=False):
    page: Required[int]
    """1-based page within this volume"""

    title: Required[str]

    children: Iterable[object]
    """Nested entries, same shape"""


class Volume(TypedDict, total=False):
    filename: Required[str]
    """Output filename, ending in .pdf"""

    pages: Required[Iterable[VolumePage]]
    """Page ranges in output order.

    Pages are 1-based and inclusive; repeats are allowed.
    """

    bates: VolumeBates
    """This volume’s own Bates series, numbered from its own start.

    Same fields as the top-level bates.
    """

    contents: VolumeContents
    """Adds linked contents pages at the front of the volume, built from its outline.

    Outline pages stay numbered within the manifest pages.
    """

    outline: Iterable[VolumeOutline]
    """Bookmarks, up to 8 levels deep"""

    title: str
    """PDF document title"""


class Bates(TypedDict, total=False):
    """Bates numbering that continues across every volume without its own series.

    Text must be printable ASCII.
    """

    font_size: Annotated[float, PropertyInfo(alias="fontSize")]

    legend: str
    """Line printed above each label"""

    margin_bottom: Annotated[float, PropertyInfo(alias="marginBottom")]
    """Points from the bottom edge to the label"""

    margin_side: Annotated[float, PropertyInfo(alias="marginSide")]
    """Points from the side edge to the label"""

    pad_to: Annotated[int, PropertyInfo(alias="padTo")]

    position: Literal["bottom_right", "bottom_center", "bottom_left"]

    prefix: str

    shrink: bool
    """
    Shrinks each stamped page slightly so the label sits in a clear strip below its
    content instead of over existing footer text
    """

    start: int

    suffix: str


class Compression(TypedDict, total=False):
    """Downsamples colour and grayscale scans above maxDpi and re-encodes them.

    Images already stored as 1-bit, JPEG 2000, indexed or CMYK keep their bytes.
    """

    bitonal: bool
    """Store pages that are only ink on paper as 1-bit images"""

    clean_scans: Annotated[bool, PropertyInfo(alias="cleanScans")]
    """Clean up scanned document pages: 300 dpi, white paper, dark ink.

    Photos and imaging keep their tones; gray stays gray and colour stays colour
    """

    encoding: Literal["jpeg2000", "jpeg"]
    """JPEG 2000 is smaller; JPEG is faster"""

    max_dpi: Annotated[int, PropertyInfo(alias="maxDpi")]

    quality: Literal["high", "standard", "small"]
