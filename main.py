# coding=utf8
import sys

from PyQt5.QtWidgets import QApplication

from call_stackwidget import MyStackWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyStackWidget()
    my_window.show()
    sys.exit(app.exec())
