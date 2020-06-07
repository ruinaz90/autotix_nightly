from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pathlib import Path
import pandas as pd
import ezsheets
import datetime


# AutoTix Nightly functions
def copy_clipboard(report_filename):
    # Copy report contents to clipboard
    ex_file = pd.read_csv(report_filename)
    ex_file.to_clipboard(excel=True, index=False)
    print("Data copied to clipboard! Please paste into the Nightly Check-in doc!")


def latest_file():
    # Find the latest sales report file
    folder_path = Path('C:/Users/arenz/PycharmProjects/autotix/nightly/Excel')
    list_of_paths = folder_path.glob('*.csv')
    recent_file = max(list_of_paths, key=lambda p: p.stat().st_ctime)
    print("Most recent report is " + str(recent_file) + ".")
    return recent_file


def nightly_doc_tab():
    # Get today's date
    todays_date = datetime.datetime.now()
    todays_date_str = todays_date.strftime('%m/%d/%y')

    # Create new tab in nightly doc and name it with today's date
    nightly_gdoc = ezsheets.Spreadsheet('1EwvByoi9LIQPsqwFraAE38xaghENWKhyI-_c1_3yWEM')
    try:
        nightly_gdoc.createSheet(todays_date_str)
        print("New tab created in Nightly doc: " + todays_date_str + "...")
    except:
        print("Sheet titled '" + todays_date_str + "' already exists.")


def sort_columns(report_filename):
    # Remove and sort columns
    input_file = pd.read_csv(report_filename)
    keep_col = ['Name', 'Show', 'Performance Date', 'Confirmation Date', '# of Seats', 'Section', 'Row', 'Start', 'End']
    nightly_file = input_file[keep_col].sort_values(by=['Performance Date', 'Show', 'Name'], ascending=True)
    nightly_file.to_csv(report_filename, index=False)
    print("Sorting " + str(report_filename) + "...")

    # Remove "on Broadway" from show names
    bway_txt = open(report_filename, 'r', encoding='utf8')
    bway_txt = ''.join([i for i in bway_txt]).replace(' on Broadway', '')
    nightly_file = open(report_filename, 'w', encoding='utf8')
    nightly_file.writelines(bway_txt)
    nightly_file.close()
    print("Cleaning up show names...")


# GUI functions
def run_clicked():
    print("Run button clicked!")
    #latest_path = latest_file()
    #sort_columns(latest_path)
    #nightly_doc_tab()
    #copy_clipboard(latest_path)


def menu_instructions_clicked():
    print("Instructions clicked!")


def menu_about_clicked():
    msg = QMessageBox()
    msg.setWindowTitle("About")
    msg.setText("AutoTix Nightly\nVersion 1.0, built on June 4, 2020\n\nCopyright © 2020")
    msg.exec_()


# Qt Creator
class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout.addWidget(self.progress_bar, 3, 1, 1, 1)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setText("")
        self.logo.setPixmap(
            QtGui.QPixmap("C:\\Users\\Ruina\\PycharmProjects\\autotix\\nightly\\../1x/logo_nightly_sm.png"))
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 0, 1, 2)
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setObjectName("run_button")
        self.gridLayout.addWidget(self.run_button, 3, 0, 1, 1)
        self.text_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_browser.setObjectName("text_browser")
        self.gridLayout.addWidget(self.text_browser, 1, 0, 1, 2)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 389, 21))
        self.menubar.setObjectName("menubar")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.menu_about = QtWidgets.QAction(main_window)
        self.menu_about.setObjectName("menu_about")
        self.menu_instructions = QtWidgets.QAction(main_window)
        self.menu_instructions.setObjectName("menu_instructions")
        self.menu_help.addAction(self.menu_instructions)
        self.menu_help.addAction(self.menu_about)
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        self.run_button.clicked.connect(run_clicked)
        self.menu_instructions.triggered.connect(menu_instructions_clicked)
        self.menu_about.triggered.connect(menu_about_clicked)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "AutoTix Nightly"))
        self.run_button.setText(_translate("main_window", "Run"))
        self.text_browser.setHtml(_translate("main_window",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Make sure you have pulled a report and saved it to your </span><span style=\" font-size:9pt; font-weight:600;\">Downloads</span><span style=\" font-size:9pt;\"> folder.</span></p>\n"
                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Click </span><span style=\" font-size:9pt; font-weight:600;\">Run</span><span style=\" font-size:9pt;\"> to begin.</span></p></body></html>"))
        self.menu_help.setTitle(_translate("main_window", "Help"))
        self.menu_about.setText(_translate("main_window", "About"))
        self.menu_instructions.setText(_translate("main_window", "Instructions"))
