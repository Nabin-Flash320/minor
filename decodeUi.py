
from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib
import Steganography.image_to_text as itt
import Steganography.audio_to_text as att

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
        self.input_image_flag = False
        self.input_audio_flag = False

        #----------Input----------#
        #input file label
        self.inputFileLabel = QtWidgets.QLabel(self.frame)
        self.inputFileLabel.setGeometry(QtCore.QRect(90, 110, 67, 17))
        self.inputFileLabel.setObjectName("inputFileLabel")

        #input line edit
        self.inputLineEdit = QtWidgets.QLineEdit(self.frame)
        self.inputLineEdit.setGeometry(QtCore.QRect(190, 110, 113, 25))
        self.inputLineEdit.setObjectName("inputLineEdit")

        #browesw push button
        self.browsePushButton = QtWidgets.QPushButton(self.frame)
        self.browsePushButton.setGeometry(QtCore.QRect(320, 110, 58, 25))
        self.browsePushButton.setObjectName("pushButton")
        self.browsePushButton.clicked.connect(self.open_file_dialouge)


        #----------Decode----------#
        # decode label
        self.DecodeLabel = QtWidgets.QLabel(self.frame)
        self.DecodeLabel.setGeometry(QtCore.QRect(90, 170, 71, 20))
        self.DecodeLabel.setObjectName("DecodeLabel")

        #decode push button
        self.decodePushButton = QtWidgets.QPushButton(self.frame)
        self.decodePushButton.setGeometry(QtCore.QRect(148, 230, 89, 25))
        self.decodePushButton.setObjectName("decodePushButton")
        self.decodePushButton.clicked.connect(self.decode_call_back)

        #decode combo box
        self.decodeComboBox = QtWidgets.QComboBox(self.frame)
        self.decodeComboBox.setGeometry(QtCore.QRect(190, 170, 111, 25))
        self.decodeComboBox.setObjectName("decodeComboBox")
        self.decode_items = ["Text", "Image", "Audio"]
        self.decodeComboBox.addItems(self.decode_items)

        
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_file_dialouge(self):
        self.path = QtWidgets.QFileDialog.getOpenFileName()
        self.file_suffix = [".txt", ".png", ".wav"]
        self.file_path = pathlib.Path(self.path[0])
        if self.file_path.suffix in self.file_suffix:
            self.inputLineEdit.setText(self.file_path.name)
            if self.inputLineEdit.text().split('.')[-1] == "txt":
                self.decodeComboBox.clear()
                self.to_items = ['Text']
                self.decodeComboBox.addItems(self.to_items)
            elif self.inputLineEdit.text().split('.')[-1] == "png":
                self.decodeComboBox.clear()
                self.to_items = ['Text', 'Image']
                self.decodeComboBox.addItems(self.to_items)
                self.input_image_flag = True
                self.input_audio_flag = False
            else:
                self.decodeComboBox.clear()
                self.to_items = ['Text']
                self.decodeComboBox.addItems(self.to_items)
                self.input_image_flag = False
                self.input_audio_flag = True
        else:
            if len(str(self.path[0])) == 0:
                pass
            else:
                self.message = QtWidgets.QMessageBox()
                self.message.setIcon(QtWidgets.QMessageBox.Warning)
                self.message.setWindowTitle("Warning")
                self.message.setText("Wrong file format")
                self.message.setInformativeText("*.txt, *.png and *.wav files are acceptable.")
                self.message.setStandardButtons(QtWidgets.QMessageBox.Ok)
                self.message.exec_()
        
    def decode_call_back(self):
        if self.decodeComboBox.currentText() == "Text":
            if self.input_image_flag == True:
                self.image_to_text = itt.ImageToText(self.file_path)
                self.msg = self.image_to_text.decode()
                print("The encoded message is {}".format(self.msg))

            if self.input_audio_flag == True:
                self.audio_to_text = att.AudioToText()
                self.msg = self.audio_to_text.decode(self.file_path)
               



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputFileLabel.setText(_translate("MainWindow", "Input File"))
        self.DecodeLabel.setText(_translate("MainWindow", "Decode to "))
        self.decodePushButton.setText(_translate("MainWindow", "Decode"))
        self.browsePushButton.setText(_translate("MainWindow", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
