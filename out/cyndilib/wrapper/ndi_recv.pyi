import enum
from typing import Callable, ClassVar

# BGRX_BGRA: RecvColorFormat
# RGBX_RGBA: RecvColorFormat
# UYVY_BGRA: RecvColorFormat
# UYVY_RGBA: RecvColorFormat
# __pyx_capi__: dict
# __test__: dict
# audio_only: RecvBandwidth
# best: RecvColorFormat
# fastest: RecvColorFormat
# highest: RecvBandwidth
# lowest: RecvBandwidth
# metadata_only: RecvBandwidth

class RecvBandwidth(enum.IntEnum):
    # __new__: ClassVar[Callable] = ...
    # _generate_next_value_: ClassVar[Callable] = ...
    # _member_map_: ClassVar[dict] = ...
    # _member_names_: ClassVar[list] = ...
    # _member_type_: ClassVar[type[int]] = ...
    # _value2member_map_: ClassVar[dict] = ...
    audio_only = ...
    highest = ...
    lowest = ...
    metadata_only = ...

class RecvColorFormat(enum.IntFlag):
    # __new__: ClassVar[Callable] = ...
    BGRX_BGRA = ...
    RGBX_RGBA = ...
    UYVY_BGRA = ...
    UYVY_RGBA = ...
    # _generate_next_value_: ClassVar[Callable] = ...
    # _member_map_: ClassVar[dict] = ...
    # _member_names_: ClassVar[list] = ...
    # _member_type_: ClassVar[type[int]] = ...
    # _value2member_map_: ClassVar[dict] = ...
    best = ...
    fastest = ...
