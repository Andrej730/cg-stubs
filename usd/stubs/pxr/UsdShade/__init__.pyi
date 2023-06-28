# mypy: disable_error_code = misc
import Boost.Python
import pxr.Ar
import typing
from typing import Any, ClassVar, overload

class AttributeType(Boost.Python.enum):
    Input: ClassVar[AttributeType] = ...
    Invalid: ClassVar[AttributeType] = ...
    Output: ClassVar[AttributeType] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...

class ConnectableAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    @classmethod
    def CanConnect(cls, input: Input, source: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    @overload
    @classmethod
    def CanConnect(cls, output: Output, source: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output = ...) -> bool: ...
    @classmethod
    def ClearSource(cls, shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    @classmethod
    def ClearSources(cls, shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    @overload
    @classmethod
    def ConnectToSource(cls, shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, source: ConnectableAPI, sourceName: object, sourceType: AttributeType = ..., typeName: pxr.Sdf.ValueTypeName = ...) -> bool: ...
    @overload
    @classmethod
    def ConnectToSource(cls, shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, source: ConnectionSourceInfo, mod: ConnectionModification = ...) -> bool: ...
    @overload
    @classmethod
    def ConnectToSource(cls, shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, sourcePath: pxr.Sdf.Path | str) -> bool: ...
    @overload
    @classmethod
    def ConnectToSource(cls, shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, input: Input) -> bool: ...
    @overload
    @classmethod
    def ConnectToSource(cls, shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, output: Output) -> bool: ...
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Input: ...
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Output: ...
    @classmethod
    def DisconnectSource(cls, shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, sourceAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output = ...) -> bool: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> ConnectableAPI: ...
    @classmethod
    def GetConnectedSource(cls, shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> Any: ...
    @classmethod
    def GetConnectedSources(cls, shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> Any: ...
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> Input: ...
    def GetInputs(self, onlyAuthored: bool = ...) -> list[Input]: ...
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> Output: ...
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[Output]: ...
    @classmethod
    def GetRawConnectedSourcePaths(cls, shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> list: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def HasConnectableAPI(cls, schemaType: pxr.Tf.Type) -> bool: ...
    @classmethod
    def HasConnectedSource(cls, shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    def IsContainer(self) -> bool: ...
    @classmethod
    def IsSourceConnectionFromBaseMaterial(cls, shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    def RequiresEncapsulation(self) -> bool: ...
    @classmethod
    def SetConnectedSources(cls, arg1: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, arg2: typing.Iterable[ConnectionSourceInfo]) -> bool: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class ConnectionModification(Boost.Python.enum):
    Append: ClassVar[ConnectionModification] = ...
    Prepend: ClassVar[ConnectionModification] = ...
    Replace: ClassVar[ConnectionModification] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...

class ConnectionSourceInfo(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    source: Any
    sourceName: Any
    sourceType: Any
    typeName: Any
    @overload
    def __init__(self, source: ConnectableAPI, sourceName: object, sourceType: AttributeType, typeName: pxr.Sdf.ValueTypeName = ...) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Usd.Stage, arg3: pxr.Sdf.Path | str) -> None: ...
    @overload
    def __init__(self, input: Input) -> None: ...
    @overload
    def __init__(self, output: Output) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def IsValid(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...

class CoordSysAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg2: pxr.Usd.Prim, arg3: object) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Usd.SchemaBase, arg3: object) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> CoordSysAPI: ...
    def ApplyAndBind(self, name: str | pxr.Ar.ResolvedPath, path: pxr.Sdf.Path | str) -> bool: ...
    @overload
    def Bind(self, name: str | pxr.Ar.ResolvedPath, path: pxr.Sdf.Path | str) -> bool: ...
    @overload
    def Bind(self, path: pxr.Sdf.Path | str) -> bool: ...
    def BlockBinding(self, name: object = ...) -> bool: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> _CanApplyResult: ...
    @classmethod
    def CanContainPropertyName(cls, name: str | pxr.Ar.ResolvedPath) -> bool: ...
    @overload
    def ClearBinding(self, name: str | pxr.Ar.ResolvedPath, removeSpec: bool) -> bool: ...
    @overload
    def ClearBinding(self, removeSpec: bool) -> bool: ...
    def CreateBindingRel(self) -> pxr.Usd.Relationship: ...
    def FindBindingWithInheritance(self) -> pxr.UsdSkel.Binding: ...
    def FindBindingsWithInheritance(self) -> list[pxr.UsdSkel.Binding]: ...
    @classmethod
    def FindBindingsWithInheritanceForPrim(cls, arg1: pxr.Usd.Prim) -> list[pxr.UsdSkel.Binding]: ...
    @overload
    @classmethod
    def Get(cls, prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> CoordSysAPI: ...
    @overload
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> CoordSysAPI: ...
    @classmethod
    def GetAll(cls, prim: pxr.Usd.Prim) -> list[CoordSysAPI]: ...
    def GetBindingRel(self) -> pxr.Usd.Relationship: ...
    @classmethod
    def GetCoordSysRelationshipName(cls, coordSysName: str | pxr.Ar.ResolvedPath) -> str: ...
    def GetLocalBinding(self) -> pxr.UsdSkel.Binding: ...
    def GetLocalBindings(self) -> list[pxr.UsdSkel.Binding]: ...
    @classmethod
    def GetLocalBindingsForPrim(cls, prim: pxr.Usd.Prim) -> list[pxr.UsdSkel.Binding]: ...
    @overload
    @classmethod
    def GetSchemaAttributeNames(cls, arg1: bool, includeInherited: str | pxr.Ar.ResolvedPath) -> list[str]: ...
    @overload
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def HasLocalBindings(self) -> bool: ...
    @classmethod
    def HasLocalBindingsForPrim(cls, prim: pxr.Usd.Prim) -> bool: ...
    @classmethod
    def IsCoordSysAPIPath(cls, arg1: pxr.Sdf.Path | str) -> bool: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class Input(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CanConnect(self, source: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    def ClearConnectability(self) -> bool: ...
    def ClearSdrMetadata(self) -> None: ...
    def ClearSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> None: ...
    def ClearSource(self) -> bool: ...
    def ClearSources(self) -> bool: ...
    @overload
    def ConnectToSource(self, source: ConnectableAPI, sourceName: str | pxr.Ar.ResolvedPath, sourceType: AttributeType = ..., typeName: pxr.Sdf.ValueTypeName = ...) -> bool: ...
    @overload
    def ConnectToSource(self, source: ConnectionSourceInfo, mod: ConnectionModification = ...) -> bool: ...
    @overload
    def ConnectToSource(self, input: Input) -> bool: ...
    @overload
    def ConnectToSource(self, output: Output) -> bool: ...
    @overload
    def ConnectToSource(self, sourcePath: pxr.Sdf.Path | str) -> bool: ...
    def DisconnectSource(self, sourceAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output = ...) -> bool: ...
    def Get(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> Any: ...
    def GetAttr(self) -> pxr.Usd.Attribute: ...
    def GetBaseName(self) -> str: ...
    def GetConnectability(self) -> str: ...
    def GetConnectedSource(self) -> tuple[ConnectableAPI, str, AttributeType]: ...
    def GetConnectedSources(self) -> tuple[list[SourceInfo], list[pxr.Sdf.Path]]: ...
    def GetDisplayGroup(self) -> str: ...
    def GetDocumentation(self) -> str: ...
    def GetFullName(self) -> str: ...
    def GetPrim(self) -> pxr.Usd.Prim: ...
    def GetRawConnectedSourcePaths(self) -> list[pxr.Sdf.Path]: ...
    def GetRenderType(self) -> str: ...
    def GetSdrMetadata(self) -> pxr.Ndr.TokenMap: ...
    def GetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> str: ...
    def GetTypeName(self) -> pxr.Sdf.ValueTypeName: ...
    def GetValueProducingAttribute(self) -> tuple[pxr.Usd.Attribute, AttributeType]: ...
    def GetValueProducingAttributes(self, shaderOutputsOnly: bool = ...) -> list[Attribute]: ...
    def HasConnectedSource(self) -> bool: ...
    def HasRenderType(self) -> bool: ...
    def HasSdrMetadata(self) -> bool: ...
    def HasSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> bool: ...
    @classmethod
    def IsInput(cls, arg1: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    @classmethod
    def IsInterfaceInputName(cls, arg1: str | pxr.Ar.ResolvedPath) -> bool: ...
    def IsSourceConnectionFromBaseMaterial(self) -> bool: ...
    def Set(self, value: object, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool: ...
    def SetConnectability(self, arg2: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetConnectedSources(self, arg2: typing.Iterable[ConnectionSourceInfo]) -> bool: ...
    def SetDisplayGroup(self, arg2: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetDocumentation(self, arg2: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetRenderType(self, renderType: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetSdrMetadata(self, sdrMetadata: pxr.Ndr.TokenMap) -> None: ...
    def SetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath, value: str | pxr.Ar.ResolvedPath) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...

class Material(NodeGraph):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def ClearBaseMaterial(self) -> None: ...
    def ComputeDisplacementSource(self, renderContext: object = ...) -> Any: ...
    def ComputeSurfaceSource(self, renderContext: object = ...) -> Any: ...
    def ComputeVolumeSource(self, renderContext: object = ...) -> Any: ...
    def CreateDisplacementAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDisplacementOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output: ...
    @classmethod
    def CreateMasterMaterialVariant(cls, masterPrim: pxr.Usd.Prim, materialPrims: typing.Iterable[pxr.Usd.Prim], masterVariantSetName: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def CreateSurfaceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSurfaceOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output: ...
    def CreateVolumeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateVolumeOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Material: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Material: ...
    def GetBaseMaterial(self) -> Material: ...
    def GetBaseMaterialPath(self) -> pxr.Sdf.Path: ...
    def GetDisplacementAttr(self) -> pxr.Usd.Attribute: ...
    def GetDisplacementOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output: ...
    def GetDisplacementOutputs(self) -> list[Output]: ...
    def GetEditContextForVariant(self, materialVariantName: str | pxr.Ar.ResolvedPath, layer: pxr.Sdf.Layer = ...) -> pxr.Usd.EditContext: ...
    def GetMaterialVariant(self) -> pxr.Usd.VariantSet: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def GetSurfaceAttr(self) -> pxr.Usd.Attribute: ...
    def GetSurfaceOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output: ...
    def GetSurfaceOutputs(self) -> list[Output]: ...
    def GetVolumeAttr(self) -> pxr.Usd.Attribute: ...
    def GetVolumeOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output: ...
    def GetVolumeOutputs(self) -> list[Output]: ...
    def HasBaseMaterial(self) -> bool: ...
    def SetBaseMaterial(self, baseMaterial: Material) -> None: ...
    def SetBaseMaterialPath(self, baseLookPath: pxr.Sdf.Path | str) -> None: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class MaterialBindingAPI(pxr.Usd.APISchemaBase):
    class CollectionBinding(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        @overload
        def __init__(self, collBindingRel: pxr.Usd.Relationship) -> None: ...
        @overload
        def __init__(self) -> None: ...
        def GetBindingRel(self) -> pxr.Usd.Relationship: ...
        def GetCollection(self) -> pxr.Usd.CollectionAPI: ...
        def GetCollectionPath(self) -> pxr.Sdf.Path: ...
        def GetMaterial(self) -> Material: ...
        def GetMaterialPath(self) -> pxr.Sdf.Path: ...
        def IsCollectionBindingRel(self, bindingRel: pxr.Usd.Relationship) -> bool: ...
        def IsValid(self) -> bool: ...
        def __reduce__(self) -> Any: ...
    class DirectBinding(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        @overload
        def __init__(self, bindingRel: pxr.Usd.Relationship) -> None: ...
        @overload
        def __init__(self) -> None: ...
        def GetBindingRel(self) -> pxr.Usd.Relationship: ...
        def GetMaterial(self) -> Material: ...
        def GetMaterialPath(self) -> pxr.Sdf.Path: ...
        def GetMaterialPurpose(self) -> Any: ...
        def __reduce__(self) -> Any: ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def AddPrimToBindingCollection(self, prim: pxr.Usd.Prim, bindingName: str | pxr.Ar.ResolvedPath, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> MaterialBindingAPI: ...
    @overload
    def Bind(self, collection: pxr.Usd.CollectionAPI, material: Material, bindingName: str | pxr.Ar.ResolvedPath = ..., bindingStrength: str | pxr.Ar.ResolvedPath = ..., materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    @overload
    def Bind(self, material: Material, bindingStrength: str | pxr.Ar.ResolvedPath = ..., materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    @classmethod
    def CanContainPropertyName(cls, name: str | pxr.Ar.ResolvedPath) -> bool: ...
    def ComputeBoundMaterial(self, materialPurpose: object = ...) -> Any: ...
    @classmethod
    def ComputeBoundMaterials(cls, prims: typing.Iterable[pxr.Usd.Prim], materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> tuple[list[Material], list[pxr.Usd.Relationship]]: ...
    def CreateMaterialBindSubset(self, subsetName: str | pxr.Ar.ResolvedPath, indices: pxr.Vt.IntArray | typing.Iterable[int], elementType: str | pxr.Ar.ResolvedPath = ...) -> pxr.UsdGeom.Subset: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MaterialBindingAPI: ...
    def GetCollectionBindingRel(self, bindingName: str | pxr.Ar.ResolvedPath, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> pxr.Usd.Relationship: ...
    def GetCollectionBindingRels(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> list[pxr.Usd.Relationship]: ...
    def GetCollectionBindings(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> list[MaterialBindingAPI.CollectionBinding]: ...
    def GetDirectBinding(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> MaterialBindingAPI.DirectBinding: ...
    def GetDirectBindingRel(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> pxr.Usd.Relationship: ...
    def GetMaterialBindSubsets(self) -> list[pxr.UsdGeom.Subset]: ...
    def GetMaterialBindSubsetsFamilyType(self) -> str: ...
    @classmethod
    def GetMaterialBindingStrength(cls, bindingRel: pxr.Usd.Relationship) -> str: ...
    @classmethod
    def GetMaterialPurposes(cls) -> list[str]: ...
    @classmethod
    def GetResolvedTargetPathFromBindingRel(cls, bindingRel: pxr.Usd.Relationship) -> pxr.Sdf.Path: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def RemovePrimFromBindingCollection(self, prim: pxr.Usd.Prim, bindingName: str | pxr.Ar.ResolvedPath, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def SetMaterialBindSubsetsFamilyType(self, familyType: str | pxr.Ar.ResolvedPath) -> bool: ...
    @classmethod
    def SetMaterialBindingStrength(cls, arg1: pxr.Usd.Relationship, bindingRel: str | pxr.Ar.ResolvedPath) -> bool: ...
    def UnbindAllBindings(self) -> bool: ...
    def UnbindCollectionBinding(self, bindingName: str | pxr.Ar.ResolvedPath, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def UnbindDirectBinding(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class NodeDefAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> NodeDefAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateIdAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateImplementationSourceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NodeDefAPI: ...
    def GetIdAttr(self) -> pxr.Usd.Attribute: ...
    def GetImplementationSource(self) -> str: ...
    def GetImplementationSourceAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def GetShaderId(self) -> str: ...
    def GetShaderNodeForSourceType(self, sourceType: str | pxr.Ar.ResolvedPath) -> pxr.Sdr.ShaderNode: ...
    def GetSourceAsset(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> pxr.Sdf.AssetPath: ...
    def GetSourceAssetSubIdentifier(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> str: ...
    def GetSourceCode(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> str: ...
    def SetShaderId(self, arg2: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetSourceAsset(self, sourceAsset: pxr.Sdf.AssetPath | str, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def SetSourceAssetSubIdentifier(self, subIdentifier: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def SetSourceCode(self, sourceCode: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class NodeGraph(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, connectable: ConnectableAPI) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def ComputeInterfaceInputConsumersMap(self, computeTransitiveConsumers: bool = ...) -> dict: ...
    def ComputeOutputSource(self, outputName: str | pxr.Ar.ResolvedPath) -> tuple[Shader, str, AttributeType]: ...
    def ConnectableAPI(self) -> ConnectableAPI: ...
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Input: ...
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, typeName: pxr.Sdf.ValueTypeName) -> Output: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NodeGraph: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NodeGraph: ...
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> Input: ...
    def GetInputs(self, onlyAuthored: bool = ...) -> list[Input]: ...
    def GetInterfaceInputs(self) -> list[Input]: ...
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> Output: ...
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[Output]: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class Output(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CanConnect(self, source: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    def ClearSdrMetadata(self) -> None: ...
    def ClearSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> None: ...
    def ClearSource(self) -> bool: ...
    def ClearSources(self) -> bool: ...
    @overload
    def ConnectToSource(self, source: ConnectableAPI, sourceName: str | pxr.Ar.ResolvedPath, sourceType: AttributeType = ..., typeName: pxr.Sdf.ValueTypeName = ...) -> bool: ...
    @overload
    def ConnectToSource(self, source: ConnectionSourceInfo, mod: ConnectionModification = ...) -> bool: ...
    @overload
    def ConnectToSource(self, sourceInput: Input) -> bool: ...
    @overload
    def ConnectToSource(self, sourceOutput: Output) -> bool: ...
    @overload
    def ConnectToSource(self, sourcePath: pxr.Sdf.Path | str) -> bool: ...
    def DisconnectSource(self, sourceAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output = ...) -> bool: ...
    def GetAttr(self) -> pxr.Usd.Attribute: ...
    def GetBaseName(self) -> str: ...
    def GetConnectedSource(self) -> tuple[ConnectableAPI, str, AttributeType]: ...
    def GetConnectedSources(self) -> tuple[list[SourceInfo], list[pxr.Sdf.Path]]: ...
    def GetFullName(self) -> str: ...
    def GetPrim(self) -> pxr.Usd.Prim: ...
    def GetRawConnectedSourcePaths(self) -> list[pxr.Sdf.Path]: ...
    def GetRenderType(self) -> str: ...
    def GetSdrMetadata(self) -> pxr.Ndr.TokenMap: ...
    def GetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> str: ...
    def GetTypeName(self) -> pxr.Sdf.ValueTypeName: ...
    def GetValueProducingAttributes(self, shaderOutputsOnly: bool = ...) -> list[Attribute]: ...
    def HasConnectedSource(self) -> bool: ...
    def HasRenderType(self) -> bool: ...
    def HasSdrMetadata(self) -> bool: ...
    def HasSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> bool: ...
    @classmethod
    def IsOutput(cls, arg1: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool: ...
    def IsSourceConnectionFromBaseMaterial(self) -> bool: ...
    def Set(self, value: object, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool: ...
    def SetConnectedSources(self, arg2: typing.Iterable[ConnectionSourceInfo]) -> bool: ...
    def SetRenderType(self, renderType: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetSdrMetadata(self, sdrMetadata: pxr.Ndr.TokenMap) -> None: ...
    def SetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath, value: str | pxr.Ar.ResolvedPath) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...

class Shader(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, connectable: ConnectableAPI) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def ClearSdrMetadata(self) -> None: ...
    def ClearSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> None: ...
    def ConnectableAPI(self) -> ConnectableAPI: ...
    def CreateIdAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateImplementationSourceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Input: ...
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Output: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Shader: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Shader: ...
    def GetIdAttr(self) -> pxr.Usd.Attribute: ...
    def GetImplementationSource(self) -> str: ...
    def GetImplementationSourceAttr(self) -> pxr.Usd.Attribute: ...
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> Input: ...
    def GetInputs(self, onlyAuthored: bool = ...) -> list[Input]: ...
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> Output: ...
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[Output]: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def GetSdrMetadata(self) -> pxr.Ndr.TokenMap: ...
    def GetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> str: ...
    def GetShaderId(self) -> str: ...
    def GetShaderNodeForSourceType(self, sourceType: str | pxr.Ar.ResolvedPath) -> pxr.Sdr.ShaderNode: ...
    def GetSourceAsset(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> pxr.Sdf.AssetPath: ...
    def GetSourceAssetSubIdentifier(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> str: ...
    def GetSourceCode(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> str: ...
    def HasSdrMetadata(self) -> bool: ...
    def HasSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetSdrMetadata(self, sdrMetadata: pxr.Ndr.TokenMap) -> None: ...
    def SetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath, value: str | pxr.Ar.ResolvedPath) -> None: ...
    def SetShaderId(self, arg2: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetSourceAsset(self, sourceAsset: pxr.Sdf.AssetPath | str, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def SetSourceAssetSubIdentifier(self, subIdentifier: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    def SetSourceCode(self, sourceCode: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class ShaderDefParserPlugin(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def GetDiscoveryTypes(self) -> pxr.Ndr.TokenVec: ...
    def GetSourceType(self) -> str: ...
    def Parse(self, arg2: pxr.Ndr.NodeDiscoveryResult) -> pxr.Sdr.ShaderNode: ...
    def __reduce__(self) -> Any: ...

class ShaderDefUtils(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetNodeDiscoveryResults(cls, shaderDef: Shader, sourceUri: str | pxr.Ar.ResolvedPath) -> list: ...
    @classmethod
    def GetPrimvarNamesMetadataString(cls, metadata: pxr.Ndr.TokenMap, shaderDef: ConnectableAPI) -> str: ...
    @classmethod
    def GetShaderProperties(cls, shaderDef: ConnectableAPI) -> list: ...
    def __reduce__(self) -> Any: ...

class Tokens(Boost.Python.instance):
    ConnectableAPI: ClassVar[Any] = ...  # read-only
    CoordSysAPI: ClassVar[Any] = ...  # read-only
    Material: ClassVar[Any] = ...  # read-only
    MaterialBindingAPI: ClassVar[Any] = ...  # read-only
    NodeDefAPI: ClassVar[Any] = ...  # read-only
    NodeGraph: ClassVar[Any] = ...  # read-only
    Shader: ClassVar[Any] = ...  # read-only
    allPurpose: ClassVar[Any] = ...  # read-only
    bindMaterialAs: ClassVar[Any] = ...  # read-only
    coordSys: ClassVar[Any] = ...  # read-only
    coordSys_MultipleApplyTemplate_Binding: ClassVar[Any] = ...  # read-only
    displacement: ClassVar[Any] = ...  # read-only
    fallbackStrength: ClassVar[Any] = ...  # read-only
    full: ClassVar[Any] = ...  # read-only
    id: ClassVar[Any] = ...  # read-only
    infoId: ClassVar[Any] = ...  # read-only
    infoImplementationSource: ClassVar[Any] = ...  # read-only
    inputs: ClassVar[Any] = ...  # read-only
    interfaceOnly: ClassVar[Any] = ...  # read-only
    materialBind: ClassVar[Any] = ...  # read-only
    materialBinding: ClassVar[Any] = ...  # read-only
    materialBindingCollection: ClassVar[Any] = ...  # read-only
    materialVariant: ClassVar[Any] = ...  # read-only
    outputs: ClassVar[Any] = ...  # read-only
    outputsDisplacement: ClassVar[Any] = ...  # read-only
    outputsSurface: ClassVar[Any] = ...  # read-only
    outputsVolume: ClassVar[Any] = ...  # read-only
    preview: ClassVar[Any] = ...  # read-only
    sdrMetadata: ClassVar[Any] = ...  # read-only
    sourceAsset: ClassVar[Any] = ...  # read-only
    sourceCode: ClassVar[Any] = ...  # read-only
    strongerThanDescendants: ClassVar[Any] = ...  # read-only
    subIdentifier: ClassVar[Any] = ...  # read-only
    surface: ClassVar[Any] = ...  # read-only
    universalRenderContext: ClassVar[Any] = ...  # read-only
    universalSourceType: ClassVar[Any] = ...  # read-only
    volume: ClassVar[Any] = ...  # read-only
    weakerThanDescendants: ClassVar[Any] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class UdimUtils(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def IsUdimIdentifier(cls, identifier: str | pxr.Ar.ResolvedPath) -> bool: ...
    @classmethod
    def ReplaceUdimPattern(cls, identifierWithPattern: str | pxr.Ar.ResolvedPath, replacement: str | pxr.Ar.ResolvedPath) -> str: ...
    @classmethod
    def ResolveUdimPath(cls, udimPath: str | pxr.Ar.ResolvedPath, layer: pxr.Sdf.Layer) -> str: ...
    @classmethod
    def ResolveUdimTilePaths(cls, udimPath: str | pxr.Ar.ResolvedPath, layer: pxr.Sdf.Layer) -> list[ResolvedPathAndTile]: ...
    def __reduce__(self) -> Any: ...

class Utils(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetBaseNameAndType(cls, arg1: str | pxr.Ar.ResolvedPath) -> tuple[str, AttributeType]: ...
    @classmethod
    def GetConnectedSourcePath(cls, connectionSourceInfo: ConnectionSourceInfo) -> pxr.Sdf.Path: ...
    @classmethod
    def GetFullName(cls, arg1: str | pxr.Ar.ResolvedPath, arg2: AttributeType) -> str: ...
    @classmethod
    def GetPrefixForAttributeType(cls, arg1: AttributeType) -> str: ...
    @classmethod
    def GetType(cls, arg1: str | pxr.Ar.ResolvedPath) -> AttributeType: ...
    @overload
    @classmethod
    def GetValueProducingAttributes(cls, input: Input, shaderOutputsOnly: bool = ...) -> list[Attribute]: ...
    @overload
    @classmethod
    def GetValueProducingAttributes(cls, output: Output, shaderOutputsOnly: bool = ...) -> list[Attribute]: ...
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