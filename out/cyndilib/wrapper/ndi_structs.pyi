# import _cython_3_0_10
import enum

# BGRA: FourCC
# BGRX: FourCC
# I420: FourCC
# NV12: FourCC
# P216: FourCC
# PA16: FourCC
# RGBA: FourCC
# RGBX: FourCC
# UYVA: FourCC
# UYVY: FourCC
# YV12: FourCC
# __pyx_capi__: dict
# __test__: dict
# audio: FrameType
# error: FrameType
# field_0: FrameFormat
# field_1: FrameFormat
# get_ndi_version: _cython_3_0_10.cython_function_or_method
# interleaved: FrameFormat
# metadata: FrameType
# progressive: FrameFormat
# unknown: FrameType
# video: FrameType

def get_ndi_version() -> str: ...

class FourCC(enum.IntEnum):
    # __new__: ClassVar[Callable] = ...
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
