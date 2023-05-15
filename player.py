from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 740)
        Form.setWindowFlags(Qt.FramelessWindowHint)


        self.closeButton = QPushButton(Form)
        self.closeButton.clicked.connect(Form.close)
        self.closeButton.setGeometry(QRect(1210, 0, 60, 30))
        self.closeButton.setStyleSheet("background-color: rgb(218, 0, 0); \n"
                                       "color: rgb(237, 237, 237, 237);")
        # file = location
        self.tutorialWidget = QWidget(Form)
        self.tutorialWidget.setGeometry(QRect(0, 20, 1280, 720))
        self.tutorialWidget.setObjectName("tutorialWidget")

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.playButton = QPushButton(Form)
        self.playButton.clicked.connect(self.play)

        

        videoWidget = QVideoWidget(self.tutorialWidget)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("Dangerously.mp4"))) 

        Layout = QHBoxLayout()
        Layout.setContentsMargins(0, 0, 0, 0)
        Layout.addWidget(self.playButton)
        Layout.addWidget(self.positionSlider)

        frame = QVBoxLayout()
        
        frame.addWidget(videoWidget)
        frame.addLayout(Layout)

        self.tutorialWidget.setLayout(frame)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

        self.tutorialWidget.raise_()
        self.playButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.playButton.setText(_translate("Form", "Play / Pause"))
        self.closeButton.setText(_translate("Form", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
