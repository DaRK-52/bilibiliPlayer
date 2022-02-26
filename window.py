import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from function import *


class main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.setWindowTitle("Bilibili Player")
        self.setFixedSize(400, 600)
        self.show()

    def init_window(self):
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.main_layout)

        self.top_layout = QGridLayout()  # 这个是整个控件里面的对齐

        self.title_label = QLabel("Title")  # 这个是控件Qlabel里面的对齐
        self.title_label.setAlignment(Qt.AlignCenter)
        self.top_layout.addWidget(self.title_label)

        self.button_layout = QHBoxLayout()
        self.button_layout.setAlignment(Qt.AlignBottom)
        self.pause_button = QPushButton("pause_button")
        self.next_button = QPushButton("next_button")
        self.mode_button = QPushButton("mode_button")
        self.pause_button.lower()
        self.next_button.lower()
        self.mode_button.lower()

        # self.pause_button.clicked.connect()

        self.button_layout.addWidget(self.mode_button)
        self.button_layout.addWidget(self.pause_button)
        self.button_layout.addWidget(self.next_button)

        test_label = QLabel()
        pixmap = QPixmap("test.png")
        test_label.setPixmap(pixmap)

        self.main_layout.setVerticalSpacing(50)
        self.main_layout.addLayout(self.top_layout, 0, 0)
        self.main_layout.addWidget(test_label, 1, 0)
        self.main_layout.addLayout(self.button_layout, 10, 0, -1, -1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()  # ui_from是类名
    ui.setupUi(MainWindow)
    MainWindow.show()
    # window = main_window()
    sys.exit(app.exec_())
