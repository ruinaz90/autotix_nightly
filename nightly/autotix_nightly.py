#! python3
# autotix_nightly.py - Automate nightly for fulfillment team

import pandas as pd
import csv

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
