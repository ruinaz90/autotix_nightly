#! python3
# autotix_nightly.py - Automate nightly for fulfillment team

import pandas as pd
import csv
import ezsheets
import datetime

input_file = pd.read_csv("./Excel/AllSalesTest.csv")
keep_col = ['Name', 'Show', 'Performance Date', 'Confirmation Date', '# of Seats', 'Section', 'Row', 'Start',
            'End']
nightly_file = input_file[keep_col].sort_values(by=['Performance Date', 'Show', 'Name'], ascending=True)
nightly_file.to_csv("./Excel/AllSalesTest_Updated.csv", index=False)

bway_txt = open("./Excel/AllSalesTest_Updated.csv", "r")
bway_txt = "".join([i for i in bway_txt]).replace(" on Broadway", "")
nightly_file = open("./Excel/AllSalesTest_Updated.csv", "w")
nightly_file.writelines(bway_txt)
nightly_file.close()

todays_date = datetime.datetime.now()
todays_date_str = todays_date.strftime('%m/%d')

ex_file = pd.read_csv("./Excel/AllSalesTest_Updated.csv")
ex_file.to_clipboard(excel=True, sep=None, index=False)
