#! python3
# autotix_nightly_original.py - Automate nightly for fulfillment team

from pathlib import Path
import pandas as pd
import ezsheets
import datetime
import traceback
import logging


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


# Run the program
latest_path = latest_file()
sort_columns(latest_path)
nightly_doc_tab()
copy_clipboard(latest_path)
