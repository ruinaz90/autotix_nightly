import sys
from PyQt5 import QtWidgets, uic

from nightly.main_window import Ui_main_window


class main_window(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(main_window, self).__init__(*args, **kwargs)

        # Load the UI Page
        uic.loadUi('mainwindow.ui', self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_win = main_window()
    main_win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
