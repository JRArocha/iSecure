from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from pickle import TRUE
import numpy as np
import os
import time
import datetime
from pushbullet import PushBullet
import sys, res
import cv2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 804)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/image/logo.jpg"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 1391, 781))
        self.widget.setObjectName("widget")
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1371, 751))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(47, 47, 47);")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(159, 40))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")


        # HOME TAB

        # Home Camera Start
        self.HomeCamera = HomeCamera()
        self.HomeCamera.start()
        self.HomeCamera.ImageUpdate.connect(self.ImageUpdateSlot)

        self.Home = QWidget()
        self.Home.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"")
        self.Home.setObjectName("Home")
        self.labelHome = QLabel(self.Home)
        self.labelHome.setGeometry(QtCore.QRect(40, 50, 1291, 601))
        self.labelHome.setStyleSheet("color: white;\n"
"font-size: 100px;\n"
"")
        self.labelHome.setFrameShape(QFrame.Box)
        self.labelHome.setFrameShadow(QFrame.Raised)
        self.labelHome.setLineWidth(4)
        self.labelHome.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHome.setObjectName("labelHome")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("home.jpg"), QIcon.Normal, QIcon.On)
        self.tabWidget.addTab(self.Home, icon1, "")


        # CAMERA TAB

        self.CameraFeed = Detection()
        self.CameraFeed.start()
        self.CameraFeed.detectionUpdate.connect(self.ImageUpdateSlot)


        self.Camera = QWidget()
        self.Camera.setStyleSheet("color: rgb(0, 0, 0);")
        self.Camera.setObjectName("Camera")
        self.widget_3 = QWidget(self.Camera)
        self.widget_3.setGeometry(QtCore.QRect(30, 20, 1311, 651))
        self.widget_3.setObjectName("widget_3")
        self.labelCameraFeed = QLabel(self.widget_3)
        self.labelCameraFeed.setGeometry(QtCore.QRect(520, 90, 781, 531))
        self.labelCameraFeed.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 100px;")
        self.labelCameraFeed.setFrameShape(QFrame.Box)
        self.labelCameraFeed.setFrameShadow(QFrame.Raised)
        self.labelCameraFeed.setLineWidth(4)
        self.labelCameraFeed.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCameraFeed.setObjectName("labelCameraFeed")
        self.btnStart = QPushButton(self.widget_3)
        self.btnStart.setGeometry(QtCore.QRect(290, 20, 101, 31))
        self.btnStart.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QPushButton(self.widget_3)
        self.btnStop.setGeometry(QtCore.QRect(400, 20, 101, 31))
        self.btnStop.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.btnStop.setObjectName("btnStop")
        self.selectCamera = QComboBox(self.widget_3)
        self.selectCamera.setGeometry(QtCore.QRect(10, 20, 261, 31))
        self.selectCamera.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.selectCamera.setPlaceholderText("")
        self.selectCamera.setObjectName("selectCamera")
        self.selectCamera.addItem("")
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(10, 410, 491, 211))
        self.label_10.setFrameShape(QFrame.Box)
        self.label_10.setFrameShadow(QFrame.Raised)
        self.label_10.setLineWidth(4)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setGeometry(QtCore.QRect(210, 430, 121, 31))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_13.setObjectName("label_13")
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setGeometry(QtCore.QRect(0, 90, 501, 311))
        self.widget_2.setObjectName("widget_2")
        self.comboBBox = QComboBox(self.widget_2)
        self.comboBBox.setEnabled(True)
        self.comboBBox.setGeometry(QtCore.QRect(410, 130, 61, 41))
        self.comboBBox.setAutoFillBackground(False)
        self.comboBBox.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.comboBBox.setObjectName("comboBBox")
        self.comboBBox.addItem("")
        self.comboBBox.addItem("")
        self.labelAPI = QLabel(self.widget_2)
        self.labelAPI.setGeometry(QtCore.QRect(40, 52, 91, 31))
        self.labelAPI.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.labelAPI.setObjectName("labelAPI")
        self.comboDetection = QComboBox(self.widget_2)
        self.comboDetection.setEnabled(True)
        self.comboDetection.setGeometry(QtCore.QRect(410, 190, 61, 41))
        self.comboDetection.setAutoFillBackground(False)
        self.comboDetection.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.comboDetection.setObjectName("comboDetection")
        self.comboDetection.addItem("")
        self.comboDetection.addItem("")
        self.apiKey = QLineEdit(self.widget_2)
        self.apiKey.setGeometry(QtCore.QRect(150, 50, 321, 41))
        self.apiKey.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.apiKey.setText("")
        self.apiKey.setObjectName("apiKey")
        self.labelBoundingBox = QLabel(self.widget_2)
        self.labelBoundingBox.setGeometry(QtCore.QRect(40, 130, 171, 31))
        self.labelBoundingBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.labelBoundingBox.setObjectName("labelBoundingBox")
        self.labelDetection = QLabel(self.widget_2)
        self.labelDetection.setGeometry(QtCore.QRect(40, 200, 131, 31))
        self.labelDetection.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.labelDetection.setObjectName("labelDetection")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 491, 311))
        self.label_9.setFrameShape(QFrame.Box)
        self.label_9.setFrameShadow(QFrame.Raised)
        self.label_9.setLineWidth(4)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_9.raise_()
        self.apiKey.raise_()
        self.labelBoundingBox.raise_()
        self.labelDetection.raise_()
        self.labelAPI.raise_()
        self.comboDetection.raise_()
        self.comboBBox.raise_()
        self.widget_2.raise_()
        self.labelCameraFeed.raise_()
        self.btnStart.raise_()
        self.btnStop.raise_()
        self.selectCamera.raise_()
        self.label_10.raise_()
        self.label_13.raise_()
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("camera.jpg"), QIcon.Normal, QIcon.On)
        self.tabWidget.addTab(self.Camera, icon2, "")


        # GALLERY TAB
        self.Gallery = QWidget()
        self.Gallery.setObjectName("Gallery")
        self.widget_4 = QWidget(self.Gallery)
        self.widget_4.setGeometry(QtCore.QRect(20, 20, 1331, 661))
        self.widget_4.setObjectName("widget_4")
        self.layoutWidget = QWidget(self.widget_4)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 350, 1271, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_17.setFrameShape(QFrame.Box)
        self.label_17.setFrameShadow(QFrame.Raised)
        self.label_17.setLineWidth(3)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_18.setFrameShape(QFrame.Box)
        self.label_18.setFrameShadow(QFrame.Raised)
        self.label_18.setLineWidth(3)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_19.setFrameShape(QFrame.Box)
        self.label_19.setFrameShadow(QFrame.Raised)
        self.label_19.setLineWidth(3)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        self.verticalScrollBar = QScrollBar(self.widget_4)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1310, 10, 21, 631))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.layoutWidget1 = QWidget(self.widget_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 1271, 261))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.layoutWidget1)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setLineWidth(3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_15.setFrameShape(QFrame.Box)
        self.label_15.setFrameShadow(QFrame.Raised)
        self.label_15.setLineWidth(3)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_14.setFrameShape(QFrame.Box)
        self.label_14.setFrameShadow(QFrame.Raised)
        self.label_14.setLineWidth(3)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("gallery.jpg"), QIcon.Normal, QIcon.On)
        self.tabWidget.addTab(self.Gallery, icon3, "")


        # SETTINGS TAB
        self.Settings = QWidget()
        self.Settings.setObjectName("Settings")
        self.tabWidget_2 = QTabWidget(self.Settings)
        self.tabWidget_2.setGeometry(QtCore.QRect(330, 100, 681, 481))
        self.tabWidget_2.setTabShape(QTabWidget.Rounded)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.btnSaveFile = QPushButton(self.tab)
        self.btnSaveFile.setGeometry(QtCore.QRect(295, 360, 93, 28))
        self.btnSaveFile.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-size: 18px")
        self.btnSaveFile.setObjectName("btnSaveFile")
        self.labelFileLocation = QLabel(self.tab)
        self.labelFileLocation.setGeometry(QtCore.QRect(50, 150, 141, 41))
        self.labelFileLocation.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"")
        self.labelFileLocation.setObjectName("labelFileLocation")
        self.btnBrowse = QToolButton(self.tab)
        self.btnBrowse.setGeometry(QtCore.QRect(510, 220, 103, 42))
        self.btnBrowse.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.btnBrowse.setObjectName("btnBrowse")
        self.lineLocation = QLineEdit(self.tab)
        self.lineLocation.setGeometry(QtCore.QRect(47, 220, 463, 41))
        self.lineLocation.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineLocation.setText("")
        self.lineLocation.setObjectName("lineLocation")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btnSaveSecurity = QPushButton(self.tab_2)
        self.btnSaveSecurity.setGeometry(QtCore.QRect(295, 360, 93, 28))
        self.btnSaveSecurity.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-size: 18px")
        self.btnSaveSecurity.setObjectName("btnSaveSecurity")
        self.lineOldUname = QLineEdit(self.tab_2)
        self.lineOldUname.setGeometry(QtCore.QRect(290, 100, 311, 41))
        self.lineOldUname.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineOldUname.setObjectName("lineOldUname")
        self.labelOldUname = QLabel(self.tab_2)
        self.labelOldUname.setGeometry(QtCore.QRect(81, 100, 151, 31))
        self.labelOldUname.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.labelOldUname.setObjectName("labelOldUname")
        self.labelNewUname = QLabel(self.tab_2)
        self.labelNewUname.setGeometry(QtCore.QRect(80, 160, 151, 31))
        self.labelNewUname.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.labelNewUname.setObjectName("labelNewUname")
        self.lineNewUname = QLineEdit(self.tab_2)
        self.lineNewUname.setGeometry(QtCore.QRect(289, 160, 311, 41))
        self.lineNewUname.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineNewUname.setObjectName("lineNewUname")
        self.labelOldPword = QLabel(self.tab_2)
        self.labelOldPword.setGeometry(QtCore.QRect(80, 220, 151, 31))
        self.labelOldPword.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.labelOldPword.setObjectName("labelOldPword")
        self.lineOldPword = QLineEdit(self.tab_2)
        self.lineOldPword.setGeometry(QtCore.QRect(289, 220, 311, 41))
        self.lineOldPword.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineOldPword.setObjectName("lineOldPword")
        self.labelNewPword = QLabel(self.tab_2)
        self.labelNewPword.setGeometry(QtCore.QRect(80, 280, 151, 31))
        self.labelNewPword.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.labelNewPword.setObjectName("labelNewPword")
        self.lineNewPword = QLineEdit(self.tab_2)
        self.lineNewPword.setGeometry(QtCore.QRect(289, 280, 311, 41))
        self.lineNewPword.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineNewPword.setObjectName("lineNewPword")
        self.tabWidget_2.addTab(self.tab_2, "")
        icon4 = QIcon()
        icon4.addPixmap(QPixmap("settings.jpg"), QIcon.Normal, QIcon.On)
        self.tabWidget.addTab(self.Settings, icon4, "")


        # HELP TAB
        self.Help = QWidget()
        self.Help.setObjectName("Help")
        self.labelHelp = QLabel(self.Help)
        self.labelHelp.setGeometry(QtCore.QRect(40, 50, 1291, 601))
        self.labelHelp.setStyleSheet("color: white;\n"
"font-size: 100px;")
        self.labelHelp.setFrameShape(QFrame.Box)
        self.labelHelp.setFrameShadow(QFrame.Raised)
        self.labelHelp.setLineWidth(4)
        self.labelHelp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHelp.setObjectName("labelHelp")
        icon5 = QIcon()
        icon5.addPixmap(QPixmap("help.jpg"), QIcon.Normal, QIcon.On)
        self.tabWidget.addTab(self.Help, icon5, "")
        

        # EXIT BUTTON
        self.btnMainExit = QPushButton(self.widget)
        self.btnMainExit.setGeometry(QtCore.QRect(1160, 12, 220, 48))
        self.btnMainExit.clicked.connect(MainWindow.close)
        self.btnMainExit.setStyleSheet("background-color: rgb(243, 243, 243);")
        icon7 = QIcon()
        icon7.addPixmap(QPixmap("exit.jpg"), QIcon.Normal, QIcon.Off)
        self.btnMainExit.setIcon(icon7)
        self.btnMainExit.setIconSize(QtCore.QSize(200, 40))
        self.btnMainExit.setCheckable(False)
        self.btnMainExit.setObjectName("btnMainExit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelHome.setText(_translate("MainWindow", "Camera Feed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("MainWindow", "Home"))
        self.labelCameraFeed.setText(_translate("MainWindow", "Camera Feed"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))
        self.selectCamera.setCurrentText(_translate("MainWindow", "Select Camera"))
        self.selectCamera.setItemText(0, _translate("MainWindow", "Select Camera"))
        self.label_13.setText(_translate("MainWindow", "Counter"))
        self.comboBBox.setItemText(0, _translate("MainWindow", "On"))
        self.comboBBox.setItemText(1, _translate("MainWindow", "Off"))
        self.labelAPI.setText(_translate("MainWindow", "API Key"))
        self.comboDetection.setItemText(0, _translate("MainWindow", "On"))
        self.comboDetection.setItemText(1, _translate("MainWindow", "Off"))
        self.labelBoundingBox.setText(_translate("MainWindow", "Bounding Box"))
        self.labelDetection.setText(_translate("MainWindow", "Detection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Camera), _translate("MainWindow", "Camera"))
        self.label_17.setText(_translate("MainWindow", "Video"))
        self.label_18.setText(_translate("MainWindow", "Video"))
        self.label_19.setText(_translate("MainWindow", "Video"))
        self.label.setText(_translate("MainWindow", "Video"))
        self.label_15.setText(_translate("MainWindow", "Video"))
        self.label_14.setText(_translate("MainWindow", "Video"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Gallery), _translate("MainWindow", "Gallery"))
        self.btnSaveFile.setText(_translate("MainWindow", "Save"))
        self.labelFileLocation.setText(_translate("MainWindow", "File Location"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "File "))
        self.btnSaveSecurity.setText(_translate("MainWindow", "Save"))
        self.labelOldUname.setText(_translate("MainWindow", "Old Username  :"))
        self.labelNewUname.setText(_translate("MainWindow", "New Username  :"))
        self.labelOldPword.setText(_translate("MainWindow", "Old Password  :"))
        self.labelNewPword.setText(_translate("MainWindow", "New Password"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Security"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Settings"))
        self.labelHelp.setText(_translate("MainWindow", "Video Tutorial"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Help), _translate("MainWindow", "Help"))
        self.btnMainExit.setText(_translate("MainWindow", "Exit"))


    def ImageUpdateSlot(self, Image):
        # self.labelHome.setPixmap(QPixmap.fromImage(Image))

        self.labelCameraFeed.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.HomeCamera.stop()
        
class HomeCamera(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1291, 601, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()
    
# new trial
class Detection(QThread):
    detectionUpdate = pyqtSignal(QImage)
    def run(self):
        seconds_to_record_after_detection = 5

        # API_KEY = "o.ASdCcRfpsLEabwyPowDFQvfGYFu0kQEY" # CJ API
        API_KEY = "o.1HTwzyZJCaj4XtW8EOLIGJI9MINcugIF"   # CHIE API

        self.ThreadActive = True
        cap = cv2.VideoCapture(0)

        pb = PushBullet(API_KEY)

        detect = 0

        # Opencv DNN
        net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
        # net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        # net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        model = cv2.dnn_DetectionModel(net)
        model.setInputParams(size=(320, 320), scale=1/255)


        # Load class lists
        classes = []
        with open("dnn_model/classes.txt", "r") as file_object:
                for class_name in file_object.readlines():
                        class_name = class_name.strip()
                        classes.append(class_name)
        print(classes)

        detection = False
        detection_stopped_time = None
        timer_started = False
        SECONDS_TO_RECORD_AFTER_DETECTION = seconds_to_record_after_detection

        frame_size = (int(cap.get(3)), int(cap.get(4)))
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")


        # used to record the time when we processed last frame
        prev_frame_time = 0

        # used to record the time at which we processed current frame
        new_frame_time = 0

        while True:
                ret, frame = cap.read()

                if ret:
                        FlippedImage = cv2.flip(frame, 1)

                        # time when we finish processing for this frame
                        new_frame_time = time.time()

                        # Calculating the fps

                        fps = 1/(new_frame_time-prev_frame_time)
                        prev_frame_time = new_frame_time

                        # converting the fps into integer
                        fps = int(fps)

                        # converting the fps to string so that we can display it on frame
                        # by using putText function
                        fps = str(fps)

                        # putting the FPS count on the frame
                        cv2.putText(frame, fps, (7, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 2, cv2.LINE_AA)
                        

                        class_id = None

                        (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)
                        for class_id, score, bbox in zip(class_ids, scores, bboxes):
                                (x, y, w, h) = bbox
                                class_name = classes[class_id]
                        #if human is detected then draw a bounding box
                        if class_id == 0:
                                cv2.putText(frame, class_name.upper(), (x, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 2)
                                cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 1)
                                cv2.putText(frame,str(round(score*100,2))+'%',(x + 100, y - 10),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 2)
                                print(class_name)
                                class_id = 1
                                if detection:
                                        timer_started = False
                                else:
                                        detection = True
                                        current_time = datetime.datetime.now().strftime("%b-%m-%Y-%H-%M-%S")
                                        detect_time = datetime.datetime.now().strftime("%I:%M %p")
                                        rec = cv2.VideoWriter(
                                        f"{current_time}.mp4", fourcc, 20, frame_size)
                                        print("Started Recording!")
                                        #push = pb.push_note(f" ALERT on {detect_time}",class_name.upper() + " DETECTED")
                                        # #send notification
                                        # with open("snapshot-{detect_time}.jpg", "rb") as pic:
                                        #     file_data = pb.upload_file(pic, "snapshot-{detect_time}.jpg")
                                        #     push = pb.push_file(**file_data)
                                #---------------------end of human detection --------------------
                                        
                                #Records and save video into mp4 file when there is a detection               
                        elif detection:
                                print(class_id)
                                print(score)
                                print(detection)
                                if timer_started:
                                        print(time.time(),detection_stopped_time, SECONDS_TO_RECORD_AFTER_DETECTION)
                                        if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                                                detection = False
                                                timer_started = False
                                                rec.release()
                                                print('Stop Recording!')
                                                #Send video to user
                                                # with open(f"{current_time}.mp4", "rb") as vid:
                                                #     file_data = pb.upload_file(vid, f"{current_time}.mp4")

                                                # push = pb.push_file(**file_data)
                        
                                else:
                                        timer_started = True
                                        detection_stopped_time = time.time()
                        if detection:
                                rec.write(frame)
      
                                #------------------end of recording----------------------------------------
    def stop(self):
        self.ThreadActive = False
        self.quit()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
