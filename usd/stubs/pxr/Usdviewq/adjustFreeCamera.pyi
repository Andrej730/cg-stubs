# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import PySide6.QtWidgets
import pxr.Gf as Gf
import pxr.UsdGeom as UsdGeom
from pxr.Usdviewq.adjustFreeCameraUI import Ui_AdjustFreeCamera as Ui_AdjustFreeCamera
from pxr.Usdviewq.common import FixableDoubleValidator as FixableDoubleValidator
from typing import ClassVar

class AdjustFreeCamera(PySide6.QtWidgets.QDialog):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent, dataModel, signalFrustumChanged) -> None: ...
    def _aspectSpinBoxChanged(self, value): ...
    def _farChanged(self, value): ...
    def _freeCamFovChanged(self, value): ...
    def _frustumChanged(self): ...
    def _getCurrentAspectRatio(self): ...
    def _getCurrentClippingRange(self): ...
    def _getCurrentFov(self): ...
    def _lockFreeCamAspectToggled(self, state): ...
    def _nearChanged(self, value): ...
    def _overrideFarToggled(self, state): ...
    def _overrideNearToggled(self, state): ...
    def closeEvent(self, event): ...
