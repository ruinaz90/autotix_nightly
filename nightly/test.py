import datetime
import ezsheets
import pyperclip
import csv

nightly_csv = open('./Excel/AllSalesTest_Updated.csv')
nightly_reader = csv.reader(nightly_csv)
nightly_data = list(nightly_reader)

todays_date = datetime.datetime.now()
todays_date_str = todays_date.strftime('%m/%d/%y')

nightly_gdoc = ezsheets.Spreadsheet('1EwvByoi9LIQPsqwFraAE38xaghENWKhyI-_c1_3yWEM')
nightly_gdoc.createSheet(todays_date_str)
current_sheet = nightly_gdoc[todays_date_str]

i = 1
for data in nightly_data:
    current_sheet.updateRow(i, data)
    i += 1

nightly_gdoc.refresh()
