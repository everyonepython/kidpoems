# coding=utf8
import sys

from base import context
from call_stackwidget import MyStackWidget


if __name__ == '__main__':
    my_window = MyStackWidget()
    my_window.show()
    exit_code = context.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
