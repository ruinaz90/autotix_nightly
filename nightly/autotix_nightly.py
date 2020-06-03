#! python3
# autotix_nightly.py - Automate nightly

import ezsheets
import openpyxl
import pyexcel
import pyexcel
import os
from pathlib import Path

pyexcel.save_book_as(file_name='./Excel/AllSales1.xls', dest_file_name='./Excel/AllSales1.xlsx')

nightly_excel = openpyxl.load_workbook('./Excel/AllSales1.xlsx')
nightly_excel_sheet = nightly_excel.active

nightly_excel_sheet.delete_cols(1)
nightly_excel_sheet.delete_cols(2,5)
nightly_excel_sheet.delete_cols(4)
nightly_excel_sheet.delete_cols(10,9)
nightly_excel.save('./Excel/AllSales1_Updated.xlsx')
