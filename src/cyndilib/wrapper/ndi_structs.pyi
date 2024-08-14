# import _cython_3_0_10
from typing import TypedDict
import enum


def get_ndi_version() -> str: ...

class FourCC(enum.IntEnum):
    BGRA = ...
    BGRX = ...
    I420 = ...
    NV12 = ...
    P216 = ...
    PA16 = ...
    RGBA = ...
    RGBX = ...
    UYVA = ...
    UYVY = ...
    YV12 = ...

class FrameFormat(enum.IntEnum):
    field_0 = ...
    field_1 = ...
    interleaved = ...
    progressive = ...

class FrameType(enum.IntEnum):
    audio = ...
    error = ...
    metadata = ...
    unknown = ...
    video = ...

class NDIlib_tally_t(TypedDict):
    on_program: bool
    on_preview: bool
