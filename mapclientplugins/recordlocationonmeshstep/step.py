
"""
MAP Client Plugin Step
"""
import json
import os

from PySide6 import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.recordlocationonmeshstep.configuredialog import ConfigureDialog
from mapclientplugins.recordlocationonmeshstep.model.meshlocation import MeshLocationModel
from mapclientplugins.recordlocationonmeshstep.view.meshlocation import MeshLocationWidget


class RecordLocationonMeshStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(RecordLocationonMeshStep, self).__init__('Record Location on Mesh', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Location'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/recordlocationonmeshstep/images/segmentation.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'https://physiomeproject.org/workflow/1.0/rdf-schema#mesh_location'))
        # Port data:
        self._input_mesh_file = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        self._output_mesh_location = None  # https://physiomeproject.org/workflow/1.0/rdf-schema#mesh_location
        # Config:
        self._config = {
            'identifier': '',
        }

        self._model = None
        self._view = None

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        if self._view is None:
            self._model = MeshLocationModel()
            self._view = MeshLocationWidget(self._model)
            self._view.register_done_execution(self._doneExecution)

        self._view.set_identifier(self._config['identifier'])
        self._view.set_location(os.path.join(self._location, self._config['identifier']))
        self._view.clear()
        self._view.load(self._input_mesh_file)
        self._setCurrentWidget(self._view)

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param dataIn: The data to set for the port at the given index.
        """
        self._input_mesh_file = dataIn  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.

        :param index: Index of the port to return.
        """
        return self._output_mesh_location  # https://physiomeproject.org/workflow/1.0/rdf-schema#mesh_location

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()


