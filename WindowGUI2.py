from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys, res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 657)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 1080, 640))
        self.widget.setStyleSheet("background-color: rgba(47, 47, 47);\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1080, 40))
        self.label.setStyleSheet("background-color:rgb(127, 127, 129)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.home = QtWidgets.QPushButton(self.widget)
        self.home.setGeometry(QtCore.QRect(0, 0, 150, 40))
        self.home.setStyleSheet("QPushButton#home{\n"
"    image: url(:/image/home.jpg);\n"
"    background-color: rgba(127, 127, 129,255);\n"
"}\n"
"\n"
"QPushButton#home:hover{\n"
"    background-color: rgba(159, 159, 162, 255);\n"
"}\n"
"\n"
"QPushButton#home:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(127, 127, 129,255);\n"
"}")
        self.home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("home.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home.setIcon(icon)
        self.home.setIconSize(QtCore.QSize(40, 40))
        self.home.setObjectName("home")
        self.camera = QtWidgets.QPushButton(self.widget)
        self.camera.setGeometry(QtCore.QRect(150, 0, 150, 40))
        self.camera.setStyleSheet("QPushButton#camera{\n"
"    image: url(:/image/camera.jpg);\n"
"    background-color: rgba(127, 127, 129,255);\n"
"}\n"
"\n"
"QPushButton#camera:hover{\n"
"    background-color: rgba(159, 159, 162, 255);\n"
"}\n"
"\n"
"QPushButton#camera:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(127, 127, 129,255);\n"
"}")
        self.camera.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("camera.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camera.setIcon(icon1)
        self.camera.setIconSize(QtCore.QSize(50, 40))
        self.camera.setObjectName("camera")
        self.gallery = QtWidgets.QPushButton(self.widget)
        self.gallery.setGeometry(QtCore.QRect(300, 0, 150, 40))
        self.gallery.setStyleSheet("QPushButton#gallery{\n"
"    image: url(:/image/gallery.jpg);\n"
"    background-color: rgba(127, 127, 129,255);\n"
"}\n"
"\n"
"QPushButton#gallery:hover{\n"
"    background-color: rgba(159, 159, 162, 255);\n"
"}\n"
"\n"
"QPushButton#gallery:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(127, 127, 129,255);\n"
"}")
        self.gallery.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("gallery.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gallery.setIcon(icon2)
        self.gallery.setIconSize(QtCore.QSize(50, 35))
        self.gallery.setObjectName("gallery")
        self.settings = QtWidgets.QPushButton(self.widget)
        self.settings.setGeometry(QtCore.QRect(630, 0, 150, 40))
        self.settings.setStyleSheet("QPushButton#settings{\n"
"    image: url(:/image/settings.jpg);\n"
"    background-color: rgba(127, 127, 129,255);\n"
"}\n"
"\n"
"QPushButton#settings:hover{\n"
"    background-color: rgba(159, 159, 162, 255);\n"
"}\n"
"\n"
"QPushButton#settings:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(127, 127, 129,255);\n"
"}")
        self.settings.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("settings.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon3)
        self.settings.setIconSize(QtCore.QSize(40, 38))
        self.settings.setObjectName("settings")
        self.help = QtWidgets.QPushButton(self.widget)
        self.help.setGeometry(QtCore.QRect(780, 0, 150, 40))
        self.help.setStyleSheet("QPushButton#help{\n"
"    image: url(:/image/help.jpg);\n"
"    background-color: rgba(127, 127, 129,255);\n"
"}\n"
"\n"
"QPushButton#help:hover{\n"
"    background-color: rgba(159, 159, 162, 255);\n"
"}\n"
"\n"
"QPushButton#help:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(127, 127, 129,255);\n"
"}")
        self.help.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("help.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon4)
        self.help.setIconSize(QtCore.QSize(40, 38))
        self.help.setObjectName("help")
        self.exit = QtWidgets.QPushButton(self.widget, clicked = lambda: self.show_popup(MainWindow))
        self.exit.setGeometry(QtCore.QRect(930, 0, 150, 40))
        self.exit.setStyleSheet("QPushButton#exit{\n"
"    image: url(:/image/exit.jpg);\n"
"    background-color: rgba(127, 127, 129,255);\n"
"}\n"
"\n"
"QPushButton#exit:hover{\n"
"    background-color: rgba(159, 159, 162, 255);\n"
"}\n"
"\n"
"QPushButton#exit:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(127, 127, 129,255);\n"
"}")
        self.exit.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("exit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon5)
        self.exit.setIconSize(QtCore.QSize(40, 38))
        self.exit.setObjectName("exit")
        self.cameraFeed = QtWidgets.QLabel(self.widget)
        self.cameraFeed.setGeometry(QtCore.QRect(10, 60, 1060, 570))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.cameraFeed.setFont(font)
        self.cameraFeed.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 5px solid rgba(255, 255, 255)")
        self.cameraFeed.setScaledContents(False)
        self.cameraFeed.setObjectName("cameraFeed")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cameraFeed.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Camera Feed</p></body></html>"))

        # Confirm exit
    def show_popup(self, MainWindow):
            msg = QMessageBox()
            msg.setWindowTitle("iSecure")
            msg.setText("\nAre you sure you want to exit the program?\t\t\n")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            
            if QMessageBox.Yes:
                msg.buttonClicked.connect(MainWindow.close)
                
            else:
                pass    
        
            x = msg.exec_()         

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(window)
        window.show()
        sys.exit(app.exec_())
