from PyQt5 import QtCore, QtGui, QtWidgets
from WindowGUI2 import Ui_MainWindow
import sys, res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 804)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 1391, 781))
        self.widget.setObjectName("widget")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1371, 751))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(47, 47, 47);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(159, 40))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        
        # HOME
        self.Home = QtWidgets.QWidget()
        self.Home.setStyleSheet("background-color: rgb(47, 47, 47);\n""")
        self.Home.setObjectName("Home")
        self.HomeLabel = QtWidgets.QLabel(self.Home)
        self.HomeLabel.setGeometry(QtCore.QRect(30, 30, 1311, 641))
        self.HomeLabel.setStyleSheet("color: white;\n"
"font-size: 100px;\n"
"")
        self.HomeLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.HomeLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HomeLabel.setLineWidth(4)
        self.HomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HomeLabel.setObjectName("HomeLabel")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("home.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.Home, icon1, "")


        # CAMERA
        self.Camera = QtWidgets.QWidget()
        self.Camera.setStyleSheet("color: rgb(0, 0, 0);")
        self.Camera.setObjectName("Camera")
        self.widget_3 = QtWidgets.QWidget(self.Camera)
        self.widget_3.setGeometry(QtCore.QRect(30, 20, 1311, 651))
        self.widget_3.setObjectName("widget_3")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(520, 90, 781, 531))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 100px;")
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_8.setLineWidth(4)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 20, 101, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 20, 101, 31))
        self.pushButton_5.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox = QtWidgets.QComboBox(self.widget_3)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 261, 31))
        self.comboBox.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.comboBox.setPlaceholderText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(10, 410, 491, 211))
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_10.setLineWidth(4)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.widget_3)
        self.label_13.setGeometry(QtCore.QRect(210, 430, 121, 31))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_13.setObjectName("label_13")
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setGeometry(QtCore.QRect(0, 90, 501, 311))
        self.widget_2.setObjectName("widget_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setGeometry(QtCore.QRect(410, 130, 61, 41))
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(40, 52, 91, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label.setObjectName("label")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_3.setEnabled(True)
        self.comboBox_3.setGeometry(QtCore.QRect(410, 190, 61, 41))
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 50, 321, 41))
        self.lineEdit_5.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setGeometry(QtCore.QRect(40, 130, 171, 31))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(40, 200, 131, 31))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 491, 311))
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_9.setLineWidth(4)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_9.raise_()
        self.lineEdit_5.raise_()
        self.label_12.raise_()
        self.label_11.raise_()
        self.label.raise_()
        self.comboBox_3.raise_()
        self.comboBox_2.raise_()
        self.widget_2.raise_()
        self.label_8.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.comboBox.raise_()
        self.label_10.raise_()
        self.label_13.raise_()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("camera.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.Camera, icon2, "")


        # GALLERY
        self.Gallery = QtWidgets.QWidget()
        self.Gallery.setObjectName("Gallery")
        self.widget_4 = QtWidgets.QWidget(self.Gallery)
        self.widget_4.setGeometry(QtCore.QRect(20, 20, 1331, 661))
        self.widget_4.setObjectName("widget_4")
        self.layoutWidget = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 350, 1291, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_17.setFrameShape(QtWidgets.QFrame.Box)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_17.setLineWidth(3)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_18.setFrameShape(QtWidgets.QFrame.Box)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_18.setLineWidth(3)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_19.setFrameShape(QtWidgets.QFrame.Box)
        self.label_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_19.setLineWidth(3)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.widget_4)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1310, 10, 21, 631))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.widget1 = QtWidgets.QWidget(self.widget_4)
        self.widget1.setGeometry(QtCore.QRect(20, 30, 1271, 261))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_16 = QtWidgets.QLabel(self.widget1)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_16.setFrameShape(QtWidgets.QFrame.Box)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_16.setLineWidth(3)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.label_15 = QtWidgets.QLabel(self.widget1)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_15.setLineWidth(3)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.label_14 = QtWidgets.QLabel(self.widget1)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25px;")
        self.label_14.setFrameShape(QtWidgets.QFrame.Box)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_14.setLineWidth(3)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("gallery.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.Gallery, icon3, "")


        # SETTINGS
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.Settings)
        self.tabWidget_2.setGeometry(QtCore.QRect(330, 100, 681, 481))
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(295, 360, 93, 28))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-size: 18px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 141, 41))
        self.label_3.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"")
        self.label_3.setObjectName("label_3")
        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.toolButton.setGeometry(QtCore.QRect(510, 220, 103, 42))
        self.toolButton.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font-size: 18px")
        self.toolButton.setObjectName("toolButton")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(47, 220, 463, 41))
        self.lineEdit_6.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(295, 360, 93, 28))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-size: 18px")
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(290, 100, 311, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 160, 311, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 220, 311, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 280, 311, 41))
        self.lineEdit_4.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 18px")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(81, 100, 151, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(79, 160, 151, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(81, 220, 151, 31))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(80, 280, 151, 31))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.label_7.setObjectName("label_7")
        self.tabWidget_2.addTab(self.tab_2, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("settings.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.Settings, icon4, "")


        # HELP
        self.Help = QtWidgets.QWidget()
        self.Help.setObjectName("Help")
        self.label_2 = QtWidgets.QLabel(self.Help)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 1291, 601))
        self.label_2.setStyleSheet("color: white;\n"
"font-size: 100px;")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setLineWidth(4)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("help.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.Help, icon5, "")

        
        # EXIT 
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(1160, 12, 220, 48))
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton.setStyleSheet("background-color: rgb(243, 243, 243);")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("exit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QtCore.QSize(200, 40))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.HomeLabel.setText(_translate("MainWindow", "Camera Feed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("MainWindow", "Home"))
        self.label_8.setText(_translate("MainWindow", "Camera Feed"))
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.pushButton_5.setText(_translate("MainWindow", "Stop"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Select Camera"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select Camera"))
        self.label_13.setText(_translate("MainWindow", "Counter"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "On"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Off"))
        self.label.setText(_translate("MainWindow", "API Key"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "On"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Off"))
        self.label_12.setText(_translate("MainWindow", "Bounding Box"))
        self.label_11.setText(_translate("MainWindow", "Detection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Camera), _translate("MainWindow", "Camera"))
        self.label_17.setText(_translate("MainWindow", "Video"))
        self.label_18.setText(_translate("MainWindow", "Video"))
        self.label_19.setText(_translate("MainWindow", "Video"))
        self.label_16.setText(_translate("MainWindow", "Video"))
        self.label_15.setText(_translate("MainWindow", "Video"))
        self.label_14.setText(_translate("MainWindow", "Video"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Gallery), _translate("MainWindow", "Gallery"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.label_3.setText(_translate("MainWindow", "File Location"))
        self.toolButton.setText(_translate("MainWindow", "Browse"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "File "))
        self.pushButton_6.setText(_translate("MainWindow", "Save"))
        self.label_4.setText(_translate("MainWindow", "Old Username  :"))
        self.label_5.setText(_translate("MainWindow", "New Username :"))
        self.label_6.setText(_translate("MainWindow", "Old Password   :"))
        self.label_7.setText(_translate("MainWindow", "New Password  :"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Security"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Settings"))
        self.label_2.setText(_translate("MainWindow", "Video Tutorial"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Help), _translate("MainWindow", "Help"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.Exit), _translate("MainWindow", "Exit"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
