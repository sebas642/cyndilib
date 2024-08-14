# import _cython_3_0_10
from typing import Any, TypedDict
from types import MethodType

import enum
import threading

from .wrapper import RecvColorFormat, RecvBandwidth
from .wrapper.ndi_structs import NDIlib_tally_t
from .locks import RLock, Condition
from .framesync import FrameSync
from .finder import Source
from .audio_frame import AudioRecvFrame
from .video_frame import VideoRecvFrame
from .metadata_frame import MetadataRecvFrame

class RecvPerformance_t(TypedDict):
    frames_total: int
    frames_dropped: int
    dropped_percent: float


class ReceiveFrameType(enum.IntFlag):
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
    audio_frame: AudioRecvFrame|None
    audio_stats: RecvPerformance_t
    connection_lock: RLock
    connection_notify: Condition
    frame_sync: FrameSync
    has_audio_frame: bool
    has_metadata_frame: bool
    has_video_frame: bool
    metadata_frame: MetadataRecvFrame|None
    metadata_stats: RecvPerformance_t
    source: Source|None
    source_name: str|None
    source_tally: NDIlib_tally_t
    video_frame: VideoRecvFrame|None
    video_stats: RecvPerformance_t
    def __init__(
        self,
        source_name: str = ...,
        source: Source|None = ...,
        color_format: RecvColorFormat = ...,
        bandwidth: RecvBandwidth = ...,
        allow_video_fields: bool = ...,
        recv_name: str = ...
    ) -> None: ...
    @property
    def preview_tally(self) -> bool: ...
    @property
    def program_tally(self) -> bool: ...
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

class RecvThread(threading.Thread):
    def __init__(self, receiver: Receiver, timeout_ms: int, recv_frame_type: int = ..., wait_time: float = ...) -> None: ...
    def run(self) -> None: ...
    def set_callback(self, cb: MethodType) -> None: ...
    def set_wait_event(self) -> None: ...
    def stop(self) -> None: ...

class RecvThreadWorker:
    # __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(
        self,
        receiver: Receiver,
        recv_frame_type: ReceiveFrameType,
        timeout_ms: int,
        wait_time: float = ...
    ) -> None: ...
    def __reduce__(self): ...
