#! python3
# autotix_nightly.py - Automate nightly for fulfillment team

import pandas

input_file = pandas.read_csv("./Excel/AllSales3.csv")
keep_col = ['Name', 'Show', 'Performance Date', 'Confirmation Date', '# of Seats', 'Section', 'Row', 'Start',
            'End']

nightly_file = input_file[keep_col].sort_values(by=['Performance Date', 'Show', 'Name'], ascending=True)
nightly_file.to_csv("./Excel/AllSales3_Updated.csv", index=False)
