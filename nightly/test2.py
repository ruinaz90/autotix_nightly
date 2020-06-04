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


nightly_gdoc = ezsheets.Spreadsheet('1EwvByoi9LIQPsqwFraAE38xaghENWKhyI-_c1_3yWEM')
nightly_gdoc.createSheet(todays_date_str)
current_sheet = nightly_gdoc[todays_date_str]

i = 1
for data in nightly_data:
    current_sheet.updateRow(i, data)
    i += 1




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




import sys
from PyQt5 import QtWidgets, uic

from nightly.main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Load the UI Page
        uic.loadUi('mainwindow.ui', self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
