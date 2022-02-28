from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from main_window import *
from function import *
import function


class my_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(my_window, self).__init__(parent)
        function.change_mod(['chmod', 'random'])
        self.setupUi(self)
