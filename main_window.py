

from PyQt5 import QtCore, QtGui, QtWidgets
import encodeUi as eui
import decodeUi as dui
import Steganography.audio_to_text

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background-color: rgb(56, 67, 84);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #encode button
        self.Encode_Btn = QtWidgets.QPushButton(self.frame)
        self.Encode_Btn.setGeometry(QtCore.QRect(170, 150, 89, 31))
        self.Encode_Btn.setObjectName("Encode_Btn")
        self.Encode_Btn.clicked.connect(self.encode_call)

        #decode button
        self.Decode_Btn = QtWidgets.QPushButton(self.frame)
        self.Decode_Btn.setGeometry(QtCore.QRect(170, 220, 89, 31))
        self.Decode_Btn.setObjectName("Decode_Btn")
        self.Decode_Btn.clicked.connect(self.decode_call)

        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def encode_call(self):
        self.encode_window = QtWidgets.QMainWindow()
        self.encode_ui = eui.Ui_MainWindow()
        self.encode_ui.setupUi(self.encode_window)
        self.encode_window.show()


    def decode_call(self):
        self.decode_window = QtWidgets.QMainWindow()
        self.decode_ui = dui.Ui_MainWindow()
        self.decode_ui.setupUi(self.decode_window)
        self.decode_window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Encode_Btn.setText(_translate("MainWindow", "Encode"))
        self.Decode_Btn.setText(_translate("MainWindow", "Decode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
