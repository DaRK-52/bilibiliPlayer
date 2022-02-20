import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(200, 200)
    w.setWindowTitle("1111")
    w.show()
    app.exec()