from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from pickle import TRUE
import numpy as np
import os
from os.path import expanduser
import time
import datetime
from pushbullet import PushBullet
import sys, res
import cv2
from threading import Thread
import queue
import pymysql

# Load Data from Database
con = pymysql.connect(host="localhost",user="root",password="",db="isecure")
cur = con.cursor()
cur.execute("SELECT API, Directory, Camera, RTSP FROM logindb")

for i in range (cur.rowcount):
        data = cur.fetchall()

        for row in data:
                api = str(row[0])
                directory = str(row[1])
                cam = str(row[2])
                rtspCam = str(row[3])


# rtsp = "rtsp://192.168.86.234/live/ch00_0"
if int(cam) == 2:
    print(rtspCam)
    vid = cv2.VideoCapture(rtspCam)
else:
    print(cam)
    vid = cv2.VideoCapture(int(cam))

# vid = cv2.VideoCapture(0)

frame_queue = queue.Queue()

video_name = None  


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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 804)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/image/logo.jpg"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(30, 20, 1391, 781))
        self.widget.setObjectName("widget")
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setGeometry(QRect(10, 10, 1371, 751))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(47, 47, 47);")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(201, 40))
        self.tabWidget.setElideMode(Qt.ElideLeft)
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
        self.labelHome.setGeometry(QRect(40, 50, 1291, 601))
        self.labelHome.setStyleSheet("color: white;\n"
"font-size: 100px;\n"
"")
        self.labelHome.setFrameShape(QFrame.Box)
        self.labelHome.setFrameShadow(QFrame.Raised)
        self.labelHome.setLineWidth(4)
        self.labelHome.setAlignment(Qt.AlignCenter)
        self.labelHome.setObjectName("labelHome")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("home.jpg"), QIcon.Normal, QIcon.On)
        self.tabWidget.addTab(self.Home, icon1, "")


        # CAMERA TAB

        self.Camera = QWidget()
        self.Camera.setStyleSheet("color: rgb(0, 0, 0);")
        self.Camera.setObjectName("Camera")
        self.widget_3 = QWidget(self.Camera)
        self.widget_3.setGeometry(QRect(30, 20, 1311, 651))
        self.widget_3.setObjectName("widget_3")
        self.labelCameraFeed = QLabel(self.widget_3)
        self.labelCameraFeed.setGeometry(QRect(520, 90, 781, 531))
        self.labelCameraFeed.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 100px;")
        self.labelCameraFeed.setFrameShape(QFrame.Box)
        self.labelCameraFeed.setFrameShadow(QFrame.Raised)
        self.labelCameraFeed.setLineWidth(4)
        self.labelCameraFeed.setAlignment(Qt.AlignCenter)
        self.labelCameraFeed.setObjectName("labelCameraFeed")
        self.btnStart = QPushButton(self.widget_3)
        self.btnStart.setEnabled(True)
        self.btnStart.clicked.connect(self.CameraStart)
        self.btnStart.setGeometry(QRect(290, 20, 101, 31))
        self.btnStart.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QPushButton(self.widget_3)
        self.btnStop.setEnabled(False)
        self.btnStop.clicked.connect(self.CancelFeed)

        self.btnStop.setGeometry(QRect(400, 20, 101, 31))
        self.btnStop.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.btnStop.setObjectName("btnStop")
        self.selectCamera = QComboBox(self.widget_3)
        self.selectCamera.addItem("Camera 1", 0)
        self.selectCamera.addItem("Camera 2", 1)
        self.selectCamera.addItem("IP Camera", 2)
        self.selectCamera.setCurrentIndex(int(cam))
        self.selectCamera.setEnabled(True)
        self.selectCamera.setObjectName(u"selectCamera")
        self.selectCamera.setGeometry(QRect(10, 20, 261, 31))
        self.selectCamera.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setGeometry(QRect(10, 410, 491, 211))
        self.label_10.setFrameShape(QFrame.Box)
        self.label_10.setFrameShadow(QFrame.Raised)
        self.label_10.setLineWidth(4)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setGeometry(QRect(205, 430, 121, 31))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_13.setObjectName("label_13")
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setGeometry(QRect(0, 90, 501, 311))
        self.widget_2.setObjectName("widget_2")
        self.comboBBox = QComboBox(self.widget_2)
        self.comboBBox.setEnabled(False)
        self.comboBBox.setGeometry(QRect(410, 130, 61, 41))
        self.comboBBox.setAutoFillBackground(False)
        self.comboBBox.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.comboBBox.setObjectName("comboBBox")
        self.comboBBox.addItem("Off", 0)
        self.comboBBox.addItem("On", 1)
        self.labelAPI = QLabel(self.widget_2)
        self.labelAPI.setGeometry(QRect(40, 52, 91, 31))
        self.labelAPI.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.labelAPI.setObjectName("labelAPI")
        self.comboDetection = QComboBox(self.widget_2)
        self.comboDetection.setEnabled(False)
        self.comboDetection.setGeometry(QRect(410, 190, 61, 41))
        self.comboDetection.setAutoFillBackground(False)
        self.comboDetection.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.comboDetection.setObjectName("comboDetection")
        self.comboDetection.addItem("Off", 0)
        self.comboDetection.addItem("On", 1)
        self.apiKey = QLineEdit(self.widget_2)
        self.apiKey.setEnabled(False)
        self.apiKey.setGeometry(QRect(150, 50, 321, 41))
        self.apiKey.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.apiKey.setText("")
        self.apiKey.setObjectName("apiKey")
        self.labelBoundingBox = QLabel(self.widget_2)
        self.labelBoundingBox.setGeometry(QRect(40, 130, 171, 31))
        self.labelBoundingBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.labelBoundingBox.setObjectName("labelBoundingBox")
        self.labelDetection = QLabel(self.widget_2)
        self.labelDetection.setGeometry(QRect(40, 200, 131, 31))
        self.labelDetection.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.labelDetection.setObjectName("labelDetection")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setGeometry(QRect(10, 0, 491, 311))
        self.label_9.setFrameShape(QFrame.Box)
        self.label_9.setFrameShadow(QFrame.Raised)
        self.label_9.setLineWidth(4)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_9.raise_()
        self.btnCamSave = QPushButton(self.widget_2)
        self.btnCamSave.setEnabled(False)
        self.btnCamSave.clicked.connect(self.buttonCameraSave)
        self.btnCamSave.setGeometry(QRect(210, 260, 101, 31))
        self.btnCamSave.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.btnCamSave.setObjectName("btnCamSave")
        self.rtspLink = QLineEdit(self.widget_3)
        self.rtspLink.setObjectName("rtspLink")
        self.rtspLink.setGeometry(QRect(40, 490, 431, 41))
        self.rtspLink.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.rtspSave = QPushButton(self.widget_3)
        self.rtspSave.clicked.connect(self.rtspCamStart)
        self.rtspSave.setObjectName("rtspSave")
        self.rtspSave.setEnabled(True)
        self.rtspSave.setGeometry(QRect(210, 560, 101, 31))
        self.rtspSave.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.btnCamSave.raise_()
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
        self.rtspLink.raise_()
        self.rtspSave.raise_()
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("camera.jpg"), QIcon.Normal, QIcon.On)
        self.tabWidget.addTab(self.Camera, icon2, "")



        # SETTINGS TAB
        self.Settings = QWidget()
        self.Settings.setObjectName("Settings")
        self.tabWidget_2 = QTabWidget(self.Settings)
        self.tabWidget_2.setGeometry(QRect(330, 100, 681, 481))
        self.tabWidget_2.setTabShape(QTabWidget.Rounded)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.btnSaveFile = QPushButton(self.tab)
        self.btnSaveFile.clicked.connect(self.buttonSaveDirectory)
        self.btnSaveFile.setEnabled(False)
        self.btnSaveFile.setGeometry(QRect(295, 360, 93, 28))
        self.btnSaveFile.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-size: 18px")
        self.btnSaveFile.setObjectName("btnSaveFile")
        self.labelFileLocation = QLabel(self.tab)
        self.labelFileLocation.setGeometry(QRect(50, 150, 141, 41))
        self.labelFileLocation.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"")
        self.labelFileLocation.setObjectName("labelFileLocation")
        self.btnBrowse = QToolButton(self.tab)
        self.btnBrowse.clicked.connect(self.buttonBrowse)
        self.btnBrowse.setGeometry(QRect(510, 220, 103, 42))
        self.btnBrowse.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.btnBrowse.setObjectName("btnBrowse")
        self.lineLocation = QLineEdit(self.tab)
        self.lineLocation.setEnabled(False)
        self.lineLocation.setGeometry(QRect(47, 220, 463, 41))
        self.lineLocation.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineLocation.setText("")
        self.lineLocation.setObjectName("lineLocation")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btnSaveSecurity = QPushButton(self.tab_2)
        self.btnSaveSecurity.clicked.connect(self.buttonSaveSecurity)
        self.btnSaveSecurity.setGeometry(QRect(295, 360, 93, 28))
        self.btnSaveSecurity.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-size: 18px")
        self.btnSaveSecurity.setObjectName("btnSaveSecurity")
        self.lineOldUname = QLineEdit(self.tab_2)
        self.lineOldUname.setGeometry(QRect(290, 100, 311, 41))
        self.lineOldUname.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineOldUname.setObjectName("lineOldUname")
        self.labelOldUname = QLabel(self.tab_2)
        self.labelOldUname.setGeometry(QRect(81, 100, 151, 31))
        self.labelOldUname.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.labelOldUname.setObjectName("labelOldUname")
        self.labelOldPword = QLabel(self.tab_2)
        self.labelOldPword.setGeometry(QRect(80, 160, 151, 31))
        self.labelOldPword.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.labelOldPword.setObjectName("labelOldPword")
        self.lineOldPword = QLineEdit(self.tab_2)
        self.lineOldPword.setEchoMode(QLineEdit.Password)
        self.lineOldPword.setGeometry(QRect(289, 160, 311, 41))
        self.lineOldPword.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineOldPword.setObjectName("lineOldPword")
        self.labelNewUname = QLabel(self.tab_2)
        self.labelNewUname.setGeometry(QRect(80, 220, 151, 31))
        self.labelNewUname.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.labelNewUname.setObjectName("labelNewUname")
        self.lineNewUname = QLineEdit(self.tab_2)
        self.lineNewUname.setGeometry(QRect(289, 220, 311, 41))
        self.lineNewUname.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineNewUname.setObjectName("lineNewUname")
        self.labelNewPword = QLabel(self.tab_2)
        self.labelNewPword.setGeometry(QRect(80, 280, 151, 31))
        self.labelNewPword.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.labelNewPword.setObjectName("labelNewPword")
        self.lineNewPword = QLineEdit(self.tab_2)
        self.lineNewPword.setEchoMode(QLineEdit.Password)
        self.lineNewPword.setGeometry(QRect(289, 280, 311, 41))
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
        
        # for video player
        self.labelHelp = QLabel(self.Help)
        self.labelHelp.setGeometry(QRect(40, 50, 1291, 551))
        self.labelHelp.setStyleSheet("color: white;\n"
"font-size: 100px;")
        self.labelHelp.setFrameShape(QFrame.Box)
        self.labelHelp.setFrameShadow(QFrame.Raised)
        self.labelHelp.setLineWidth(4)
        self.labelHelp.setAlignment(Qt.AlignCenter)
        self.labelHelp.setObjectName("labelHelp")
        self.horizontalSlider = QSlider(self.Help)
        self.horizontalSlider.setGeometry(QRect(160, 630, 1161, 31))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setRange(0, 0)
        self.horizontalSlider.sliderMoved.connect(self.setPosition)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.playButton = QPushButton(self.Help)
        self.playButton.clicked.connect(self.videoTutorial)
        self.playButton.setGeometry(QRect(50, 620, 91, 51))
        self.playButton.setStyleSheet("border-radius: 15px;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(237, 237, 237);\n"
"")
        self.playButton.setObjectName("playButton")

        self.tutorialWidget = QWidget(self.Help)
        self.tutorialWidget.setGeometry(QRect(50, 60, 1271, 531))
        self.tutorialWidget.setObjectName("tutorialWidget")
        
        # Video 
        videoWidget = QVideoWidget(self.tutorialWidget)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("Dangerously.mp4"))) 

        Layout = QHBoxLayout(self.tutorialWidget)
        Layout.setContentsMargins(10, 10, 10, 10)
        Layout.addWidget(videoWidget)

        self.tutorialWidget.setLayout(Layout)

        self.mediaPlayer.setVideoOutput(videoWidget)

        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

        icon5 = QIcon()
        icon5.addPixmap(QPixmap("help.jpg"), QIcon.Normal, QIcon.On)
        self.tabWidget.addTab(self.Help, icon5, "")
        self.mediaPlayer.pause()
        

        # EXIT BUTTON
        self.btnMainExit = QPushButton(self.widget)
        self.btnMainExit.setGeometry(QRect(1100, 12, 278, 48))
        self.btnMainExit.clicked.connect(MainWindow.close)
        self.btnMainExit.setStyleSheet("background-color: rgb(243, 243, 243);")
        icon7 = QIcon()
        icon7.addPixmap(QPixmap("exit.jpg"), QIcon.Normal, QIcon.Off)
        self.btnMainExit.setIcon(icon7)
        self.btnMainExit.setIconSize(QSize(200, 40))
        self.btnMainExit.setCheckable(False)
        self.btnMainExit.setObjectName("btnMainExit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelHome.setText(_translate("MainWindow", "Camera Feed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("MainWindow", "Home"))
        self.labelCameraFeed.setText(_translate("MainWindow", "Camera Feed"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))
        self.selectCamera.setCurrentText(_translate("MainWindow", "Select Camera"))
        self.selectCamera.setItemText(0, _translate("MainWindow", "Camera 1"))
        self.label_13.setText(_translate("MainWindow", "RTSP Link"))
        self.rtspSave.setText(_translate("MainWindow", "Save"))
        self.comboBBox.setItemText(0, _translate("MainWindow", "Off"))
        self.comboBBox.setItemText(1, _translate("MainWindow", "On"))
        self.labelAPI.setText(_translate("MainWindow", "API Key"))
        self.comboDetection.setItemText(0, _translate("MainWindow", "Off"))
        self.comboDetection.setItemText(1, _translate("MainWindow", "On"))
        self.labelBoundingBox.setText(_translate("MainWindow", "Bounding Box"))
        self.labelDetection.setText(_translate("MainWindow", "Detection"))
        self.btnCamSave.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Camera), _translate("MainWindow", "Camera"))
        self.btnSaveFile.setText(_translate("MainWindow", "Save"))
        self.labelFileLocation.setText(_translate("MainWindow", "File Location"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "File "))
        self.btnSaveSecurity.setText(_translate("MainWindow", "Save"))
        self.labelOldUname.setText(_translate("MainWindow", "Old Username  :"))
        self.labelOldPword.setText(_translate("MainWindow", "Old Password  :"))
        self.labelNewUname.setText(_translate("MainWindow", "New Username  :"))
        self.labelNewPword.setText(_translate("MainWindow", "New Password  :"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Security"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Settings"))
        self.labelHelp.setText(_translate("MainWindow", "Video Tutorial"))
        self.playButton.setText(_translate("MainWindow", "Play / Pause"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Help), _translate("MainWindow", "Help"))
        self.btnMainExit.setText(_translate("MainWindow", "Exit"))


    def ImageUpdateSlot(self, Image):
        self.labelHome.setPixmap(QPixmap.fromImage(Image))
        self.labelHome.setScaledContents(True)
        
    def rtspCamStart(self):
        rtsp = self.rtspLink.text()
        con = pymysql.connect(host="localhost",user="root",password="",db="isecure")
        cur = con.cursor()
        sql = "UPDATE logindb SET RTSP = '"+rtsp+"'"

        if rtsp != "":
           cur.execute(sql)
           con.commit()
           cur.close()
           con.close()
           self.rtspSave.setEnabled(False)
           self.rtspLink.setEnabled(False)

    def CameraStart(self):
        con = pymysql.connect(host="localhost",user="root",password="",db="isecure")
        cur = con.cursor()
        sql = "UPDATE logindb SET Camera = '"+str(self.selectCamera.currentData())+"'"
        if self.selectCamera.currentData() == 0:
            cur.execute(sql)
            con.commit()
            cur.close()
            con.close()
            if self.selectCamera.currentData() != int(cam):
                self.alert("Alert", "Camera Changed... Restart the system...")
                MainWindow.close()

        elif self.selectCamera.currentData() == 1:
            cur.execute(sql)
            con.commit()
            cur.close()
            con.close()
            if self.selectCamera.currentData() != int(cam):
                self.alert("Alert", "Camera Changed... Restart the system...")
                MainWindow.close()

        elif self.selectCamera.currentData() == 2:
            cur.execute(sql)
            con.commit()
            cur.close()
            con.close()
            if self.selectCamera.currentData() != int(cam):
                self.alert("Alert", "Camera Changed... Restart the system...")
                MainWindow.close()

        self.rtspLink.setEnabled(False)
        self.rtspSave.setEnabled(False)
        self.selectCamera.setEnabled(False)
        self.btnStart.setEnabled(False)
        self.btnStop.setEnabled(True)
        self.comboDetection.setEnabled(True)
        self.comboBBox.setEnabled(True)
        self.apiKey.setEnabled(True)
        self.btnCamSave.setEnabled(True)
        self.CamStart = HomeCamera()
        self.CamStart.start()
        self.CamStart.ImageUpdate.connect(self.startCamera)
        
    def startCamera(self, Image):
        self.labelCameraFeed.setPixmap(QPixmap.fromImage(Image))
        self.labelCameraFeed.setScaledContents(True)     

    def CancelFeed(self):
        self.labelCameraFeed.setPixmap(QPixmap("camera.jpg"))
        self.labelCameraFeed.setScaledContents(True)
        
        self.rtspLink.setEnabled(True)
        self.rtspSave.setEnabled(True)
        self.selectCamera.setEnabled(True)
        self.btnStart.setEnabled(True)
        self.btnStop.setEnabled(False)
        self.comboDetection.setEnabled(False)
        self.comboBBox.setEnabled(False)
        self.apiKey.setEnabled(False)
        self.CamStart.stop()
        self.HomeCamera = HomeCamera()
        self.HomeCamera.start()
        self.HomeCamera.ImageUpdate.connect(self.ImageUpdateSlot)

    def videoTutorial(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def positionChanged(self, position):
        self.horizontalSlider.setValue(position)

    def durationChanged(self, duration):
        self.horizontalSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def buttonCameraSave(self):
        apikey = self.apiKey.text()
        con = pymysql.connect(host="localhost",user="root",password="",db="isecure")
        cur = con.cursor()
        sql = "UPDATE logindb SET API = '"+apikey+"'"

        if apikey != "":
           cur.execute(sql)
           con.commit()
           cur.close()
           con.close()

        elif self.comboBBox.currentData() == 0 and self.comboDetection.currentData() == 0:
           self.CamStart.stop()
           self.CamStart = HomeCamera()
           self.CamStart.start()
           self.CamStart.ImageUpdate.connect(self.startCamera)

        elif self.comboBBox.currentData() == 1 and self.comboDetection.currentData() == 0:
           self.CamStart.stop()
           self.CamStart = BoundingBox()
           self.CamStart.start()
           self.CamStart.ImageUpdate.connect(self.startCamera)

        elif self.comboBBox.currentData() == 0 and self.comboDetection.currentData() == 1:
           self.CamStart.stop()
           self.CamStart = Detection()
           self.CamStart.start()
           self.CamStart.ImageUpdate.connect(self.startCamera)

        elif self.comboBBox.currentData() == 1 and self.comboDetection.currentData() == 1:
           self.CamStart.stop()
           self.CamStart = BoxedDetection()
           self.CamStart.start()
           self.CamStart.ImageUpdate.connect(self.startCamera)

    def buttonBrowse(self):
        input_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        self.lineLocation.setText(input_dir)
        
        if input_dir == "":
            self.btnSaveFile.setEnabled(False)

        else:
            self.btnSaveFile.setEnabled(True)
            self.lineLocation.setEnabled(True)
            
    def buttonSaveDirectory(self):
        dir = self.lineLocation.text()
        con = pymysql.connect(host="localhost",user="root",password="",db="isecure")
        cur = con.cursor()
        sql = "UPDATE logindb SET Directory = '"+dir+"'"
        self.alert("Alert", "Directory changed")
        cur.execute(sql)
        con.commit()
        cur.close()
        con.close()
        self.btnSaveFile.setEnabled(False)
        self.lineLocation.setEnabled(False)

    def buttonSaveSecurity(self):
        username = self.lineOldUname.text()
        password= self.lineOldPword.text()
        newUname = self.lineNewUname.text()
        newPword = self.lineNewPword.text()
        con = pymysql.connect(host="localhost",user="root",password="",db="isecure")
        cur = con.cursor()
        query = "SELECT * FROM logindb WHERE username = %s AND password = %s"
        data = cur.execute(query,(username,password))
        if (len(cur.fetchall())>0):
            con = pymysql.connect(host="localhost",user="root",password="",db="isecure")
            cur = con.cursor()
            sql = "UPDATE logindb SET Username = '"+newUname+"', Password = '"+newPword+"'"
            self.alert("Alert", "Update Success... Restarting the System")
            cur.execute(sql)
            con.commit()
            cur.close()
            con.close()
            sys.exit()
                
        else:
            self.alert("Alert", "Username and password Does not match")
                         

    def alert(self, title, message):
        text = QMessageBox()
        text.setWindowTitle(title)
        text.setText(message)
        text.setStandardButtons(QMessageBox.Ok)
        text.exec()



class HomeCamera(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        while self.ThreadActive:
            ret, frame = vid.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1291, 601, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()  
       
        
class Detection(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        # API_KEY = "o.NgkjKngSaV9sBaxAZPHo2W00pIg0jqrf"   # CJ API
        # API_KEY = "o.1HTwzyZJCaj4XtW8EOLIGJI9MINcugIF"   # CHIE API
        API_KEY = str(api)

        pb = PushBullet(API_KEY)

        frame_size = (int(vid.get(3)), int(vid.get(4)))
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        
        detection = False
        detection_stopped_time = None
        timer_started = False
        SECONDS_TO_RECORD_AFTER_DETECTION = 5
        

        self.ThreadActive = True

        def send_notification():
            while True:
                # get the next frame from the queue
                frame = frame_queue.get()
                if os.path.exists(snapshot_path):
                    # upload the image file
                    with open(snapshot_path, "rb") as pic:
                        file_data = pb.upload_file(pic, f"snapshot-{detect_time}.jpg")
                        push = pb.push_file(**file_data)
                        print("Notification sent to user")

                # sleep for a short time before checking again
                time.sleep(0.1)

        # start the notification thread
        notification_thread = Thread(target=send_notification)
        notification_thread.start()

        

        while self.ThreadActive:
            QtWidgets.QApplication.processEvents()
            ret, frame = vid.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1291, 601, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

                try:
                    class_id = None
                    (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)
                    for class_id, score, bbox in zip(class_ids, scores, bboxes):
                        (x, y, w, h) = bbox
                        class_name = classes[class_id]
                    #if human is detected then draw a bounding box
                    if class_id == 0:
                        print(class_name)
                        class_id = 1
                        if detection:
                            timer_started = False
                        else:
                            detection = True
                            current_time = datetime.datetime.now().strftime("%b-%d-%Y-%H-%M-%S")
                            detect_time = datetime.datetime.now().strftime("%I:%M %p")
                            img_name = 'Snapshot '+ str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'
                            snapshot = './snapshots/'
                            snapshot_path = os.path.join(snapshot, img_name)
                            cv2.imwrite(snapshot_path, frame)
                            print("Snapshot Taken")
                            push = pb.push_note(f" ALERT on {detect_time}",class_name.upper() + " DETECTED")
                            rec = cv2.VideoWriter(
                                f"{directory+'/'}{current_time}.mp4", fourcc, 10, frame_size)
                            print("Started Recording!")
                            frame_queue.put(FlippedImage)
                            
                            # #---------------------end of human detection --------------------
                        
                #Records and save video into mp4 file when there is a detection               
                    elif detection:
                        if timer_started:
                            print(int(SECONDS_TO_RECORD_AFTER_DETECTION - (time.time() - detection_stopped_time)))
                            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                                detection = False
                                timer_started = False
                                rec.release()
                                print('Stop Recording!')
                                #Send video to user
                                with open(f"{current_time}.mp4", "rb") as video:
                                    file_data = pb.upload_file(video, f"{current_time}.mp4")
                                push = pb.push_file(**file_data)
                                
                        else:
                            timer_started = True
                            detection_stopped_time = time.time()

                    if detection:
                        rec.write(frame)
                #------------------end of recording----------------------------------------

                except Exception as e:
                    pass

                # Convert the image back to the original format and emit the signal
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1291, 601, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

                
    def stop(self):

        self.ThreadActive = False
        self.quit()


class BoundingBox(QThread):
    ImageUpdate = pyqtSignal(QImage)
    
    def run(self):
        self.ThreadActive = True
        while self.ThreadActive:
            QtWidgets.QApplication.processEvents()
            ret, frame = vid.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1291, 601, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

                try:
                    class_id = None
                    (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)
                    for class_id, score, bbox in zip(class_ids, scores, bboxes):
                        (x, y, w, h) = bbox
                        class_name = classes[class_id]
                    #if human is detected then draw a bounding box
                    if class_id == 0:
                        (img_h, img_w) = FlippedImage.shape[:2]
                        xFlip = img_w - x - w
                        cv2.rectangle(FlippedImage, (xFlip, y), (xFlip + w, y + h), (0,255,0), 1)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 1)
                        cv2.putText(FlippedImage, class_name.upper(), (xFlip, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 2)
                        cv2.putText(frame, class_name.upper(), (x, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 2)
                        cv2.putText(FlippedImage,str(round(score*100,2))+'%',(xFlip + 100, y - 10),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 2)
                        cv2.putText(frame,str(round(score*100,2))+'%',(x + 100, y - 10),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 2)
                        print(class_name)
                        class_id = 1

                except Exception as e:
                    pass

                # Convert the image back to the original format and emit the signal
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1291, 601, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
                
    def stop(self):
        self.ThreadActive = False
        self.quit()


class BoxedDetection(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        # API_KEY = "o.NgkjKngSaV9sBaxAZPHo2W00pIg0jqrf"   # CJ API
        # API_KEY = "o.1HTwzyZJCaj4XtW8EOLIGJI9MINcugIF"   # CHIE API
        API_KEY = str(api)

        pb = PushBullet(API_KEY)

        frame_size = (int(vid.get(3)), int(vid.get(4)))
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        
        detection = False
        detection_stopped_time = None
        timer_started = False
        SECONDS_TO_RECORD_AFTER_DETECTION = 5
        

        self.ThreadActive = True

        def send_notification():
            while True:
                # get the next frame from the queue
                frame = frame_queue.get()
                if os.path.exists(snapshot_path):
                    # upload the image file
                    with open(snapshot_path, "rb") as pic:
                        file_data = pb.upload_file(pic, f"snapshot-{detect_time}.jpg")
                        push = pb.push_file(**file_data)
                        print("Notification sent to user")

                # sleep for a short time before checking again
                time.sleep(0.1)

        # start the notification thread
        notification_thread = Thread(target=send_notification)
        notification_thread.start()

        

        while self.ThreadActive:
            QtWidgets.QApplication.processEvents()
            ret, frame = vid.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1291, 601, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

                try:
                    class_id = None
                    (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)
                    for class_id, score, bbox in zip(class_ids, scores, bboxes):
                        (x, y, w, h) = bbox
                        class_name = classes[class_id]
                    #if human is detected then draw a bounding box
                    if class_id == 0:
                        (img_h, img_w) = FlippedImage.shape[:2]
                        xFlip = img_w - x - w
                        cv2.rectangle(FlippedImage, (xFlip, y), (xFlip + w, y + h), (0,255,0), 1)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 1)
                        cv2.putText(FlippedImage, class_name.upper(), (xFlip, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 2)
                        cv2.putText(frame, class_name.upper(), (x, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 2)
                        cv2.putText(FlippedImage,str(round(score*100,2))+'%',(xFlip + 100, y - 10),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 2)
                        cv2.putText(frame,str(round(score*100,2))+'%',(x + 100, y - 10),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 2)
                        print(class_name)
                        class_id = 1
                        if detection:
                            timer_started = False
                        else:
                            detection = True
                            current_time = datetime.datetime.now().strftime("%b-%d-%Y-%H-%M-%S")
                            detect_time = datetime.datetime.now().strftime("%I:%M %p")
                            img_name = 'Snapshot '+ str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'
                            snapshot = './snapshots/'
                            snapshot_path = os.path.join(snapshot, img_name)
                            cv2.imwrite(snapshot_path, frame)
                            print("Snapshot Taken")
                            push = pb.push_note(f" ALERT on {detect_time}",class_name.upper() + " DETECTED")
                            rec = cv2.VideoWriter(
                                f"{directory+'/'}{current_time}.mp4", fourcc, 10, frame_size)
                            print("Started Recording!")
                            frame_queue.put(FlippedImage)
                            
                            # #---------------------end of human detection --------------------
                        
                #Records and save video into mp4 file when there is a detection               
                    elif detection:
                        if timer_started:
                            print(int(SECONDS_TO_RECORD_AFTER_DETECTION - (time.time() - detection_stopped_time)))
                            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                                detection = False
                                timer_started = False
                                rec.release()
                                print('Stop Recording!')
                                #Send video to user
                                with open(f"{directory+'/'}{current_time}.mp4", "rb") as video:
                                    file_data = pb.upload_file(video, f"{current_time}.mp4")
                                push = pb.push_file(**file_data)
                                
                        else:
                            timer_started = True
                            detection_stopped_time = time.time()

                    if detection:
                        rec.write(frame)
                #------------------end of recording----------------------------------------

                except Exception as e:
                    pass

                # Convert the image back to the original format and emit the signal
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1291, 601, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

                
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