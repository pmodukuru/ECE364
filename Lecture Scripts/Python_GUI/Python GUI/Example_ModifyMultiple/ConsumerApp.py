# Import PySide classes
from PySide.QtCore import *
from PySide.QtGui import *

from UI_Relations import *

class ConsumerApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(ConsumerApp, self).__init__(parent)
        self.setupUi(self)

        self.boxes = [self.txt1, self.txt2, self.txt3, self.txt4, self.txt5]
        self.buttons = [self.btnMon, self.btnTue, self.btnWed, self.btnThu, self.btnFri]

        self.btnAdd.clicked.connect(self.addToAll)
        self.btnSubtract.clicked.connect(self.subtractFromAll)

        for button in self.buttons:
            button.clicked.connect(self.displayDay)

    def addToAll(self):

        self.modifyValue(+1)

    def subtractFromAll(self):

        self.modifyValue(-1)

    def modifyValue(self, value):

        for box in self.boxes:
            newValue = int(box.text()) + value
            box.setText(str(newValue))

    def displayDay(self):

        button = self.sender()
        self.txtDay.setText(button.text())


if __name__ == "__main__":
    currentApp = QApplication([])
    currentForm = ConsumerApp()

    currentForm.show()
    currentApp.exec_()
