# import _cython_3_0_10
import enum
import threading
from _typeshed import Incomplete
from typing import Any, Callable, ClassVar
from types import MethodType

from cyndilib.wrapper import RecvColorFormat, RecvBandwidth
from cyndilib.locks import RLock, Condition
from cyndilib.framesync import FrameSync
from cyndilib.finder import Source
from cyndilib.audio_frame import AudioRecvFrame
from cyndilib.video_frame import VideoRecvFrame
from cyndilib.metadata_frame import MetadataRecvFrame

# __pyx_capi__: dict
# __reduce_cython__: _cython_3_0_10.cython_function_or_method
# __setstate_cython__: _cython_3_0_10.cython_function_or_method
# __test__: dict
# nothing: ReceiveFrameType
# recv_all: ReceiveFrameType
# recv_audio: ReceiveFrameType
# recv_buffers_full: ReceiveFrameType
# recv_error: ReceiveFrameType
# recv_metadata: ReceiveFrameType
# recv_status_change: ReceiveFrameType
# recv_video: ReceiveFrameType
# test: _cython_3_0_10.cython_function_or_method

class ReceiveFrameType(enum.IntFlag):
    # __new__: ClassVar[Callable] = ...
    # _generate_next_value_: ClassVar[Callable] = ...
    # _member_map_: ClassVar[dict] = ...
    # _member_names_: ClassVar[list] = ...
    # _member_type_: ClassVar[type[int]] = ...
    # _value2member_map_: ClassVar[dict] = ...
    nothing = ...
    recv_all = ...
    recv_audio = ...
    recv_buffers_full = ...
    recv_error = ...
    recv_metadata = ...
    recv_status_change = ...
    recv_video = ...

class Receiver:
    # __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(
        self,
        source_name: str = ...,
        source: Source|None = ...,
        color_format: RecvColorFormat = ...,
        bandwidth: RecvBandwidth = ...,
        allow_video_fields: bool = ...,
        recv_name: str = ...
    ) -> None: ...
    audio_frame: AudioRecvFrame|None
    audio_stats: Incomplete
    connection_lock: RLock
    connection_notify: Condition
    frame_sync: FrameSync
    has_audio_frame: bool
    has_metadata_frame: bool
    has_video_frame: bool
    metadata_frame: MetadataRecvFrame|None
    metadata_stats: Incomplete
    @property
    def preview_tally(self) -> bool: ...
    @property
    def program_tally(self) -> bool: ...
    source: Source|None
    source_name: str|None
    source_tally: Incomplete
    video_frame: VideoRecvFrame|None
    video_stats: Incomplete
    # def __init__(self, *args, **kwargs) -> None: ...
    def connect_to(self, src: Source) -> Any: ...
    def disconnect(self) -> Any: ...
    def get_num_connections(self) -> Any: ...
    def get_performance_data(self) -> Any: ...
    def is_connected(self) -> Any: ...
    def receive(self, recv_type: ReceiveFrameType, timeout_ms: int) -> ReceiveFrameType: ...
    def reconnect(self) -> Any: ...
    def set_audio_frame(self, af: AudioRecvFrame) -> Any: ...
    def set_metadata_frame(self, mf: MetadataRecvFrame) -> Any: ...
    def set_source(self, src: Source) -> Any: ...
    def set_source_tally_preview(self, value: bool) -> Any: ...
    def set_source_tally_program(self, value: bool) -> Any: ...
    def set_video_frame(self, vf: VideoRecvFrame) -> Any: ...
    def __reduce__(self): ...

class RecvCreate:
    # __pyx_vtable__: ClassVar[PyCapsule] = ...
    allow_video_fields: bool
    bandwidth: RecvBandwidth
    color_format: RecvColorFormat
    recv_name: str
    source_name: str
    def __init__(
        self,
        source_name: str = ...,
        color_format: RecvColorFormat = ...,
        bandwidth: RecvBandwidth = ...,
        allow_video_fields: bool = ...,
        recv_name: str = ...
    ) -> None: ...
    def __reduce__(self): ...
    # def __reduce_cython__(self) -> Any: ...
    # def __setstate_cython__(self, __pyx_state) -> Any: ...

class RecvThread(threading.Thread):
    def __init__(self, receiver: Receiver, timeout_ms: int, recv_frame_type: int = ..., wait_time: float = ...) -> None: ...
    def run(self) -> None: ...
    def set_callback(self, cb: MethodType) -> None: ...
    def set_wait_event(self) -> None: ...
    def stop(self) -> None: ...

class RecvThreadWorker:
    # __pyx_vtable__: ClassVar[PyCapsule] = ...
    # def __init__(self, *args, **kwargs) -> None: ...
    def __init__(
        self,
        receiver: Receiver,
        recv_frame_type: ReceiveFrameType,
        timeout_ms: int,
        wait_time: float = ...
    ) -> None: ...
    def __reduce__(self): ...
    # def __reduce_cython__(self) -> Any: ...
    # def __setstate_cython__(self, __pyx_state) -> Any: ...
