from PySide6 import QtCore

from cmlibs.utils.zinc.field import create_field_finite_element
from cmlibs.utils.zinc.finiteelement import create_nodes
from cmlibs.utils.zinc.general import ChangeManager
from cmlibs.zinc.context import Context


def _add_label_field(node):
    node_set = node.getNodeset()
    fm = node_set.getFieldmodule()
    fc = fm.createFieldcache()
    with ChangeManager(fm):
        fc.setNode(node)

        label_field = fm.createFieldStoredString()

        node_template = node_set.createNodetemplate()
        node_template.defineField(label_field)

        node.merge(node_template)

    return label_field


def _create_orientation_field(node):
    node_set = node.getNodeset()
    fm = node_set.getFieldmodule()
    with ChangeManager(fm):
        orientation_field = fm.createFieldConstant([10, 0, 0, 0, 10, 0, 0, 0, 10])

    return orientation_field


class Marker:

    def __init__(self, node, coordinate_field=None):
        self._node = node
        self._coordinate_field = coordinate_field
        self._label_field = _add_label_field(node)
        self._orientation_field = _create_orientation_field(node)
        self._pixel_scale = [1, 1, 1]
        self.set_name('unnamed')

    def identifier(self):
        return self._node.getIdentifier()

    def name(self):
        node_set = self._node.getNodeset()
        fm = node_set.getFieldmodule()
        with ChangeManager(fm):
            fc = fm.createFieldcache()
            fc.setNode(self._node)
            label = self._label_field.evaluateString(fc)

        return label

    def field(self, name='coordinate'):
        if name == 'coordinate':
            return self._coordinate_field
        elif name == 'orientation':
            return self._orientation_field
        elif name == 'label':
            return self._label_field

    def set_name(self, name):
        node_set = self._node.getNodeset()
        fm = node_set.getFieldmodule()
        with ChangeManager(fm):
            fc = fm.createFieldcache()
            fc.setNode(self._node)
            self._label_field.assignString(fc, name)

    def scale(self):
        return f'{self._pixel_scale}'

    def orientation(self):
        node_set = self._node.getNodeset()
        fm = node_set.getFieldmodule()
        with ChangeManager(fm):
            fc = fm.createFieldcache()
            fc.setNode(self._node)
            result, value = self._orientation_field.evaluateReal(fc, 9)

        return f'{value}'

    def set_scale(self, scale):
        self._pixel_scale = scale


class MarkerListModel(QtCore.QAbstractTableModel):

    def __init__(self):
        super().__init__()
        self._markers = []

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._markers)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return 3

    def headerData(self, section, orientation, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                if section == 0:
                    return 'Name'
                elif section == 1:
                    return 'Orientation'
                elif section == 2:
                    return 'Scale'
            elif orientation == QtCore.Qt.Orientation.Vertical:
                return f'{section}'

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        # print("data:", index.row(), index.column(), role)
        if index.isValid():
            # print(role, QtCore.Qt.ItemDataRole.DisplayRole, QtCore.Qt.ItemDataRole.EditRole)
            if role == QtCore.Qt.ItemDataRole.DisplayRole or role == QtCore.Qt.ItemDataRole.EditRole:
                if index.column() == 0:
                    return self._markers[index.row()].name()
                elif index.column() == 1:
                    return self._markers[index.row()].orientation()
                elif index.column() == 2:
                    return self._markers[index.row()].scale()
            elif role == QtCore.Qt.ItemDataRole.UserRole:
                return self._markers[index.row()]

    def setData(self, index, value, role=QtCore.Qt.ItemDataRole.EditRole):
        # print("set data:", index.row(), index.column(), role)
        if index.isValid():
            if role == QtCore.Qt.ItemDataRole.EditRole:
                if index.column() == 0:
                    self._markers[index.row()].set_name(value)
                    self.dataChanged.emit(index, index)
                    return True
                elif index.column() == 1:
                    print('edit col1', value)
                elif index.column() == 2:
                    self._markers[index.row()].set_scale(value)
                    self.dataChanged.emit(index, index)
                    return True

        return False

    def flags(self, index):
        if index.isValid():
            if index.column() == 0 or index.column() == 2:
                return QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEditable
            else:
                return QtCore.Qt.ItemFlag.ItemIsEnabled

        return QtCore.Qt.ItemFlag.NoItemFlags

    def append_data(self, marker):
        self.beginInsertRows(QtCore.QModelIndex(), len(self._markers), len(self._markers))
        self._markers.append(marker)
        self.endInsertRows()

    def remove_data(self, index):
        pass

    def populate(self, markers):
        self.beginResetModel()
        self._markers = markers
        self.endResetModel()

    def new(self, node, coordinate_field):
        m = Marker(node, coordinate_field)
        self.append_data(m)

    def update(self, node, parameter=None):
        row = self._find(node, mode='index')
        if parameter == 'orientation':
            index = self.index(row, 1)
            self.dataChanged.emit(index, index)

    def parameter(self, node, name='coordinate'):
        marker = self._find(node)
        if marker:
            return marker.field(name)

    def _find(self, target, mode='marker'):
        index = 0
        while index < len(self._markers):
            marker = self._markers[index]
            if marker.identifier() == target.getIdentifier():
                if mode == 'marker':
                    return marker
                else:
                    return index

            index += 1

        if mode == 'marker':
            return None
        else:
            return -1


class MeshLocationModel:

    def __init__(self):
        self._context = Context("MeshLocation")
        self._root_region = self._context.getDefaultRegion()

        self._label_region = self._root_region.createChild("_label")
        field_module = self._label_region.getFieldmodule()
        self._label_coordinates_field = create_field_finite_element(field_module, 'normalised', 2)
        create_nodes(self._label_coordinates_field, [[10.0, 10.0]])

        self._mesh_region = self._root_region.createChild("mesh")

        self._marker_model = MarkerListModel()

        self.define_standard_materials()
        self.define_standard_glyphs()

    def get_root_region(self):
        return self._root_region

    def load(self, mesh_file_location):
        fm = self._mesh_region.getFieldmodule()
        with ChangeManager(fm):
            self._mesh_region.readFile(mesh_file_location)

    def get_context(self):
        return self._context

    def get_marker_model(self):
        return self._marker_model

    def get_mesh_region(self):
        return self._mesh_region

    def get_label_region(self):
        return self._label_region

    def get_label_coordinate_field(self):
        return self._label_coordinates_field

    def remove_label_region(self):
        root_region = self._context.getDefaultRegion()
        root_region.removeChild(self._label_region)

    def define_standard_glyphs(self):
        """
        Helper method to define the standard glyphs
        """
        glyph_module = self._context.getGlyphmodule()
        glyph_module.defineStandardGlyphs()

    def define_standard_materials(self):
        """
        Helper method to define the standard materials.
        """
        material_module = self._context.getMaterialmodule()
        material_module.defineStandardMaterials()
