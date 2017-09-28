# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *

from Address import *

class Consumer(QMainWindow, Ui_Window):

    def __init__(self, parent=None):
        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.btnDisplay.clicked.connect(self.showInfo)

    def showInfo(self):
        currentName = self.txtName.text()
        currentLocation = self.cboValues.currentText()

        sentence = "Name: {} \n Location: {}".format(currentName, currentLocation)

        self.txtDisplay.setText(sentence)
        self.txtRichDisplay.setText(sentence)

currentApp = QApplication(sys.argv)
currentForm = Consumer()

currentForm.show()
currentApp.exec_()
