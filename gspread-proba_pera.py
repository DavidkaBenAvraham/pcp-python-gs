# https://github.com/google/gdata-python-client
# https://docs.gspread.org/en/latest/#


# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('pcp-python-gs-11dd4d9f2a40.json', scope)
gc = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.

#ss = gc.open(https://docs.google.com/spreadsheets/d/19QXhtuzfPccHqLPLOuvxsVchiHCdoJxTmdSfU_gtrDs)

ss = gc.open_by_key('19QXhtuzfPccHqLPLOuvxsVchiHCdoJxTmdSfU_gtrDs')

shts = ss.worksheets


## Extract and print all of the values
#list_of_hashes = ss.get_all_records()
#print(list_of_hashes)
