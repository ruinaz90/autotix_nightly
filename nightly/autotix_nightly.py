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
'''
example_file = open("./Excel/AllSalesTest_Updated.csv")
example_reader = csv.DictReader(example_file)
example_list = list(example_reader)

output_file = open("./Excel/AllSalesTest_Updated2.csv", "w", newline="")
output_dict_writer = csv.DictWriter(output_file, ['Name', 'Show', 'Performance Date', 'Confirmation Date',
                                                  '# of Seats', 'Section', 'Row', 'Start', 'End'])

prev_show = example_list[0]['Show']

for row in example_list:
    current_show = row['Show']
    if current_show == prev_show:
        continue
    else:
        prev_show = current_show
        output_dict_writer.writerow({'Name': ''})
'''
