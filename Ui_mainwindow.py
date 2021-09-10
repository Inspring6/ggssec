# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1052, 597)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ico/mainwindow_ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1051, 521))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 26))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_openfile = QtWidgets.QMenu(self.menu_file)
        self.menu_openfile.setObjectName("menu_openfile")
        self.menu_savefile = QtWidgets.QMenu(self.menu_file)
        self.menu_savefile.setObjectName("menu_savefile")
        self.menu_tools = QtWidgets.QMenu(self.menubar)
        self.menu_tools.setObjectName("menu_tools")
        self.menu_paint_tools = QtWidgets.QMenu(self.menubar)
        self.menu_paint_tools.setObjectName("menu_paint_tools")
        self.menu_paint = QtWidgets.QMenu(self.menu_paint_tools)
        self.menu_paint.setObjectName("menu_paint")
        self.menu_change = QtWidgets.QMenu(self.menu_paint_tools)
        self.menu_change.setObjectName("menu_change")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar_showCC = QtWidgets.QStatusBar(mainWindow)
        self.statusbar_showCC.setObjectName("statusbar_showCC")
        mainWindow.setStatusBar(self.statusbar_showCC)
        self.toolBar = QtWidgets.QToolBar(mainWindow)
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_open_dxf = QtWidgets.QAction(mainWindow)
        self.action_open_dxf.setObjectName("action_open_dxf")
        self.action_open_gridsta = QtWidgets.QAction(mainWindow)
        self.action_open_gridsta.setObjectName("action_open_gridsta")
        self.action_save_img = QtWidgets.QAction(mainWindow)
        self.action_save_img.setObjectName("action_save_img")
        self.action_save_gridsta = QtWidgets.QAction(mainWindow)
        self.action_save_gridsta.setObjectName("action_save_gridsta")
        self.action_generateGrid_paint = QtWidgets.QAction(mainWindow)
        self.action_generateGrid_paint.setObjectName("action_generateGrid_paint")
        self.action_open_img = QtWidgets.QAction(mainWindow)
        self.action_open_img.setObjectName("action_open_img")
        self.action_generateGrid_dxf = QtWidgets.QAction(mainWindow)
        self.action_generateGrid_dxf.setObjectName("action_generateGrid_dxf")
        self.action_generateGrid_img = QtWidgets.QAction(mainWindow)
        self.action_generateGrid_img.setObjectName("action_generateGrid_img")
        self.action_clearboard = QtWidgets.QAction(mainWindow)
        self.action_clearboard.setObjectName("action_clearboard")
        self.action_paint_line = QtWidgets.QAction(mainWindow)
        self.action_paint_line.setObjectName("action_paint_line")
        self.action_paint_rect = QtWidgets.QAction(mainWindow)
        self.action_paint_rect.setObjectName("action_paint_rect")
        self.action_paint_ellipse = QtWidgets.QAction(mainWindow)
        self.action_paint_ellipse.setObjectName("action_paint_ellipse")
        self.action_change_width = QtWidgets.QAction(mainWindow)
        self.action_change_width.setObjectName("action_change_width")
        self.action_change_color = QtWidgets.QAction(mainWindow)
        self.action_change_color.setObjectName("action_change_color")
        self.menu_openfile.addAction(self.action_open_dxf)
        self.menu_openfile.addAction(self.action_open_img)
        self.menu_openfile.addSeparator()
        self.menu_openfile.addAction(self.action_open_gridsta)
        self.menu_savefile.addAction(self.action_save_img)
        self.menu_savefile.addSeparator()
        self.menu_savefile.addAction(self.action_save_gridsta)
        self.menu_file.addAction(self.menu_openfile.menuAction())
        self.menu_file.addAction(self.menu_savefile.menuAction())
        self.menu_tools.addAction(self.action_generateGrid_paint)
        self.menu_tools.addAction(self.action_generateGrid_dxf)
        self.menu_paint.addAction(self.action_paint_line)
        self.menu_paint.addAction(self.action_paint_rect)
        self.menu_paint.addAction(self.action_paint_ellipse)
        self.menu_change.addAction(self.action_change_width)
        self.menu_change.addAction(self.action_change_color)
        self.menu_paint_tools.addAction(self.menu_change.menuAction())
        self.menu_paint_tools.addSeparator()
        self.menu_paint_tools.addAction(self.menu_paint.menuAction())
        self.menu_paint_tools.addSeparator()
        self.menu_paint_tools.addAction(self.action_clearboard)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_paint_tools.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())
        self.toolBar.addAction(self.action_open_dxf)
        self.toolBar.addAction(self.action_open_img)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_save_img)
        self.toolBar.addAction(self.action_save_gridsta)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_clearboard)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_paint_line)
        self.toolBar.addAction(self.action_paint_rect)
        self.toolBar.addAction(self.action_paint_ellipse)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_generateGrid_dxf)
        self.toolBar.addAction(self.action_generateGrid_paint)
        self.toolBar.addAction(self.action_generateGrid_img)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "网格划分软件"))
        self.menu_file.setTitle(_translate("mainWindow", "　　文件　　"))
        self.menu_openfile.setTitle(_translate("mainWindow", "打开"))
        self.menu_savefile.setTitle(_translate("mainWindow", "保存"))
        self.menu_tools.setTitle(_translate("mainWindow", "网格生成工具"))
        self.menu_paint_tools.setTitle(_translate("mainWindow", "　绘图工具　"))
        self.menu_paint.setTitle(_translate("mainWindow", "绘制"))
        self.menu_change.setTitle(_translate("mainWindow", "调整"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))
        self.action_open_dxf.setText(_translate("mainWindow", "打开dxf文件"))
        self.action_open_dxf.setToolTip(_translate("mainWindow", "打开dxf文件"))
        self.action_open_gridsta.setText(_translate("mainWindow", "打开网格数据"))
        self.action_save_img.setText(_translate("mainWindow", "保存图片"))
        self.action_save_gridsta.setText(_translate("mainWindow", "保存网格数据"))
        self.action_generateGrid_paint.setText(_translate("mainWindow", "生成绘图网格"))
        self.action_open_img.setText(_translate("mainWindow", "打开图片"))
        self.action_generateGrid_dxf.setText(_translate("mainWindow", "生成dxf文件网格"))
        self.action_generateGrid_img.setText(_translate("mainWindow", "生成输入图片网格"))
        self.action_clearboard.setText(_translate("mainWindow", "清空画板"))
        self.action_paint_line.setText(_translate("mainWindow", "线"))
        self.action_paint_rect.setText(_translate("mainWindow", "矩形"))
        self.action_paint_ellipse.setText(_translate("mainWindow", "椭圆"))
        self.action_change_width.setText(_translate("mainWindow", "画笔线宽"))
        self.action_change_color.setText(_translate("mainWindow", "画笔颜色"))
