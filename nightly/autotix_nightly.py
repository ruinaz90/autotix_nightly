#! python3
# autotix_nightly.py - Automate nightly

import openpyxl
import ezsheets

spreadsheet = ezsheets.Spreadsheet('1EwvByoi9LIQPsqwFraAE38xaghENWKhyI-_c1_3yWEM')
print(spreadsheet.title)
