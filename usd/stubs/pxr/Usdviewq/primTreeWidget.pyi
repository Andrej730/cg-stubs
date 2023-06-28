# mypy: disable_error_code = misc
import PySide6.QtWidgets
import pxr.Sdf as Sdf
import pxr.Usd as Usd
import pxr.UsdGeom as UsdGeom
from _typeshed import Incomplete
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup
from pxr.Usdviewq.common import KeyboardShortcuts as KeyboardShortcuts, PrintWarning as PrintWarning, Timer as Timer, UIPrimTreeColors as UIPrimTreeColors
from pxr.Usdviewq.primViewItem import PrimViewColumnIndex as PrimViewColumnIndex, PrimViewItem as PrimViewItem
from typing import Any, ClassVar

class DrawModeComboBox(PySide6.QtWidgets.QComboBox):
    signalPopupHidden: ClassVar[PySide6.QtCore.Signal] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent: Incomplete | None = ...): ...
    def hidePopup(self): ...

class DrawModeItemDelegate(PySide6.QtWidgets.QStyledItemDelegate):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, makeTimer, parent: Incomplete | None = ...): ...
    def createEditor(self, parent, option, index): ...
    def paint(self, painter, option, index): ...

class DrawModeWidget(PySide6.QtWidgets.QWidget):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, primViewItem, refreshFunc, makeTimer, parent: Incomplete | None = ...): ...
    def RefreshDrawMode(self, currentDrawMode: Incomplete | None = ...): ...
    def _ClearDrawMode(self): ...
    def _CloseEditorIfNoEdit(self): ...
    def _PopupHidden(self): ...
    def _ShouldHideClearButton(self): ...
    def _UpdateDrawMode(self): ...
    def paintEvent(self, event): ...

class DrawModes(ConstantsGroup):
    BOUNDS: ClassVar[str] = ...
    CARDS: ClassVar[str] = ...
    DEFAULT: ClassVar[str] = ...
    ORIGIN: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class PrimItemSelectionModel(PySide6.QtCore.QItemSelectionModel):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    processSelections: Any
    def __init__(self, model): ...
    def clear(self): ...
    def reset(self): ...
    def select(self, indexOrSelection, command): ...

class PrimTreeWidget(PySide6.QtWidgets.QTreeWidget):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent): ...
    def ColumnPressCausesSelection(self, col): ...
    def ExpandItemRecursively(self, item): ...
    def FrameSelection(self): ...
    def InitControllers(self, appController): ...
    def ShowDrawModeWidgetForItem(self, primViewItem): ...
    def UpdatePrimViewDrawMode(self, rootItem: Incomplete | None = ...): ...
    def _refreshAncestorsOfSelected(self): ...
    def _resetAncestorsOfSelected(self): ...
    def clearSelection(self): ...
    def keyPressEvent(self, ev): ...
    def keyReleaseEvent(self, ev): ...
    def keyboardSearch(self, s): ...
    def leaveEvent(self, ev): ...
    def mousePressEvent(self, ev): ...
    def reset(self): ...
    def selectAll(self): ...
    def updateSelection(self, added, removed): ...

class SelectedAncestorItemDelegate(PySide6.QtWidgets.QStyledItemDelegate):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent: Incomplete | None = ...): ...
    def paint(self, painter, option, index): ...

class SelectionEnabler:
    def __init__(self, selectionModel): ...
    def __enter__(self): ...
    def __exit__(self, *args): ...

def _GetBackgroundColor(item, option): ...
def _GetPropertySpecInSessionLayer(usdAttribute): ...