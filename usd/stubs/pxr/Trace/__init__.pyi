# mypy: disable_error_code = misc
import Boost.Python
import pxr.Ar
from typing import Any, Callable, overload

TraceFunction: Callable
TraceMethod: Callable
TraceScope: Callable

class AggregateNode(Boost.Python.instance):
    expanded: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def children(self) -> list[AggregateNode]: ...
    @property
    def count(self) -> Any: ...
    @property
    def exclusiveCount(self) -> int: ...
    @property
    def exclusiveTime(self) -> Any: ...
    @property
    def expired(self) -> Any: ...
    @property
    def id(self) -> pxr.Usd.StageCache.Id: ...
    @property
    def inclusiveTime(self) -> TimeStamp: ...
    @property
    def key(self) -> str: ...

class Collector(Boost.Python.instance):
    enabled: Any
    pythonTracingEnabled: Any
    def __init__(self) -> None: ...
    def BeginEvent(self, arg2: str | pxr.Ar.ResolvedPath) -> int: ...
    def BeginEventAtTime(self, arg2: str | pxr.Ar.ResolvedPath, arg3: float) -> None: ...
    def Clear(self) -> None: ...
    def EndEvent(self, arg2: str | pxr.Ar.ResolvedPath) -> int: ...
    def EndEventAtTime(self, arg2: str | pxr.Ar.ResolvedPath, arg3: float) -> None: ...
    def GetLabel(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class Reporter(Boost.Python.instance):
    foldRecursiveCalls: bool
    groupByFunction: bool
    shouldAdjustForOverheadAndNoise: Any
    def __init__(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    def ClearTree(self) -> None: ...
    def GetLabel(self) -> str: ...
    @overload
    def Report(self, arg2: str | pxr.Ar.ResolvedPath, iterationCount: int = ..., append: bool = ...) -> None: ...
    @overload
    def Report(self, iterationCount: int = ...) -> None: ...
    def ReportChromeTracing(self) -> None: ...
    def ReportChromeTracingToFile(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    def ReportTimes(self) -> None: ...
    def UpdateTraceTrees(self) -> None: ...
    @classmethod
    def globalReporter(cls) -> TRACE_APITraceReporterPtr: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def aggregateTreeRoot(self) -> AggregateNode: ...
    @property
    def expired(self) -> Any: ...

def GetElapsedSeconds(arg1: int, arg2: int) -> float: ...
def GetTestEventName() -> str: ...
def TestAuto() -> None: ...
def TestCreateEvents() -> None: ...
def TestNesting() -> None: ...