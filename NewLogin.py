from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MainWindow import Ui_MainWindow
import sys, res
from time import sleep
import pymysql

class Ui_Form(object):
    def openWindow(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(929, 718)
        icon = QIcon()
        icon.addPixmap(QPixmap("logo.jpg"), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(30, 30, 791, 621))
        self.widget.setObjectName("widget")
        self.label = QLabel(self.widget)
        self.label.setGeometry(QRect(40, 30, 361, 561))
        self.label.setStyleSheet("background-color: rgba(47,47,47);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.widget)
        self.label_2.setGeometry(QRect(400, 30, 341, 561))
        self.label_2.setStyleSheet("background-color: rgb(47,47,47,);\n"
"border-bottom-right-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setGeometry(QRect(50, 150, 371, 351))
        self.label_3.setStyleSheet("border-image: url(:/image/logo.jpg);\n"
"border-top-left-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setGeometry(QRect(510, 170, 141, 51))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setGeometry(QRect(460, 250, 225, 50))
        self.lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(255,255,255,200);\n"
"color: rgba(255,255,255,240);\n"
"padding-bottom: 7px;\n"
"text-color: white;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setGeometry(QRect(460, 330, 225, 40))
        self.lineEdit_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(255,255,255,200);\n"
"color: rgba(255,255,255,240);\n"
"padding-bottom: 7px;\n"
"text-color: white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QPushButton(self.widget, clicked = lambda: self.login())
        self.pushButton.setGeometry(QRect(480, 420, 180, 35))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"    background-color: rgb(0, 72, 216);\n"
"    color: rgba(255,255,255,255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(0, 72, 216);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.clicked.connect(Form.close)
        self.pushButton_2.setGeometry(QRect(700, 50, 29, 28))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2 {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(218, 0, 0);\n"
"    color: rgba(255,255,255,255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover {\n"
"    background-color: rgb(245, 0, 0);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(218, 0, 0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

        self.counter = 3
        
    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        con = pymysql.connect(host="localhost",user="root",password="",db="isecure")
        cur = con.cursor()
        query = "SELECT * FROM logindb WHERE username = %s AND password = %s"
        data = cur.execute(query,(username,password))
        if (len(cur.fetchall())>0):
                Form.close()
                self.window = QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.window)
                self.window.show()
                
        else:   
                if self.counter == 0:
                     sys.exit()

                else:
                     self.warning("Alert", f"Attempts remaining {self.counter}")
                     self.counter -= 1
                     
    def warning(self, title, message):
        text = QMessageBox()
        text.setWindowTitle(title)
        text.setText(message)
        text.setStandardButtons(QMessageBox.Ok)
        text.exec_()

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Login"))
        self.pushButton_2.setText(_translate("Form", "X"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
