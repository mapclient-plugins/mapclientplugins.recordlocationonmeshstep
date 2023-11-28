import os
import json

import numpy as np
from PySide6 import QtWidgets, QtCore

from cmlibs.utils.zinc.field import find_coordinate_fields
from cmlibs.widgets.handlers.constrainednodeeditor import ConstrainedNodeEditor
from cmlibs.widgets.handlers.scenemanipulation import SceneManipulation
from cmlibs.widgets.models.fieldlist import FieldListModel

from mapclientplugins.recordlocationonmeshstep.view.ui_meshlocationwidget import Ui_MeshLocationWidget
from mapclientplugins.recordlocationonmeshstep.scene.meshlocation import MeshLocationScene


class MeshLocationWidget(QtWidgets.QWidget):

    def __init__(self, model, parent=None):
        super(MeshLocationWidget, self).__init__(parent)

        self._ui = Ui_MeshLocationWidget()
        self._ui.setupUi(self)

        self._model = model
        self._location = None
        self._callback = None

        self._scene = MeshLocationScene(model)

        self._ui.widgetZinc.set_grab_focus(True)
        self._ui.widgetZinc.set_context(model.get_context())
        self._ui.widgetZinc.register_handler(SceneManipulation())
        node_editor = ConstrainedNodeEditor(QtCore.Qt.Key.Key_A)
        self._ui.widgetZinc.register_handler(node_editor)

        marker_model = model.get_marker_model()
        node_editor.set_model(marker_model)
        self._ui.listViewMarkers.setModel(marker_model)

        self._widget_mapper = QtWidgets.QDataWidgetMapper()
        self._widget_mapper.setModel(marker_model)
        self._widget_mapper.addMapping(self._ui.lineEditOrientation, 1)
        self._widget_mapper.addMapping(self._ui.lineEditScale, 2)

        self._make_connections()

    def set_identifier(self, identifier):
        self._ui.labelMeshLocationIdentifier.setText(identifier)

    def load(self, mesh_file_location):
        self._scene.setup_visualisation()
        self._load_settings()

        # self._input_hash = _generate_hash(points_file_location)
        # if self._input_hash == previous_hash:
        #     points_file_location = self.get_output_file()
        self._model.load(mesh_file_location)
        self._setup_field_combo_boxes()

    def clear(self):
        pass

    def set_location(self, location):
        self._location = location

    def register_done_execution(self, done_execution):
        self._callback = done_execution

    def _make_connections(self):
        self._ui.pushButtonContinue.clicked.connect(self._continue_execution)
        self._ui.pushButtonViewAll.clicked.connect(self._view_all_button_clicked)
        self._ui.widgetZinc.graphics_initialized.connect(self._zinc_widget_ready)
        self._ui.widgetZinc.handler_activated.connect(self._update_label_text)
        self._ui.widgetZinc.pixel_scale_changed.connect(self._pixel_scale_changed)
        self._ui.checkBoxMeshVisibility.stateChanged.connect(self._scene.set_mesh_visibility)
        self._ui.spinBoxNodeSize.valueChanged.connect(self._scene.set_node_size)
        selection_model = self._ui.listViewMarkers.selectionModel()
        selection_model.currentRowChanged.connect(self._widget_mapper.setCurrentModelIndex)

    def _setup_field_combo_boxes(self):
        model = FieldListModel()
        model.populate(find_coordinate_fields(self._model.get_mesh_region()))

        self._ui.comboBoxCoordinateField.setModel(model)
        self._update_coordinates_field()

    def _update_coordinates_field(self):
        self._scene.update_mesh_coordinates(self._ui.comboBoxCoordinateField.currentData())

    def _settings_file(self):
        return os.path.join(self._location, 'settings.json')

    def _update_label_text(self):
        handler_label_map = {SceneManipulation: "Mode: View", ConstrainedNodeEditor: "Mode: Position"}
        handler_label = handler_label_map[type(self._ui.widgetZinc.active_handler())]
        self._scene.update_label_text(handler_label)

    def _zinc_widget_ready(self):
        pass
        # self._ui.widgetZinc.set_selection_filter(self._model.get_selection_filter())

    def _pixel_scale_changed(self, scale):
        self._scene.set_pixel_scale(scale)

    def _view_all_button_clicked(self):
        self._ui.widgetZinc.view_all()

    def _continue_execution(self):
        self._save_settings()
        self._remove_ui_region()
        self._callback()

    def _remove_ui_region(self):
        self._model.remove_label_region()

    def _load_settings(self):
        if os.path.isfile(self._settings_file()):
            with open(self._settings_file()) as f:
                settings = json.load(f)

            if "node_size" in settings:
                self._ui.spinBoxNodeSize.setValue(settings["node_size"])
                self._scene.set_node_size(settings["node_size"])

    def _save_settings(self):
        if not os.path.exists(self._location):
            os.makedirs(self._location)

        settings = {
            "node_size": self._ui.spinBoxNodeSize.value(),
        }

        with open(self._settings_file(), "w") as f:
            json.dump(settings, f)


def _calculate_best_fit_plane(points):
    actual_points = np.array(points).transpose()
    centroid = np.mean(actual_points, axis=1, keepdims=True)
    # subtract out the centroid and take the SVD
    U, S, Vh = np.linalg.svd(actual_points - centroid)

    return centroid.reshape(-1).tolist(), U[:, -1].tolist()

