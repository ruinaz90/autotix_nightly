#! python3
# autotix_nightly_original.py - Automate nightly for fulfillment team

import pandas as pd
import ezsheets
import datetime
import csv

input_file = pd.read_csv("../Excel/AllSales3.csv")
keep_col = ['Name', 'Show', 'Performance Date', 'Confirmation Date', '# of Seats', 'Section', 'Row', 'Start',
            'End']
nightly_file = input_file[keep_col].sort_values(by=['Performance Date', 'Show', 'Name'], ascending=True)
nightly_file.to_csv("./Excel/AllSalesTest_Updated.csv", index=False)

bway_txt = open("./Excel/AllSalesTest_Updated.csv", "r", encoding="utf8")
bway_txt = "".join([i for i in bway_txt]).replace(" on Broadway", "")
nightly_file = open("./Excel/AllSalesTest_Updated.csv", "w", encoding="utf8")
nightly_file.writelines(bway_txt)
nightly_file.close()

ex_file = pd.read_csv("./Excel/AllSalesTest_Updated.csv")
ex_file.to_clipboard(excel=True, index=False)

nightly_csv = open('./Excel/AllSalesTest_Updated.csv', encoding="utf8")
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
