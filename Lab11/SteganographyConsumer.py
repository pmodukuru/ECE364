from PySide.QtCore import *
from PySide.QtGui import *
import sys
from Steganography import *
from SteganographyGUI import *
import numpy as np
from scipy import misc
import os
from functools import partial
from PIL import Image

def writeFile(filename, string):
    with open(filename, 'w') as myFile:
        myFile.writelines(string)

def openFile(self, filename):
        with open(filename, 'r') as File:
            lines = File.readlines()
        return lines

class Consumer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        #global function variables init
        self.payload1 = None
        self.payload1img = None

        self.payload2 = None

        self.carrier1 = None
        self.carrier1img = None
        self.carrier1Pexist = False

        self.carrier2 = None
        self.carrier2img = None
        self.carrier2Pexist = True
        self.carrier2path = None


        #object init
        self.InitObjects()

        #drag and drop init
        qviewlist = [self.viewPayload1, self.viewCarrier1, self.viewCarrier2]
        for view in qviewlist:
            view.setAcceptDrops(True)
            view.dragEnterEvent = self.dragEnterEvent
            view.dragMoveEvent = self.dragMoveEvent
            view.dragLeaveEvent = self.dragLeaveEvent
            #view.dropEvent = self.imgDrop
            #view.dropEvent = lambda e: self.imgDrop(e, view)
            view.dropEvent = partial(self.imgDrop, view)

    def InitObjects(self):
        #checkboxes
        self.chkApplyCompression.stateChanged.connect(self.compressionChkd)
        self.chkOverride.stateChanged.connect(self.overrideChkd)

        #slider
        self.slideCompression.sliderReleased.connect(self.sliderChanged) #QUESTION: SHOULD THIS BE ON RELEASE OR AS YOU DRAG (valueChanged instead of sliderReleased?)

        #buttons
        self.btnSave.clicked.connect(self.EmbedandSave)
        self.btnExtract.clicked.connect(self.ExtractPayload)
        self.btnClean.clicked.connect(self.CleanCarrier)



    def dragMoveEvent(self, e):
        e.accept()
        #print("Drag Move Event")

    def dragEnterEvent(self, e):
        #e.accept()
        if e.mimeData().hasUrls():
            e.accept()
            print("Drag")
        else:
            e.ignore()

    def dragLeaveEvent(self, e):
        e.accept()
        print("Drag Leave Event")

    def imgDrop(self, view, e):
        print("Image Dropped")

        #check if filepath dropped
        if e.mimeData().hasUrls():
            e.accept()
        else:
            return

        #retrieve filepath from data dropped
        filepath = str(e.mimeData().urls())
        print(filepath)

        match = re.search(r":(.*)'", filepath)
        filepath = match.group(1)

        #try to read image from filepath
        try:
            img = misc.imread(filepath)
        except(Exception):
            print("excepted")
            return

        #display dropped image on view
        scene = QGraphicsScene()
        pixmap = QPixmap(filepath).scaled(350, 275, Qt.KeepAspectRatio)
        scene.addPixmap(pixmap)
        view.setScene(scene)
        view.show()

        #functionality of drops

        #build payload
        if view == self.viewPayload1:
            #init payload tab
            self.txtPayloadSize.setText('')
            self.chkApplyCompression.setChecked(False)
            self.slideCompression.setValue(0)
            self.slideCompression.setDisabled(True)
            self.lblLevel.setDisabled(True)
            self.txtCompression.setText('0')
            self.txtCompression.setDisabled(True)

            #build payload
            self.payload1img = img
            self.payload1 = Payload(img=img, compressionLevel=-1)
            self.txtPayloadSize.setText(str(len(self.payload1.content)))

            self.ValidtoEmbed()


        #build carrier
        elif view == self.viewCarrier1:
            #init carrier tab
            self.lblPayloadFound.setText('')
            self.chkOverride.setDisabled(True)
            self.carrier1Pexist = False
            self.chkOverride.setChecked(False)


            #build carrier
            self.carrier1img = img
            self.carrier1 = Carrier(img=self.carrier1img)
            self.txtCarrierSize.setText(str(self.carrier1img.shape[0] * self.carrier1img.shape[1]))
            #self.txtCarrierSize.setText(str(self.carrier1img.size)

            #check for existing payload
            if self.carrier1.payloadExists():
                self.lblPayloadFound.setText('>>>>Payload Found<<<<')
                self.chkOverride.setDisabled(False)
                self.carrier1Pexist = True

            #check if payload and carrier are valid to embed
            self.ValidtoEmbed()


        #extraction from carrier
        elif view == self.viewCarrier2:
            #init carrier tab
            self.btnExtract.setDisabled(False)
            self.btnClean.setDisabled(False)
            self.carrier2Pexist = True
            self.lblCarrierEmpty.setText('')

            #clear and init payload2 view
            scene = QGraphicsScene()
            pixmap = QPixmap(None)
            scene.addPixmap(pixmap)
            self.viewPayload2.setScene(scene)
            self.viewPayload2.show()

            #build carrier
            self.carrier2img = img
            self.carrier2 = Carrier(img=self.carrier2img)
            self.carrier2path = filepath

            #check for existing payload
            if not self.carrier2.payloadExists():
                self.lblCarrierEmpty.setText('>>>>Carrier Empty<<<<')
                self.carrier2Pexist = False
                self.btnExtract.setDisabled(True)
                self.btnClean.setDisabled(True)

    def compressionChkd(self):
        #if no payload object to apply compression to
        if self.payload1 == None:
            return

        #compression checked
        if self.chkApplyCompression.isChecked():
            #enable compression level widgets
            self.slideCompression.setDisabled(False)
            self.lblLevel.setDisabled(False)
            self.txtCompression.setDisabled(False)

            #recalculate payload
            self.payload1 = Payload(img=self.payload1img, compressionLevel=int(self.txtCompression.text()))
            self.txtPayloadSize.setText(str(len(self.payload1.content)))

        else:
        #compression unchecked
            self.slideCompression.setDisabled(True)
            self.lblLevel.setDisabled(True)
            self.txtCompression.setDisabled(True)
            self.payload1 = Payload(img=self.payload1img, compressionLevel=-1)
            self.txtPayloadSize.setText(str(len(self.payload1.content)))

        #check if payload and carrier are valid to embed
        self.ValidtoEmbed()

    def sliderChanged(self):
        print("Slider Changed")
        self.payload1 = Payload(img=self.payload1img, compressionLevel=self.slideCompression.value())
        self.txtPayloadSize.setText(str(len(self.payload1.content)))
        self.txtCompression.setText(str(self.slideCompression.value()))

        #check if payload and carrier are valid to embed
        self.ValidtoEmbed()


    def ValidtoEmbed(self):
        self.btnSave.setDisabled(True)

        #check if both files provided
        if self.payload1 == None or self.carrier1 == None:
            return

        #check if size of both files is acceptable
        if int(self.txtCarrierSize.text()) < int(self.txtPayloadSize.text()):
            return

        #if payload exists, check for override Payload to be enabled
        if self.carrier1Pexist and not self.chkOverride.isChecked():
            return

        self.btnSave.setDisabled(False)

    def overrideChkd(self):
        self.ValidtoEmbed()

    def EmbedandSave(self):
        print("Embed and Save clicked")

        #embed payload in carrier
        img = self.carrier1.embedPayload(payload=self.payload1, override=self.chkOverride.isChecked())

        filename = QFileDialog.getSaveFileName(self, 'Save File', '/')
        print(filename[0])

        misc.imsave(filename[0], img)

    def ExtractPayload(self):
        print("Extract Payload")

        #clear and init payload2 view
        scene = QGraphicsScene()
        pixmap = QPixmap(None)
        scene.addPixmap(pixmap)
        self.viewPayload2.setScene(scene)
        self.viewPayload2.show()

        p1 = self.carrier2.extractPayload()

        #img = QImage(p1.img.shape()[0], p1.img.shape()[1], QImage.Format_RGB24)
        #qi = QImage(p1.img.data, p1.img.shape[1], p1.img.shape[0], p1.img.shape[1], QImage.Format_RGB888)
        qi = QImage(p1.img, p1.img.shape[1], p1.img.shape[0], p1.img.shape[1]*3, QImage.Format_RGB888)

        #display extracted image on view
        scene = QGraphicsScene()
        pixmap = QPixmap.fromImage(qi).scaled(350, 275, Qt.KeepAspectRatio)
        scene.addPixmap(pixmap)
        self.viewPayload2.setScene(scene)
        self.viewPayload2.show()

    def CleanCarrier(self):
        print("Clean Carrier")

        #clear and init payload2 view
        scene = QGraphicsScene()
        pixmap = QPixmap(None)
        scene.addPixmap(pixmap)
        self.viewPayload2.setScene(scene)
        self.viewPayload2.show()

        img = self.carrier2.clean()

        #Reset
        self.lblCarrierEmpty.setText('>>>>Carrier Empty<<<<')
        self.carrier2Pexist = False
        self.btnExtract.setDisabled(True)
        self.btnClean.setDisabled(True)

        #save new carrier
        print("Overwriting file")
        print(self.carrier2path)
        misc.imsave(self.carrier2path, img)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()