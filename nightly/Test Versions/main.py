#! python3
# AutoTix Nightly - Nightly automation for fulfillment team
# main.py - Main file

# GUI import
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic
from pathlib import Path

# Code import
import sys
import pandas as pd
import ezsheets
import datetime

# Logging import
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
# logging.disable(logging.CRITICAL)


qt_creator_file = "mainwindow.ui"    # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)


# AutoTix Nightly functions
def copy_clipboard(report_filename):
    # Copy report contents to clipboard
    ex_file = pd.read_csv(report_filename)
    ex_file.to_clipboard(excel=True, index=False)
    logging.debug("Information is ready! Go to the Nightly Check-in doc and paste it in the tab with today's date!")


def latest_file():
    # Find the latest sales report file
    folder_path = Path('C:/autotix/nightly/Excel')
    list_of_paths = folder_path.glob('*.csv')
    recent_file = max(list_of_paths, key=lambda p: p.stat().st_ctime)
    logging.debug("Most recent report is " + str(recent_file) + ".")
    return recent_file


def nightly_doc_tab():
    # Get today's date
    todays_date = datetime.datetime.now()
    todays_date_str = todays_date.strftime('%m/%d/%y')

    # Create new tab in nightly doc and name it with today's date
    nightly_gdoc = ezsheets.Spreadsheet('1EwvByoi9LIQPsqwFraAE38xaghENWKhyI-_c1_3yWEM')
    try:
        nightly_gdoc.createSheet(todays_date_str)
        logging.debug("New tab created in Nightly doc: " + todays_date_str + "...")
    except:
        logging.debug("Sheet titled '" + todays_date_str + "' already exists.")


def sort_columns(report_filename):
    # Remove and sort columns
    input_file = pd.read_csv(report_filename)
    keep_col = ['Name', 'Show', 'Performance Date', 'Confirmation Date', '# of Seats', 'Section', 'Row', 'Start', 'End']
    nightly_file = input_file[keep_col].sort_values(by=['Performance Date', 'Show', 'Name'], ascending=True)
    nightly_file.to_csv(report_filename, index=False)
    logging.debug("Sorting " + str(report_filename) + "...")

    # Remove "on Broadway" from show names
    bway_txt = open(report_filename, 'r', encoding='utf8')
    bway_txt = ''.join([i for i in bway_txt]).replace(' on Broadway', '')
    nightly_file = open(report_filename, 'w', encoding='utf8')
    nightly_file.writelines(bway_txt)
    nightly_file.close()
    logging.debug("Cleaning up show names...")


# GUI functions
def menu_instructions_clicked():
    logging.debug("Instructions clicked!")
    msg = QMessageBox()
    msg.setWindowTitle("Instructions")
    msg.setText("AutoTix Nightly is an app that automates part of nightly check-in for the fulfillment team."
                "\n\n1. Pull a sales report on CMS and export it as a CSV. Save this file to the Downloads folder."
                "\n\n2. Click the Run button in this app. A popup will appear when the app finishes running. Click OK."
                " You can close the app after this."
                "\n\n3. Go to the Nightly Check-in doc and click on the tab with today's date."
                "\n\n4. Paste the data in cell A1.")
    msg.exec_()


def menu_about_clicked():
    msg = QMessageBox()
    msg.setWindowTitle("About")
    msg.setText("AutoTix Nightly\nVersion 1.0, built on June 8, 2020\n\nCopyright © 2020")
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
        logging.debug("Run button clicked!")
        latest_path = latest_file()
        self.progress_bar.setValue(25)
        sort_columns(latest_path)
        self.progress_bar.setValue(50)
        nightly_doc_tab()
        self.progress_bar.setValue(75)
        copy_clipboard(latest_path)
        self.progress_bar.setValue(100)
        msg = QMessageBox()
        msg.setWindowTitle("Done")
        msg.setText("Information is ready! Go to the Nightly Check-in doc and paste it in the tab with today's date!")
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
