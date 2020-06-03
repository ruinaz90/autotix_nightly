import datetime
import ezsheets
import pyperclip

todays_date = datetime.datetime.now()
todays_date_str = todays_date.strftime('%m/%d/%y')

nightly_gdoc = ezsheets.Spreadsheet('1EwvByoi9LIQPsqwFraAE38xaghENWKhyI-_c1_3yWEM')
nightly_gdoc.createSheet(todays_date_str)
current_sheet = nightly_gdoc[todays_date_str]
current_sheet['A1'] = pyperclip.paste()

nightly_gdoc.refresh()
