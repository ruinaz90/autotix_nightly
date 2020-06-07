import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic
from pathlib import Path
import pandas as pd
import ezsheets
import datetime

qt_creator_file = "mainwindow.ui"    # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)


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
def menu_instructions_clicked():
    print("Instructions clicked!")


def menu_about_clicked():
    msg = QMessageBox()
    msg.setWindowTitle("About")
    msg.setText("AutoTix Nightly\nVersion 1.0, built on June 4, 2020\n\nCopyright © 2020")
    msg.exec_()


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.run_button.clicked.connect(self.run_clicked)
        self.menu_instructions.triggered.connect(menu_instructions_clicked)
        self.menu_about.triggered.connect(menu_about_clicked)

    def run_clicked(self):
        print("Run button clicked!")
        latest_path = latest_file()
        self.progress_bar.setValue(10)
        # sort_columns(latest_path)
        # nightly_doc_tab()
        # copy_clipboard(latest_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
