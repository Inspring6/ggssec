from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Ui_dialog_img import Ui_Dialog_img
from Ui_dialog_paint_dxf import Ui_Dialog_paint_dxf
import main


class dialog_img(QDialog, Ui_Dialog_img):
    img_mesh_begin = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.radioButton_high_density.toggled.connect(
            lambda: main.Mymainwindow.set_density(main.mainWindow(), density=40))
        self.radioButton_mid_density.toggled.connect(
            lambda: main.Mymainwindow.set_density(main.mainWindow(), density=20))
        self.radioButton_low_density.toggled.connect(
            lambda: main.Mymainwindow.set_density(main.mainWindow(), density=10))

        self.pushButton.clicked.connect(self.send)

    def send(self):
        self.img_mesh_begin.emit()
        self.close()


class dialog_paint_dxf(QDialog, Ui_Dialog_paint_dxf):
    paint_dxf_mesh_begin = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.radioButton_high_density.toggled.connect(
            lambda: main.Mymainwindow.set_density(main.mainWindow, density=40))
        self.radioButton_mid_density.toggled.connect(
            lambda: main.Mymainwindow.set_density(main.mainWindow, density=20))
        self.radioButton_low_density.toggled.connect(
            lambda: main.Mymainwindow.set_density(main.mainWindow, density=10))

        self.pushButton.clicked.connect(lambda: self.send())

    def send(self):
        self.paint_dxf_mesh_begin.emit()
        print(123)
        self.close()
