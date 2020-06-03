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
