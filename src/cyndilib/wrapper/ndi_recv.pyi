import enum


class RecvBandwidth(enum.IntEnum):
    audio_only = ...
    highest = ...
    lowest = ...
    metadata_only = ...

class RecvColorFormat(enum.IntFlag):
    BGRX_BGRA = ...
    RGBX_RGBA = ...
    UYVY_BGRA = ...
    UYVY_RGBA = ...
    best = ...
    fastest = ...
