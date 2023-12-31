from PySide6.QtWidgets import (QWidget, QLabel, QDataWidgetMapper,
                              QLineEdit, QApplication, QGridLayout)
from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtWidgets import QListView


class Window(QWidget):
    def __init__(self, model, parent=None):
        super(Window, self).__init__(parent)
        self.model = model
        # Set up the widgets.
        nameLabel = QLabel("Na&me:")
        nameEdit = QLineEdit()
        # Set up the mapper.
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(nameEdit, 0)
        layout = QGridLayout()
        layout.addWidget(nameLabel, 0, 0, 1, 1)
        layout.addWidget(nameEdit, 0, 1, 1, 1)
        self.setLayout(layout)
        self.mapper.toLast()


class MyModel(QAbstractListModel):
    def __init__(self, status, parent=None):
        super().__init__(parent)
        self.status = status

    def rowCount(self, index_parent=None, *args, **kwargs):
        return len(self.status)

    def data(self, index, role=Qt.DisplayRole, parent=None):
        if not index.isValid():
            return None
        row = index.row()
        if row == 0:
            if role == Qt.DisplayRole:
                return self.status[row]
            elif role == Qt.EditRole:  # if it's editing mode, return value for editing
                return self.status[row]

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsEditable

    def setData(self, index, value='', role=Qt.EditRole):
        row = index.row()
        if role == Qt.EditRole:
            self.status[row] = value
            self.dataChanged.emit(index, index)  # inform the other view to request new data
            return True
        else:
            return False


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myModel_on_mywindow = MyModel([3, 2, 1])
    mywindow = Window(myModel_on_mywindow)
    mywindow.setWindowTitle('myModel_on_mywindow')
    mywindow.show()
    # myModel_on_mywindow.status[0] = 2
    myModel_on_qlistview = MyModel(['a', 'b', 'c'])
    qlistview = QListView()
    qlistview.show()
    qlistview.setModel(myModel_on_qlistview)
    qlistview.setWindowTitle('myModel_on_qlistview')
    # myModel_on_qlistview.status[0] = 2
    sys.exit(app.exec())
