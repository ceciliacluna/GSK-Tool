from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(500, 400, 500, 355)
        self.setWindowTitle("GSK Tool")
        self.initUI()

    def initUI(self):
        self.username = QtWidgets.QLabel(self)
        self.username.setText("username")
        self.username.move(30, 10)

        self.password = QtWidgets.QLabel(self)
        self.password.setText("password")
        self.password.move(30, 50)

        self.url = QtWidgets.QLabel(self)
        self.url.setText("url")
        self.url.move(30, 100)

        self.output_file_name = QtWidgets.QLabel(self)
        self.output_file_name.setText("Output File Name")
        self.output_file_name.move(30, 150)

        self.input_file_path = QtWidgets.QLabel(self)
        self.input_file_path.setText("Input File Path")
        self.input_file_path.move(30, 200)

        self.input_file_path = QtWidgets.QLabel(self)
        self.input_file_path.setText("Output File Path")
        self.input_file_path.move(30, 250)

        self.begin_button = QPushButton(self)
        self.begin_button.setText("Begin")
        self.begin_button.move(200, 300)
        # QtCore.QObject.connect(button, QtCore.SIGNAL('clicked()'), self.onClicked)
        self.begin_button.clicked.connect(self.begin_button)

        def begin_button():
            self.label.setText("You pressed the button")

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()

