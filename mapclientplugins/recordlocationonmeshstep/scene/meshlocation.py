from cmlibs.utils.zinc.general import ChangeManager
from cmlibs.zinc.field import Field
from cmlibs.zinc.glyph import Glyph
from cmlibs.zinc.scenecoordinatesystem import SCENECOORDINATESYSTEM_WINDOW_PIXEL_BOTTOM_LEFT


class MeshLocationScene(object):

    def __init__(self, model):
        self._model = model
        self._mesh_lines = None
        self._surface_graphics = None
        self._label_graphics = None
        self._point_graphics = None
        self._pixel_scale = 1.0
        self._point_base_size = 1.0 * self._pixel_scale

    def set_mesh_visibility(self, state):
        self._mesh_lines.setVisibilityFlag(state != 0)

    def set_surface_visibility(self, state):
        self._surface_graphics.setVisibilityFlag(state != 0)

    def update_mesh_coordinates(self, coordinate_field):
        self._mesh_lines.setCoordinateField(coordinate_field)
        self._surface_graphics.setCoordinateField(coordinate_field)
        self._point_graphics.setCoordinateField(coordinate_field)

    def update_label_text(self, handler_label):
        attributes = self._label_graphics.getGraphicspointattributes()
        attributes.setLabelText(1, handler_label)

    def set_pixel_scale(self, scale):
        self._pixel_scale = scale
        attributes = self._label_graphics.getGraphicspointattributes()
        attributes.setGlyphOffset([2.0 * scale, 0.0])
        font = attributes.getFont()
        font.setPointSize(int(font.getPointSize() * scale + 0.5))

        self._update_graphic_point_size()

    def set_node_size(self, size):
        self._point_base_size = size
        self._update_graphic_point_size()

    def setup_visualisation(self):
        region = self._model.get_mesh_region()
        scene = region.getScene()
        mm = scene.getMaterialmodule()
        green = mm.findMaterialByName('green')

        with ChangeManager(scene):
            scene.removeAllGraphics()
            line_graphic = scene.createGraphicsLines()
            line_graphic.setMaterial(green)
            surface_graphic = scene.createGraphicsSurfaces()
            point_graphic = scene.createGraphicsPoints()
            point_graphic.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
            attributes = point_graphic.getGraphicspointattributes()
            attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
            attributes.setBaseSize(self._point_base_size)

        self._mesh_lines = line_graphic
        self._surface_graphics = surface_graphic
        self._point_graphics = point_graphic

        normalised_region = self._model.get_label_region()

        normalised_scene = normalised_region.getScene()
        with ChangeManager(normalised_scene):
            normalised_scene.removeAllGraphics()
            graphics_points = normalised_scene.createGraphicsPoints()
            graphics_points.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
            graphics_points.setCoordinateField(self._model.get_label_coordinate_field())
            graphics_points.setScenecoordinatesystem(SCENECOORDINATESYSTEM_WINDOW_PIXEL_BOTTOM_LEFT)

        self._label_graphics = graphics_points

    def _update_graphic_point_size(self):
        attributes = self._point_graphics.getGraphicspointattributes()
        attributes.setBaseSize(self._point_base_size)
