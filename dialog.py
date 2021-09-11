from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Ui_dialog_img import Ui_Dialog_img
from Ui_dialog_paint_dxf import Ui_Dialog_paint_dxf
import main


class dialog_img(QDialog, Ui_Dialog_img):
    img_change_type = pyqtSignal(str)
    img_change_density = pyqtSignal(int)
    img_mesh_begin = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.buttonGroup_type = QButtonGroup()
        self.buttonGroup_density = QButtonGroup()

        self.buttonGroup_type.addButton(self.radioButton_select_putRect)
        self.buttonGroup_type.addButton(self.radioButton_select_sidewayRect)
        self.buttonGroup_type.addButton(self.radioButton_select_putCircle)
        self.buttonGroup_density.addButton(self.radioButton_high_density)
        self.buttonGroup_density.addButton(self.radioButton_mid_density)
        self.buttonGroup_density.addButton(self.radioButton_low_density)
        self.buttonGroup_density.addButton(self.radioButton_custom)

        self.radioButton_select_putRect.toggled.connect(lambda: self.img_change_type.emit("正放矩形"))
        self.radioButton_select_sidewayRect.toggled.connect(lambda: self.img_change_type.emit("斜放矩形"))
        self.radioButton_select_putCircle.toggled.connect(lambda: self.img_change_type.emit("正放圆形"))

        self.radioButton_high_density.toggled.connect(lambda: self.img_change_density.emit(40))
        self.radioButton_mid_density.toggled.connect(lambda: self.img_change_density.emit(20))
        self.radioButton_low_density.toggled.connect(lambda: self.img_change_density.emit(10))
        self.radioButton_custom.toggled.connect(self.set_lineEdit)

        self.pushButton.clicked.connect(self.send)

    def send(self):
        if self.radioButton_select_putRect.isChecked() or self.radioButton_select_putCircle.isChecked() or self.radioButton_select_sidewayRect.isChecked():
            if self.radioButton_high_density.isChecked() or self.radioButton_mid_density.isChecked() or self.radioButton_low_density.isChecked():
                self.close()
                self.img_mesh_begin.emit()
            elif self.radioButton_custom.isChecked():
                if 2 < int(self.lineEdit.text()) <= 50:
                    self.img_change_density.emit(int(self.lineEdit.text()))
                    self.close()
                    self.img_mesh_begin.emit()
                else:
                    msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '请输入2—50之间的整数！')
                    msg_box.exec_()
            else:
                msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '请选择网格密度！')
                msg_box.exec_()
        else:
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '请选择图形类型！')
            msg_box.exec_()

    def set_lineEdit(self):
        self.lineEdit.setEnabled(self.radioButton_custom.isChecked())


class dialog_paint_dxf(QDialog, Ui_Dialog_paint_dxf):
    paint_dxf_change_density = pyqtSignal(int)
    paint_dxf_mesh_begin = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.radioButton_high_density.toggled.connect(lambda: self.paint_dxf_change_density.emit(40))
        self.radioButton_mid_density.toggled.connect(lambda: self.paint_dxf_change_density.emit(20))
        self.radioButton_low_density.toggled.connect(lambda: self.paint_dxf_change_density.emit(10))
        self.radioButton_custom.toggled.connect(self.set_lineEdit)

        self.pushButton.clicked.connect(self.send)

    def send(self):
        if self.radioButton_high_density.isChecked() or self.radioButton_mid_density.isChecked() or self.radioButton_low_density.isChecked():
            self.img_mesh_begin.emit()
            self.close()
        elif self.radioButton_custom.isChecked():
            if 2 < int(self.lineEdit.text()) <= 50:
                self.paint_dxf_change_density.emit(int(self.lineEdit.text()))
                self.img_mesh_begin.emit()
                self.close()
            else:
                msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '请输入2—50之间的整数！')
                msg_box.exec_()
        else:
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '请选择网格密度！')
            msg_box.exec_()

    def set_lineEdit(self):
        self.lineEdit.setEnabled(self.radioButton_custom.isChecked())
