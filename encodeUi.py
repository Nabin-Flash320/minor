
from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib
import Steganography.text_to_image as tti
import Steganography.text_to_audio as tta

class combo(QtWidgets.QComboBox):

    def __init__(self, name, parent):
        super(combo, self).__init__(parent)
        self.setObjectName(name)


class lineEdit(QtWidgets.QLineEdit):
    def __init__(self, name, parent, drop=False):
        super(lineEdit, self).__init__(parent)
        self.setObjectName(name)
        self.setAcceptDrops(drop)

    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.file_path_name = pathlib.Path(e.mimeData().text())
        self.file_name = self.file_path_name.name
        # self.setText(self.file_path_name)
        self.setText(e.mimeData().text())
       
        


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

        #----------------From's----------------#
        #Label
        self.fromLabel = QtWidgets.QLabel(self.centralwidget)
        self.fromLabel.setGeometry(QtCore.QRect(170, 70, 111, 21))
        self.fromLabel.setObjectName("fromLabel")
        
        #Line Edit
        self.inputLineEdit = lineEdit("inputLineEdit", self.centralwidget)
        self.inputLineEdit.setGeometry(QtCore.QRect(210, 110, 113, 25))
        
        #Combo Box
        self.fromComboBox = combo("fromComboBox", self.centralwidget)
        self.fromComboBox.setGeometry(QtCore.QRect(100, 110, 86, 25))
        self.from_items = ['Text', 'Image']
        self.fromComboBox.addItems(self.from_items)
        self.fromComboBox.currentIndexChanged.connect(self.from_selectionchange)
        self.fromComboBox.setItemText(2, "")


        #----------------To's----------------#
        #Label
        self.toLabel = QtWidgets.QLabel(self.centralwidget)
        self.toLabel.setGeometry(QtCore.QRect(160, 180, 67, 17))
        self.toLabel.setObjectName("toLabel")
        
        #Combo Box
        self.toComboBox = combo('toComboBox', self.centralwidget)
        self.toComboBox.setGeometry(QtCore.QRect(100, 200, 86, 25))
        self.to_items = ['Text', 'Image', 'Audio']
        self.toComboBox.addItems(self.to_items)
        self.toComboBox.currentIndexChanged.connect(self.to_selectionchange)


        #Line Edit
        self.toLineEdit = lineEdit("toLineEdit", self.centralwidget, drop=True)
        self.toLineEdit.setGeometry(QtCore.QRect(210, 200, 113, 25))

        #Encode button
        self.Encode = QtWidgets.QPushButton(self.centralwidget)
        self.Encode.setGeometry(QtCore.QRect(160, 260, 89, 25))
        self.Encode.setObjectName("Encode")
        self.Encode.clicked.connect(self.encode_call_back)
        MainWindow.setCentralWidget(self.centralwidget)

        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fromLabel.setText(_translate("MainWindow", "From"))
        self.toLabel.setText(_translate("MainWindow", "To"))
        self.Encode.setText(_translate("MainWindow", "Encode"))

    def from_selectionchange(self, i):
        if i == 0:
            self.toComboBox.clear()
            self.to_items = ['Text', 'Image', 'Audio']
            self.toComboBox.addItems(self.to_items)
            self.inputLineEdit.setAcceptDrops(False)
            self.inputLineEdit.clear()
            self.toLineEdit.clear()
        else:
            self.toComboBox.clear()
            self.to_items = ['Image']
            self.toComboBox.addItems(self.to_items)
            self.inputLineEdit.setAcceptDrops(True)
            self.inputLineEdit.clear()
            self.toLineEdit.clear()

    def to_selectionchange(self, i):
        self.toLineEdit.clear()

    def encode_call_back(self):
        if self.fromComboBox.currentText() == "Text":
            if self.toComboBox.currentText() == "Image":
                self.message = self.inputLineEdit.text()
                self.file_path = pathlib.Path(self.toLineEdit.file_path_name)
                self.text_to_image = tti.textToImage()
                self.text_to_image.text_to_image(self.message, self.file_path)
            elif self.toComboBox.currentText() == "Audio":
                self.message = self.inputLineEdit.text()
                self.file_path = pathlib.Path(self.toLineEdit.file_path_name)
                self.text_to_audio = tta.TextToAudio()
                self.text_to_audio.encode(self.message, self.file_path)
        else:
            pass





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
