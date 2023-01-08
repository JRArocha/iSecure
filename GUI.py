from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(500,200,300,300)
        self.setWindowTitle("THESIS GIU")
        self.initUI()
        
    def initUI(self):    
        self.label = QtWidgets.QLabel(self)
        self.label.setText("This is Label!")
        self.label.move(50,50)
        
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Button 1")
        self.b1.clicked.connect(self.clicked)
        
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Button 2")
        self.b2.clicked.connect(self.click)
        self.b2.move(100,0)
        
    def clicked(self):
        self.label.setText("Button 1 Clicked")
        self.update()
        
    def click(self):
        self.label.setText("Button 2 Clicked")
        self.update()
        
    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
    
window()