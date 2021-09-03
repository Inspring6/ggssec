import os
import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np
import dxfgrabber
import math
from cv2 import *

from Ui_mainwindow import Ui_mainWindow
from paint_part import My_Board
from Physical_boundary_acquisition import *
from function_class import *
import dialog

class Mymainwindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        # 初始化
        self.setupUi(self)
        self.My_Area = My_Board(self)
        self.My_Area.setGeometry(5, 55, self.My_Area.pixmap_length, self.My_Area.pixmap_wigth)
        self.retranslateUi(self)
        self.density = 10
        self.dialog = None
        self.jie_dian1 = np.array([])  #########################################################################
        self.jie_dian2 = np.array([])  #########################################################################
        self.jie_dian3 = np.array([])  #########################################################################
        self.boundary_coordinates1 = []  #########################################################################
        self.boundary_coordinates2 = []  #########################################################################
        self.boundary_coordinates3 = []  #########################################################################
        self.statusBar().showMessage('                                    坐标')
        self.statusBar().show()
        self.Board_Coordinates = QLabel('')
        self.statusBar().addPermanentWidget(self.Board_Coordinates)

        # 菜单功能
        self.action_change_width.triggered.connect(self.choose_width)
        self.action_change_color.triggered.connect(self.choose_color)
        self.action_clearboard.triggered.connect(self.paint_BoardClear)
        self.action_paint_line.triggered.connect(self.choose_graph_line)
        self.action_paint_rect.triggered.connect(self.choose_graph_rect)
        self.action_paint_ellipse.triggered.connect(self.choose_graph_ellipse)

        self.action_open_dxf.triggered.connect(self.open_dxf)
        self.action_open_img.triggered.connect(self.open_img)
        self.action_open_gridsta.triggered.connect(self.open_sta)

        self.action_save_img.triggered.connect(self.save_img)
        self.action_save_gridsta.triggered.connect(self.save_sta)

        self.action_generateGrid_paint.triggered.connect(self.generateGrid_paint)
        self.action_generateGrid_dxf.triggered.connect(self.generateGrid_dxf)
        self.action_generateGrid_img.triggered.connect(self.generateGrid_img)

    def paint_BoardClear(self):
        self.My_Area._IfEmpty = 0
        self.My_Area.ellipse_list = []
        self.My_Area.rect_list = []
        self.My_Area.coord_rect_all = []
        self.My_Area.elli_short_all = []
        self.My_Area.coord_elli_all = []
        self.My_Area.elli_long_all = []
        self.My_Area.pixmap.fill(Qt.white)
        self.My_Area.update()

    def choose_width(self):
        width, ok = QInputDialog.getInt(None, '选择画笔粗细', '请输入粗细：', min=1, step=1)
        if ok:
            self.My_Area.pen_width = width

    def choose_color(self):
        Color = QColorDialog.getColor()
        if Color.isValid():
            self.My_Area.Color = Color

    def choose_graph_line(self):
        self.My_Area.Draw = '线'

    def choose_graph_rect(self):
        self.My_Area.Draw = '矩形'

    def choose_graph_ellipse(self):
        self.My_Area.Draw = '椭圆'

    def open_dxf(self):
        self.line = []
        self.circle_c = []
        self.circle_r = []
        self.lwpolyline = []
        self.ellipse_center = []
        self.ellipse_ratio_long = []
        self.ellipse_ratio = []
        self.type_of_entity = []
        dxf_name = QFileDialog.getOpenFileName(None, '选择文件', '.\\', '*.dxf')
        if dxf_name[0]:
            dxf = dxfgrabber.readfile(dxf_name[0])
            for entities in dxf.entities:
                self.type_of_entity.append(entities.dxftype)
            print(self.type_of_entity)
            if self.type_of_entity.count(self.type_of_entity[0]) == len(self.type_of_entity):
                if self.type_of_entity[0] == 'LINE':
                    for entities in dxf.entities:
                        self.line.append(entities.start[:2])
                        self.line.append(entities.end[:2])
                    self.line = set(self.line)
                    print(self.line)
                    self.line1 = list(self.line)
                if self.type_of_entity[0] == 'CIRCLE':
                    for entities in dxf.entities:
                        self.circle_c.append(list(entities.center[:2]))
                        self.circle_r.append(entities.radius)
                    print(self.circle_c)
                    print(self.circle_r)
                if self.type_of_entity[0] == 'LWPOLYLINE':
                    for entities in dxf.entities:
                        self.lwpolyline.append(list(entities.points))
                    print(self.lwpolyline)
                if self.type_of_entity[0] == 'ELLIPSE':
                    for entities in dxf.entities:
                        long_side = math.sqrt((entities.center[0] - entities.major_axis[0]) ** 2 +
                                              (entities.center[1] - entities.major_axis[1]) ** 2)
                        self.ellipse_center.append(list(entities.center)[0:2])
                        self.ellipse_ratio_long.append(long_side)
                        self.ellipse_ratio.append(entities.ratio * long_side)
                    print(
                        self.ellipse_center,
                        self.ellipse_ratio_long,
                        self.ellipse_ratio
                    )
            else:
                QMessageBox.warning(None, '警告', '非单一图形类别', QMessageBox.Yes | QMessageBox.Yes)

    def open_img(self):
        img_name = QFileDialog.getOpenFileName(None, '选择文件', '.\\')
        Filepath = img_name[0]
        if Filepath:
            self.img = cv_imread(Filepath)
            img1 = resize(self.img, None, fx=0.6, fy=0.6, interpolation=INTER_AREA)  # 将图片显示为原来的60%
            imshow('IMREAD_GRAYSCALE+Color', img1)
            self.h, self.w = self.img.shape[:]
            # self.num_edges = 1  # 多边形的边数
            waitKey(0)

    def open_sta(self):
        openPath = QFileDialog.getOpenFileName(None, '选择文件', '.\\', '*.npy')
        if openPath[0]:
            a = np.load(openPath[0])
            drawing(a)

    def save_img(self):
        savePath = QFileDialog.getSaveFileName(None, 'Save Your Paint', '.\\', '*.png')
        image = self.My_Area.make_image()
        image.save(savePath[0], "png", -1)

    def save_sta(self):  ######################################################################################
        savePath = QFileDialog.getSaveFileName(None, '选择保存路径', '.\\', '*.npy')
        print(savePath[0])
        if savePath[0]:
            if self.jie_dian1.size:
                np.save(savePath[-2], self.jie_dian1)
            if self.jie_dian2.size:
                np.save(savePath[-2], self.jie_dian2)
            if self.jie_dian3.size:
                np.save(savePath[-2], self.jie_dian3)

    def set_density(self, send_density):
        self.density =0
        self.density = send_density
        print(self.density)


    def generateGrid_paint(self):
        self.dialog = dialog.dialog_paint_dxf()
        self.dialog.show()
        self.dialog.paint_dxf_mesh_begin.connect(self.generateGrid_paint_begin)

    def generateGrid_dxf(self):
        self.dialog = dialog.dialog_paint_dxf()
        self.dialog.show()
        self.dialog.paint_dxf_mesh_begin.connect(self.generateGrid_dxf_begin)

    def generateGrid_img(self):
        self.dialog = dialog.dialog_img()
        self.dialog.show()
        self.dialog.img_mesh_begin.connect(self.generateGrid_img_begin)

    def generateGrid_paint_begin(self):
        print(self.density)
        if self.My_Area.coord_rect_all is not None:
            for i in range(len(self.My_Area.coord_rect_all)):
                plots_rect = np.array(self.My_Area.coord_rect_all[i])
                if plots_rect[0][0] == plots_rect[-1][0] and plots_rect[0][1] == plots_rect[-1][1]:
                    plots_rect = plots_rect[:len(plots_rect) - 1]
                mesh1 = polygon_block_meshing(plots_rect, self.density, self.density)
                mesh1.mesh(10)  # ##############################################################
        if self.My_Area.coord_elli_all is not None:
            for i in range(len(self.My_Area.coord_elli_all)):
                plots_ellipse = ellipse_block_meshing(self.My_Area.coord_elli_all[i], self.My_Area.elli_long_all[i],
                                                      self.My_Area.elli_short_all[i], self.density, self.density)
                plots_ellipse.mesh(5)
        plt.show()

    def generateGrid_dxf_begin(self):
        if self.type_of_entity[0] == 'LINE':
            plots = np.array(self.line1)
            mesh1 = polygon_block_meshing(plots, self.density, self.density)
            mesh1.mesh(10)
            plt.show()
        elif self.type_of_entity[0] == 'LWPOLYLINE':
            for i in range(len(self.lwpolyline)):
                plots = np.array(self.lwpolyline[i])
                if plots[0][0] == plots[-1][0] and plots[0][1] == plots[-1][1]:
                    plots = plots[:len(plots) - 1]
                mesh1 = polygon_block_meshing(plots, self.density, self.density)
                mesh1.mesh(10)
            plt.show()
        elif self.type_of_entity[0] == 'CIRCLE':
            for i in range(len(self.circle_c)):
                plots = ellipse_block_meshing(self.circle_c[i], self.circle_c[i] + np.array([self.circle_r[i], 0]),
                                              self.circle_r[i], self.density, self.density)
                plots.mesh(5)
            plt.show()
        elif self.type_of_entity[0] == 'ELLIPSE':
            for i in range(len(self.ellipse_center)):
                plots = ellipse_block_meshing(self.ellipse_center[i],
                                              self.ellipse_center[i] + np.array([self.ellipse_ratio_long[i], 0]),
                                              self.ellipse_ratio[i], self.density, self.density)
                plots.mesh(5)
            plt.show()

    def generateGrid_img_begin(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Mymainwindow()
    mainWindow.show()
    sys.exit(app.exec_())
# app = QApplication(sys.argv)
# mainWindow = Mymainwindow()
# mainWindow.show()
# sys.exit(app.exec_())
