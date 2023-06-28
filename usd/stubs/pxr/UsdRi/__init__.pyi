# mypy: disable_error_code = misc
import Boost.Python
import pxr.Usd
import typing
from typing import Any, ClassVar, overload

class MaterialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, material: pxr.UsdShade.Material) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> MaterialAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def ComputeInterfaceInputConsumersMap(self, computeTransitiveConsumers: bool = ...) -> dict: ...
    def CreateDisplacementAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSurfaceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateVolumeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MaterialAPI: ...
    def GetDisplacement(self, ignoreBaseMaterial: bool = ...) -> pxr.UsdShade.Shader: ...
    def GetDisplacementAttr(self) -> pxr.Usd.Attribute: ...
    def GetDisplacementOutput(self) -> pxr.UsdShade.Output: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def GetSurface(self, ignoreBaseMaterial: bool = ...) -> pxr.UsdShade.Shader: ...
    def GetSurfaceAttr(self) -> pxr.Usd.Attribute: ...
    def GetSurfaceOutput(self) -> pxr.UsdShade.Output: ...
    def GetVolume(self, ignoreBaseMaterial: bool = ...) -> pxr.UsdShade.Shader: ...
    def GetVolumeAttr(self) -> pxr.Usd.Attribute: ...
    def GetVolumeOutput(self) -> pxr.UsdShade.Output: ...
    def SetDisplacementSource(self, arg2: pxr.Sdf.Path | str) -> bool: ...
    def SetSurfaceSource(self, arg2: pxr.Sdf.Path | str) -> bool: ...
    def SetVolumeSource(self, arg2: pxr.Sdf.Path | str) -> bool: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class RenderPassAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> RenderPassAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> RenderPassAPI: ...
    def GetCameraVisibilityCollectionAPI(self) -> pxr.Usd.CollectionAPI: ...
    def GetMatteCollectionAPI(self) -> pxr.Usd.CollectionAPI: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class SplineAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg2: pxr.Usd.Prim, arg3: object, arg4: pxr.Sdf.ValueTypeName, arg5: bool) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Usd.SchemaBase, arg3: object, arg4: pxr.Sdf.ValueTypeName, arg5: bool) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> SplineAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateInterpolationAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreatePositionsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateValuesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SplineAPI: ...
    def GetInterpolationAttr(self) -> pxr.Usd.Attribute: ...
    def GetPositionsAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def GetValuesAttr(self) -> pxr.Usd.Attribute: ...
    def GetValuesTypeName(self) -> pxr.Sdf.ValueTypeName: ...
    def Validate(self) -> tuple: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class StatementsAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> StatementsAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    @overload
    def CreateRiAttribute(self, name: str | pxr.Ar.ResolvedPath, riType: str | pxr.Ar.ResolvedPath, nameSpace: str | pxr.Ar.ResolvedPath = ...) -> pxr.Usd.Attribute: ...
    @overload
    def CreateRiAttribute(self, name: str | pxr.Ar.ResolvedPath, tfType: pxr.Tf.Type, nameSpace: str | pxr.Ar.ResolvedPath = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> StatementsAPI: ...
    def GetCoordinateSystem(self) -> str: ...
    def GetModelCoordinateSystems(self) -> list[pxr.Sdf.Path]: ...
    def GetModelScopedCoordinateSystems(self) -> list[pxr.Sdf.Path]: ...
    def GetRiAttribute(self, name: str | pxr.Ar.ResolvedPath, nameSpace: str | pxr.Ar.ResolvedPath = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetRiAttributeName(cls, prop: pxr.Usd.Property | pxr.UsdGeom.XformOp) -> str: ...
    @classmethod
    def GetRiAttributeNameSpace(cls, prop: pxr.Usd.Property | pxr.UsdGeom.XformOp) -> str: ...
    def GetRiAttributes(self, nameSpace: str | pxr.Ar.ResolvedPath = ...) -> list[pxr.Usd.Property]: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def GetScopedCoordinateSystem(self) -> str: ...
    def HasCoordinateSystem(self) -> bool: ...
    def HasScopedCoordinateSystem(self) -> bool: ...
    @classmethod
    def IsRiAttribute(cls, prop: pxr.Usd.Property | pxr.UsdGeom.XformOp) -> bool: ...
    @classmethod
    def MakeRiAttributePropertyName(cls, attrName: str | pxr.Ar.ResolvedPath) -> str: ...
    def SetCoordinateSystem(self, coordSysName: str | pxr.Ar.ResolvedPath) -> None: ...
    def SetScopedCoordinateSystem(self, coordSysName: str | pxr.Ar.ResolvedPath) -> None: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class Tokens(Boost.Python.instance):
    RiMaterialAPI: ClassVar[Any] = ...  # read-only
    RiRenderPassAPI: ClassVar[Any] = ...  # read-only
    RiSplineAPI: ClassVar[Any] = ...  # read-only
    StatementsAPI: ClassVar[Any] = ...  # read-only
    bspline: ClassVar[Any] = ...  # read-only
    cameraVisibility: ClassVar[Any] = ...  # read-only
    catmullRom: ClassVar[Any] = ...  # read-only
    collectionCameraVisibilityIncludeRoot: ClassVar[Any] = ...  # read-only
    constant: ClassVar[Any] = ...  # read-only
    interpolation: ClassVar[Any] = ...  # read-only
    linear: ClassVar[Any] = ...  # read-only
    matte: ClassVar[Any] = ...  # read-only
    outputsRiDisplacement: ClassVar[Any] = ...  # read-only
    outputsRiSurface: ClassVar[Any] = ...  # read-only
    outputsRiVolume: ClassVar[Any] = ...  # read-only
    positions: ClassVar[Any] = ...  # read-only
    renderContext: ClassVar[Any] = ...  # read-only
    spline: ClassVar[Any] = ...  # read-only
    values: ClassVar[Any] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class _CanApplyResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int) -> Any: ...
    def __iter__(self) -> typing.Iterator[Any]: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def whyNot(self) -> Any: ...

def ConvertFromRManFaceVaryingLinearInterpolation(arg1: int) -> str: ...
def ConvertFromRManInterpolateBoundary(arg1: int) -> str: ...
def ConvertToRManFaceVaryingLinearInterpolation(arg1: str | pxr.Ar.ResolvedPath) -> int: ...
def ConvertToRManInterpolateBoundary(arg1: str | pxr.Ar.ResolvedPath) -> int: ...